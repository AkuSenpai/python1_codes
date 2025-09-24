import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser, font, simpledialog, ttk
import json
import os
import webbrowser
import urllib.parse
import re
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

--- Global Variables and Configuration ---
SETTINGS_FILE = "settings.json"
AUTOSAVE_FILE = "autosave.json"
current_file_path = None
base_font_size = 10
current_language = "en" # Default language is English
recent_files = []
fields = []
tooltip_delay = 500 # Milliseconds

--- Color Palette and Styling ---
THEME = {
"window_bg": "#2e2e2e",
"main_bg": "#3e3e3e",
"text_color": "#e0e0e0",
"entry_bg": "#505050",
"entry_border": "#606060",
"button_bg": "#4a4a4a",
"button_fg": "#e0e0e0",
"accent_color": "#2196f3",
"accent_text": "#ffffff",
"font_family": "Segoe UI",
"font_size": 10
}

--- Language Dictionaries ---
LANGUAGES = {
"en": {
"Project Details Form": "Project Details Form",
"Name": "Name",
"Father name": "Father name",
"Mother name": "Mother name",
"MOB": "Mobile Number",
"Email id": "Email ID",
"Type of project": "Type of Project",
"Cost of project": "Cost of Project",
"Social Category": "Social Category",
"Type of Land": "Type of Land",
"Total Area": "Total Area",
"Project location Type": "Project Location Type",
"If Shed & Shed Area": "If Shed & Shed Area",
"Resit Address": "Resident Address",
"PIN": "PIN",
"Project location": "Project Location",
"Project location PIN": "Project Location PIN",
"Mulnivas": "Mulnivas",
"If animal purchase number of animal": "If Animal Purchase (Number of Animals)",
"Firm Name": "Firm Name",
"Purpose bank": "Purpose Bank",
"IFC Code": "IFC Code",
"CIBIL Condition": "CIBIL Condition",
"Project Schemes and Subsidy": "Project Schemes and Subsidy",
"Save to File": "Save to File",
"Share on WhatsApp": "Share on WhatsApp",
"Export to PDF": "Export to PDF",
"File": "File",
"Save": "Save",
"Save As...": "Save As...",
"Open...": "Open...",
"Clear Form": "Clear Form",
"Theme": "Theme",
"Font Color": "Font Color",
"Entry Background": "Entry Background",
"Label Background": "Label Background",
"Window Background": "Window Background",
"Dark Theme": "Dark Theme",
"Light Theme": "Light Theme",
"High Contrast": "High Contrast",
"Zoom": "Zoom",
"Zoom In": "Zoom In",
"Zoom Out": "Zoom Out",
"Font Style": "Font Style",
"WhatsApp Number": "WhatsApp Number",
"Enter mobile number with country code (e.g. 919999999999):": "Enter mobile number with country code (e.g. 919999999999):",
"Empty": "Empty",
"Please fill out the form before sharing.": "Please fill out the form before sharing.",
"Saved": "Saved",
"Data saved to:": "Data saved to:",
"Success": "Success",
"PDF saved to:": "PDF saved to:",
"Error": "Error",
"N/A": "N/A",
"Language": "Language",
"Validation Error": "Validation Error",
"Please fill in all required fields.": "Please fill in all required fields.",
"Recent Files": "Recent Files",
"Manage Fields": "Manage Fields",
"Add Field": "Add Field",
"Remove Selected Field": "Remove Selected Field",
"Field Name:": "Field Name:",
"Please select a field to remove.": "Please select a field to remove.",
"Confirmation": "Confirmation",
"Are you sure you want to clear the form? All unsaved data will be lost.": "Are you sure you want to clear the form? All unsaved data will be lost.",
"Autosave detected!": "Autosave detected!",
"Do you want to restore the unsaved data?": "Do you want to restore the unsaved data?",
"Searching...": "Searching...",
"Print": "Print",
"PDF created, now open in a separate window or print from there.": "PDF created, now open in a separate window or print from there.",
"Please enter a field name.": "Please enter a field name.",
"Search for a field:": "Search for a field:",
"Search Bar Background": "Search Bar Background"
},
"hi": {
"Project Details Form": "परियोजना विवरण प्रपत्र",
"Name": "नाम",
"Father name": "पिता का नाम",
"Mother name": "माता का नाम",
"MOB": "मोबाइल नंबर",
"Email id": "ईमेल आईडी",
"Type of project": "परियोजना का प्रकार",
"Cost of project": "परियोजना की लागत",
"Social Category": "सामाजिक श्रेणी",
"Type of Land": "भूमि का प्रकार",
"Total Area": "कुल क्षेत्रफल",
"Project location Type": "परियोजना स्थान का प्रकार",
"If Shed & Shed Area": "यदि शेड और शेड क्षेत्र",
"Resit Address": "निवासी का पता",
"PIN": "पिन",
"Project location": "परियोजना का स्थान",
"Project location PIN": "परियोजना स्थान पिन",
"Mulnivas": "मूलनिवास",
"If animal purchase number of animal": "यदि पशु खरीद (पशुओं की संख्या)",
"Firm Name": "फर्म का नाम",
"Purpose bank": "उद्देश्य बैंक",
"IFC Code": "आईएफसी कोड",
"CIBIL Condition": "सिबिल स्थिति",
"Project Schemes and Subsidy": "परियोजना योजनाएं और सब्सिडी",
"Save to File": "फ़ाइल में सहेजें",
"Share on WhatsApp": "व्हाट्सएप पर शेयर करें",
"Export to PDF": "पीडीएफ में निर्यात करें",
"File": "फ़ाइल",
"Save": "सहेजें",
"Save As...": "इस रूप में सहेजें...",
"Open...": "खोलें...",
"Clear Form": "फॉर्म साफ़ करें",
"Theme": "थीम",
"Font Color": "फ़ॉन्ट रंग",
"Entry Background": "एंट्री पृष्ठभूमि",
"Label Background": "लेबल पृष्ठभूमि",
"Window Background": "विंडो पृष्ठभूमि",
"Dark Theme": "डार्क थीम",
"Light Theme": "लाइट थीम",
"High Contrast": "उच्च कंट्रास्ट",
"Zoom": "ज़ूम",
"Zoom In": "ज़ूम इन",
"Zoom Out": "ज़ूम आउट",
"Font Style": "फ़ॉन्ट शैली",
"WhatsApp Number": "व्हाट्सएप नंबर",
"Enter mobile number with country code (e.g. 919999999999):": "देश कोड के साथ मोबाइल नंबर दर्ज करें (उदाहरण: 919999999999):",
"Empty": "खाली",
"Please fill out the form before sharing.": "कृपया साझा करने से पहले फ़ॉर्म भरें।",
"Saved": "सहेजा गया",
"Data saved to:": "डेटा इसमें सहेजा गया:",
"Success": "सफलता",
"PDF saved to:": "पीडीएफ इसमें सहेजा गया:",
"Error": "त्रुटि",
"N/A": "उपलब्ध नहीं",
"Language": "भाषा",
"Validation Error": "सत्यापन त्रुटि",
"Please fill in all required fields.": "कृपया सभी आवश्यक फ़ील्ड भरें।",
"Recent Files": "हाल की फ़ाइलें",
"Manage Fields": "फ़ील्ड प्रबंधित करें",
"Add Field": "फ़ील्ड जोड़ें",
"Remove Selected Field": "चयनित फ़ील्ड हटाएँ",
"Field Name:": "फ़ील्ड का नाम:",
"Please select a field to remove.": "कृपया हटाने के लिए एक फ़ील्ड चुनें।",
"Confirmation": "पुष्टि",
"Are you sure you want to clear the form? All unsaved data will be lost.": "क्या आप वाकई फ़ॉर्म साफ़ करना चाहते हैं? सभी असहेजा डेटा खो जाएगा।",
"Autosave detected!": "ऑटोसेव का पता चला!",
"Do you want to restore the unsaved data?": "क्या आप असहेजा डेटा को पुनर्स्थापित करना चाहते हैं?",
"Searching...": "खोज रहा है...",
"Print": "प्रिंट",
"PDF created, now open in a separate window or print from there.": "पीडीएफ बनाया गया, अब एक अलग विंडो में खोलें या वहां से प्रिंट करें।",
"Please enter a field name.": "कृपया एक फ़ील्ड का नाम दर्ज करें।",
"Search for a field:": "किसी फ़ील्ड को खोजें:",
"Search Bar Background": "खोज बार पृष्ठभूमि"
}
}

Helper function to get translated text
def _(text):
"""Translates the given text based on the current language."""
return LANGUAGES[current_language].get(text, text)

Default theme dictionary
theme = {
"font_color": THEME["text_color"],
"entry_bg": THEME["entry_bg"],
"label_bg": THEME["main_bg"],
"window_bg": THEME["window_bg"],
"search_bg": THEME["entry_bg"],
"font_size": base_font_size,
"font_family": THEME["font_family"],
"fields": [
"Name", "Father name", "Mother name", "MOB", "Email id",
"Type of project", "Cost of project", "Social Category", "Type of Land",
"Total Area", "Project location Type", "If Shed & Shed Area",
"Resit Address", "PIN", "Project location", "Project location PIN",
"Mulnivas", "If animal purchase number of animal",
"Firm Name", "Purpose bank", "IFC Code",
"CIBIL Condition"
],
"recent_files": []
}

--- Tooltip Class ---
class Tooltip:
"""A simple tooltip class to provide help text on hover."""
def init(self, widget, text):
self.widget = widget
self.text = text
self.tooltip_window = None
self.id = None
self.widget.bind("", self.schedule)
self.widget.bind("", self.hide)

def schedule(self, event=None):
    self.unschedule()
    self.id = self.widget.after(tooltip_delay, self.show)

def unschedule(self):
    if self.id:
        self.widget.after_cancel(self.id)
        self.id = None

def show(self):
    x = self.widget.winfo_rootx() + 20
    y = self.widget.winfo_rooty() + 20
    self.tooltip_window = tk.Toplevel(self.widget)
    self.tooltip_window.wm_overrideredirect(True)
    self.tooltip_window.wm_geometry(f"+{x}+{y}")
    label = tk.Label(self.tooltip_window, text=self.text, background="#ffffe0", relief="solid", borderwidth=1, font=("TkDefaultFont", 8))
    label.pack(ipadx=1)

def hide(self, event=None):
    self.unschedule()
    if self.tooltip_window:
        self.tooltip_window.destroy()
    self.tooltip_window = None
--- Theme and Settings Functions ---
def load_settings():
"""Loads theme, fields, and recent files from a JSON file."""
global base_font_size, recent_files, fields, current_language
if os.path.exists(SETTINGS_FILE):
try:
with open(SETTINGS_FILE, "r") as f:
saved = json.load(f)
theme.update(saved)

            if 'fields' in saved:
                fields.clear()
                fields.extend(saved['fields'])
            if 'recent_files' in saved:
                recent_files.clear()
                recent_files.extend(saved['recent_files'])
            if 'current_language' in saved:
                current_language = saved['current_language']
    except (IOError, json.JSONDecodeError):
        print("Settings file not found or corrupt, using defaults.")

base_font_size = theme.get("font_size", 10)
if not fields:
    fields.extend(theme["fields"])
def save_settings():
"""Saves current theme, fields, and recent files to a JSON file."""
theme["font_size"] = base_font_size
theme["fields"] = fields
theme["recent_files"] = recent_files
theme["current_language"] = current_language

with open(SETTINGS_FILE, "w") as f:
    json.dump(theme, f, indent=4)
def update_recent_files(file_path):
"""Adds a file path to the recent files list and saves it."""
if file_path in recent_files:
recent_files.remove(file_path)
recent_files.insert(0, file_path)
if len(recent_files) > 10:
recent_files.pop()
save_settings()
create_menu_bar()

load_settings()

--- Main Application Setup ---
root = tk.Tk()
root.title(_("Project Details Form"))
root.geometry("800x700")
root.configure(bg=THEME["window_bg"])

Configure ttk style
style = ttk.Style()
style.theme_use("clam") # 'clam', 'alt', 'default', 'classic'

def apply_ttk_style():
"""Configures the ttk styles for all widgets."""
style.configure("TFrame", background=THEME["main_bg"])
style.configure("TLabel", background=THEME["main_bg"], foreground=THEME["text_color"], font=(THEME["font_family"], THEME["font_size"]))
style.configure("TButton", background=THEME["button_bg"], foreground=THEME["button_fg"], font=(THEME["font_family"], THEME["font_size"]))
style.map("TButton", background=[("active", "#606060")])
style.configure("Accent.TButton", background=THEME["accent_color"], foreground=THEME["accent_text"], font=(THEME["font_family"], THEME["font_size"]))
style.map("Accent.TButton", background=[("active", "#31aaff")])
style.configure("TEntry", fieldbackground=THEME["entry_bg"], foreground=THEME["text_color"], bordercolor=THEME["entry_border"], font=(THEME["font_family"], THEME["font_size"]))
style.configure("TText", background=THEME["entry_bg"], foreground=THEME["text_color"], font=(THEME["font_family"], THEME["font_size"]))
style.configure("TNotebook", background=THEME["window_bg"], borderwidth=0)
style.configure("TNotebook.Tab", background=THEME["main_bg"], foreground=THEME["text_color"])
style.map("TNotebook.Tab", background=[("selected", THEME["accent_color"])])
style.configure("TLabelframe", background=THEME["main_bg"], foreground=THEME["text_color"])
style.configure("TLabelframe.Label", background=THEME["main_bg"], foreground=THEME["text_color"])
style.configure("TListbox", background=THEME["entry_bg"], foreground=THEME["text_color"], borderwidth=0)

apply_ttk_style()

Search bar frame
search_frame = ttk.Frame(root, style="TFrame")
search_frame.pack(fill=tk.X, padx=20, pady=(20, 10))

search_label = ttk.Label(search_frame, text=_("Search for a field:") + " ", style="TLabel")
search_label.pack(side=tk.LEFT, padx=(0, 5))
search_var = tk.StringVar()
search_entry = ttk.Entry(search_frame, textvariable=search_var)
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
search_var.trace("w", lambda name, index, mode: search_form())

Main frame to hold the canvas and scrollbar
main_frame = ttk.Frame(root, style="TFrame")
main_frame.pack(fill=tk.BOTH, expand=1, padx=20, pady=(0, 20))

Canvas for scrollable content
canvas = tk.Canvas(main_frame, bg=THEME["main_bg"], highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

Scrollbar for the canvas
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

Frame to hold all form widgets
form_frame = ttk.Frame(canvas, style="TFrame")
canvas.create_window((0, 0), window=form_frame, anchor="nw")

Configure scrolling and resizing
def on_frame_configure(event):
"""Update scroll region when the form frame size changes."""
canvas.configure(scrollregion=canvas.bbox("all"))
form_frame.bind('', on_frame_configure)
form_frame.grid_columnconfigure(1, weight=1)

--- Form Fields and Widgets ---
entries = {}
labels = {}

Function to create or update all form widgets
def create_form_widgets():
global entries, labels, scheme_label, scheme_text

for widget in form_frame.winfo_children():
    widget.destroy()

entries = {}
labels = {}

for idx, field in enumerate(fields):
    label = ttk.Label(form_frame, text=_("{}".format(field)) + ":", anchor="w", style="TLabel")
    label.grid(row=idx, column=0, padx=15, pady=8, sticky="w")

    entry = ttk.Entry(form_frame, style="TEntry")
    entry.grid(row=idx, column=1, padx=15, pady=8, sticky="ew")

    entries[field] = entry
    labels[field] = label
    
    Tooltip(label, _("Enter the {}".format(field.lower())))

scheme_label = ttk.Label(form_frame, text=_("Project Schemes and Subsidy") + ":", anchor="nw", style="TLabel")
scheme_label.grid(row=len(fields), column=0, padx=15, pady=(20, 5), sticky="nw")
Tooltip(scheme_label, _("Enter details about project schemes and subsidies."))

scheme_text = tk.Text(form_frame, height=10, bg=THEME["entry_bg"], fg=THEME["text_color"], relief="flat", borderwidth=0, font=(THEME["font_family"], THEME["font_size"]))
scheme_text.grid(row=len(fields), column=1, padx=15, pady=5, sticky="ew")

button_frame = ttk.Frame(form_frame, style="TFrame")
button_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=(20, 10))

save_btn = ttk.Button(button_frame, text=_("Save to File"), command=save_to_file, style="Accent.TButton")
save_btn.pack(side=tk.LEFT, padx=10)

share_btn = ttk.Button(button_frame, text=_("Share on WhatsApp"), command=share_on_whatsapp, style="Accent.TButton")
share_btn.pack(side=tk.LEFT, padx=10)

pdf_btn = ttk.Button(button_frame, text=_("Export to PDF"), command=export_to_pdf, style="Accent.TButton")
pdf_btn.pack(side=tk.LEFT, padx=10)
def search_form():
"""Filters the form fields based on the search query."""
query = search_var.get().lower().strip()
for field in fields:
label = labels.get(field)
entry = entries.get(field)

    if query in field.lower() or query in _(field).lower():
        if label: label.grid()
        if entry: entry.grid()
    else:
        if label: label.grid_remove()
        if entry: entry.grid_remove()

scheme_label.grid()
scheme_text.grid()
button_frame = form_frame.grid_slaves(row=len(fields)+1, column=0)[0]
button_frame.grid()
on_frame_configure(None)
--- Form Data Management and Validation ---
def get_form_data_as_dict():
"""Collects all data from the form and formats it as a dictionary."""
data = {field: entries[field].get() for field in fields if field in entries}
data["Project Schemes and Subsidy"] = scheme_text.get("1.0", tk.END).strip()
return data

def get_form_data_as_string():
"""Collects all data from the form and formats it as a string for sharing."""
data_lines = [f"{(field)}:- {entries[field].get()}" for field in fields if field in entries]
schemes = scheme_text.get("1.0", tk.END).strip()
data_lines.append(f"\n{('Project Schemes and Subsidy')}:")
data_lines.append(schemes if schemes else _("N/A"))
return "\n".join(data_lines)

def validate_form():
"""Validates key form fields to ensure they are not empty and have correct types."""
if not entries["Name"].get().strip():
messagebox.showerror(_("Validation Error"), _("Please fill in all required fields."))
return False

email = entries.get("Email id", tk.StringVar()).get()
if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    messagebox.showerror(_("Validation Error"), _("Invalid Email ID format."))
    return False

mob = entries.get("MOB", tk.StringVar()).get()
if mob and not mob.isdigit():
    messagebox.showerror(_("Validation Error"), _("Mobile Number must contain only digits."))
    return False

cost = entries.get("Cost of project", tk.StringVar()).get()
if cost and not (cost.isdigit() or re.match(r"^\d+\.\d+$", cost)):
    messagebox.showerror(_("Validation Error"), _("Cost of Project must be a number."))
    return False

return True
def clear_form():
"""Clears all form fields and resets the form."""
if messagebox.askyesno(_("Confirmation"), _("Are you sure you want to clear the form? All unsaved data will be lost.")):
for entry in entries.values():
entry.delete(0, tk.END)
scheme_text.delete("1.0", tk.END)

--- File Operations ---
def save_to_file():
"""Saves the form data to the current file path, or prompts for a new one."""
global current_file_path
if not validate_form():
return

if current_file_path:
    try:
        with open(current_file_path, "w") as file:
            json.dump(get_form_data_as_dict(), file, indent=4)
        messagebox.showinfo(_("Saved"), f"{_('Data saved to:')}\n{current_file_path}")
        update_recent_files(current_file_path)
    except Exception as e:
        messagebox.showerror(_("Error"), str(e))
else:
    save_as()
def save_as():
"""Prompts the user to save the form data to a new file."""
global current_file_path
if not validate_form():
return

file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")], title=_("Save As..."))
if file_path:
    current_file_path = file_path
    save_to_file()
def open_file(file_path=None):
"""Prompts the user to open an existing file and loads the data."""
global current_file_path

if not file_path:
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")], title=_("Open..."))

if not file_path:
    return

try:
    with open(file_path, "r") as file:
        data = json.load(file)
        for entry in entries.values():
            entry.delete(0, tk.END)
        scheme_text.delete("1.0", tk.END)
        
        for field, value in data.items():
            if field in entries:
                entries[field].insert(0, value)
            elif field == "Project Schemes and Subsidy":
                scheme_text.insert("1.0", value)
        current_file_path = file_path
        update_recent_files(current_file_path)
except (IOError, json.JSONDecodeError, KeyError) as e:
    messagebox.showerror(_("Error"), f"Could not load file: {str(e)}")
def share_on_whatsapp():
"""Generates a simple WhatsApp message link with form data."""
if not validate_form():
return

data = get_form_data_as_string()
encoded_text = urllib.parse.quote(data)
url = f"https://wa.me/?text={encoded_text}"
webbrowser.open(url)
def export_to_pdf():
"""Exports the form data to a PDF file with a progress bar."""
file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title=_("Export to PDF"))
if not file_path:
return

