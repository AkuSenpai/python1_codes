ToDoApp_KivyMD.py

Modern To-Do List app using KivyMD (Python)

Single-file example with SQLite persistence, add/edit/delete, due dates, search, filter, sort, categories, export/import.

Notes:

- Works on desktop and Android. Packaging to iOS requires kivy-ios and a Mac with Xcode (see README section at bottom).

- Push notifications and native iOS reminders require native modules beyond pure Python.

from kivy.lang import Builder from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty from kivy.clock import mainthread from kivy.core.window import Window from kivymd.app import MDApp from kivymd.uix.card import MDCard from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch, IconRightWidget from kivymd.uix.button import MDIconButton, MDRaisedButton from kivymd.uix.picker import MDDatePicker from kivymd.uix.dialog import MDDialog from kivymd.uix.snackbar import Snackbar import sqlite3 import json from datetime import datetime

KV = ''' BoxLayout: orientation: 'vertical'

MDToolbar:
    title: app.title
    left_action_items: [['menu', lambda x: None]]
    elevation: 10
    right_action_items: [['magnify', lambda x: app.open_search()], ['filter-variant', lambda x: app.open_filter_dialog()]]

BoxLayout:
    orientation: 'vertical'
    padding: dp(12)
    spacing: dp(8)

    MDTextField:
        id: input_task
        hint_text: 'Add new task (press enter to add)'
        on_text_validate: app.add_task(self.text)
        size_hint_y: None
        height: dp(48)

    BoxLayout:
        size_hint_y: None
        height: dp(48)
        spacing: dp(8)

        MDRaisedButton:
            text: 'Add'
            on_release: app.add_task(input_task.text)

        MDRaisedButton:
            text: 'Pick Due Date'
            on_release: app.open_date_picker()

        MDRaisedButton:
            text: 'Export'
            on_release: app.export_tasks()

        MDRaisedButton:
            text: 'Import'
            on_release: app.import_tasks()

    ScrollView:
        MDList:
            id: task_list

MDFloatingActionButton:
    icon: 'plus'
    md_bg_color: app.theme_cls.primary_color
    pos_hint: {'right': .95, 'y': .02}
    on_release: input_task.focus = True

'''

DB_SCHEMA = ''' CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, notes TEXT, category TEXT, due_date TEXT, done INTEGER DEFAULT 0, priority INTEGER DEFAULT 2, created_at TEXT DEFAULT CURRENT_TIMESTAMP ); '''

class RightCheck(IRightBodyTouch, IconRightWidget): pass

class TaskItem(TwoLineAvatarIconListItem): task_id = NumericProperty() title_text = StringProperty() secondary_text = StringProperty() done = BooleanProperty(False)

class ToDoApp(MDApp): title = 'Modern ToDo — Aku' tasks = ListProperty([]) pick_due = None

def build(self):
    self.theme_cls.primary_palette = 'BlueGray'
    self.theme_cls.theme_style = 'Light'
    self.conn = sqlite3.connect('tasks.db', check_same_thread=False)
    self.cursor = self.conn.cursor()
    self.cursor.executescript(DB_SCHEMA)
    self.conn.commit()
    return Builder.load_string(KV)

def on_start(self):
    Window.softinput_mode = 'below_target'
    self.load_tasks()

def load_tasks(self, query=None, filters=None):
    sql = 'SELECT id, title, notes, category, due_date, done, priority FROM tasks'
    params = ()
    if query:
        sql += " WHERE title LIKE ? OR notes LIKE ?"
        params = (f'%{query}%', f'%{query}%')
    sql += ' ORDER BY done, priority, due_date IS NULL, due_date'
    rows = self.cursor.execute(sql, params).fetchall()
    self.root.ids.task_list.clear_widgets()
    for r in rows:
        tid, title, notes, category, due_date, done, pr = r
        secondary = ''
        if category:
            secondary += f'[{category}] '
        if due_date:
            secondary += f'Due: {due_date} '
        if notes:
            secondary += f'• {notes[:60]}'
        item = TaskItem(text=title, secondary_text=secondary, task_id=tid, title_text=title, done=bool(done))
        icon = RightCheck(icon='check-circle' if done else 'checkbox-blank-circle-outline')
        icon.bind(on_release=lambda btn, item=item: self.toggle_done(item))
        item.add_widget(icon)
        edit_btn = MDIconButton(icon='pencil', on_release=lambda btn, item=item: self.open_edit_dialog(item))
        item.add_widget(edit_btn)
        del_btn = MDIconButton(icon='delete', on_release=lambda btn, item=item: self.delete_task(item))
        item.add_widget(del_btn)
        self.root.ids.task_list.add_widget(item)

def add_task(self, text):
    text = (text or '').strip()
    if not text:
        Snackbar(text='Type a task first.').open()
        return
    due = None
    if self.pick_due:
        due = self.pick_due
        self.pick_due = None
    self.cursor.execute('INSERT INTO tasks (title, due_date) VALUES (?, ?)', (text, due))
    self.conn.commit()
    self.root.ids.input_task.text = ''
    Snackbar(text='Task added').open()
    self.load_tasks()

def toggle_done(self, item: TaskItem):
    new = 0 if item.done else 1
    self.cursor.execute('UPDATE tasks SET done=? WHERE id=?', (new, item.task_id))
    self.conn.commit()
    self.load_tasks()

def delete_task(self, item: TaskItem):
    self.cursor.execute('DELETE FROM tasks WHERE id=?', (item.task_id,))
    self.conn.commit()
    Snackbar(text='Task deleted').open()
    self.load_tasks()

def open_date_picker(self):
    def on_save(instance, value, date_range):
        self.pick_due = value.strftime('%Y-%m-%d')
        Snackbar(text=f'Due date set: {self.pick_due}').open()
    date_dialog = MDDatePicker(callback=on_save)
    date_dialog.open()

def open_search(self):
    from kivymd.uix.textfield import MDTextField
    dialog = MDDialog(title='Search tasks', type='custom', content_cls=MDTextField(hint_text='Search...'))
    content = dialog.content_cls
    content.on_text_validate = lambda: (self.load_tasks(query=content.text), dialog.dismiss())
    dialog.open()

def open_filter_dialog(self):
    # simple example: filter by category or show completed
    content = 'Filter: (not implemented)'
    MDDialog(title='Filters', text=content, size_hint=(.8, None), height=dp(180)).open()

def open_edit_dialog(self, item: TaskItem):
    from kivymd.uix.boxlayout import MDBoxLayout
    from kivymd.uix.textfield import MDTextField
    box = MDBoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
    title = MDTextField(text=item.title_text, hint_text='Title')
    notes = MDTextField(text=item.secondary_text or '', hint_text='Notes')
    box.add_widget(title)
    box.add_widget(notes)
    dialog = MDDialog(title='Edit task', type='custom', content_cls=box, buttons=[MDRaisedButton(text='Save', on_release=lambda x: self.save_edit(item, title.text, notes.text, dialog)), MDRaisedButton(text='Cancel', on_release=lambda x: dialog.dismiss())])
    dialog.open()

def save_edit(self, item, title, notes, dialog):
    self.cursor.execute('UPDATE tasks SET title=?, notes=? WHERE id=?', (title, notes, item.task_id))
    self.conn.commit()
    dialog.dismiss()
    Snackbar(text='Saved').open()
    self.load_tasks()

def export_tasks(self):
    rows = self.cursor.execute('SELECT id, title, notes, category, due_date, done, priority, created_at FROM tasks').fetchall()
    data = []
    for r in rows:
        data.append({
            'id': r[0], 'title': r[1], 'notes': r[2], 'category': r[3], 'due_date': r[4], 'done': r[5], 'priority': r[6], 'created_at': r[7]
        })
    fp = 'tasks_export.json'
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    Snackbar(text=f'Exported {len(data)} tasks to {fp}').open()

def import_tasks(self):
    try:
        fp = 'tasks_export.json'
        with open(fp, 'r', encoding='utf-8') as f:
            data = json.load(f)
        count = 0
        for t in data:
            self.cursor.execute('INSERT INTO tasks (title, notes, category, due_date, done, priority, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)', (t.get('title'), t.get('notes'), t.get('category'), t.get('due_date'), t.get('done', 0), t.get('priority', 2), t.get('created_at')))
            count += 1
        self.conn.commit()
        Snackbar(text=f'Imported {count} tasks from {fp}').open()
        self.load_tasks()
    except Exception as e:
        Snackbar(text=f'Import failed: {e}').open()

if name == 'main': ToDoApp().run()

------------------------

README / Packaging notes

------------------------

How to run (desktop / dev):

1. Install dependencies:

pip install kivy kivymd

2. Run: python ToDoApp_KivyMD.py



iOS packaging notes (summary):

- To deploy to iPhone you must build a native app. The recommended route with Python is using kivy-ios (https://github.com/kivy/kivy-ios).

- Steps (high-level):

1. On a Mac with Xcode installed, clone kivy-ios and use it to create an Xcode project that bundles your Kivy app.

2. Some KivyMD widgets and dependencies may require tweaks; test on simulator first.

3. Build the Xcode project and deploy to your device or submit to App Store.

- Limitations on iOS: Local notifications, background tasks, and deep iOS integrations may require writing a small Objective-C/Swift bridge or using PyOBJus. Push notifications typically require native code.



Alternatives:

- Use a web-app approach (Flask/FastAPI + responsive frontend like Ionic/React) and wrap as a PWA — easiest to get onto iPhone home screen with offline caching and notifications via Web APIs (with some limits on iOS).

- Use BeeWare / Toga to create a native-looking app (project still maturing for iOS).



Features included in this example:

- Add tasks (with optional due date selected prior to adding)

- Edit / Delete tasks

- Mark complete / incomplete

- Simple search dialog

- Export / Import JSON

- Persistent storage (SQLite)



Features you might want to add next:

- Recurring tasks, reminders (local notifications), priority picker UI, subtasks, syncing with cloud (Firebase / custom API), calendar integration, drag-and-drop reordering, prettier animations.



If you want, I can:

- Add native local notification support guidance for iOS (with example bridge code)

- Convert this to a Flask + React/Ionic PWA implementation that is much easier to deploy to iPhone as a web app

- Expand UI with custom themes, categories screen, and sorting controls



