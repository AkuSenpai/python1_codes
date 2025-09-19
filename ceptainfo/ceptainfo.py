import random
import tkinter as tk
from tkinter import scrolledtext

# CETPA Chat Program using only Dictionary
cetpa_chat = {
    "intro": "👋 Welcome to CETPA Infotech!\nWe provide training in various IT & software domains.",

    "courses": {
        "Python": {
            "Duration": "3 months (weekend & weekday batches available)",
            "Fees": "₹1200/Month",
            "Mode": "Online / Offline",
            "Details": "Python programming from basics to advanced, covering OOP, data structures, "
                        "web development (Flask/Django), and project work."
        },
        "Java": {
            "Duration": "4 months",
            "Fees": "₹15,000",
            "Mode": "Offline / Online",
            "Details": "Core + Advanced Java, JDBC, JSP, Servlets, and Mini Project."
        },
        "Data Science": {
            "Duration": "6 months",
            "Fees": "₹25,000",
            "Mode": "Online / Offline",
            "Details": "Python, Statistics, Machine Learning, Deep Learning, and hands-on projects."
        },
        "Web Development": {
            "Duration": "5 months",
            "Fees": "₹20,000",
            "Mode": "Online / Offline",
            "Details": "HTML, CSS, JavaScript, React, Node.js, PHP, and Full Stack Projects."
        }
    },
    "faq": {
        "timings": "We are open from 9am to 7pm, Monday to Saturday.",
        "location": "CETPA Infotech, Noida, India.",
        "contact": "You can call us at +91-120-4535353 or email info@cetpainfotech.com."
    },
    "greetings": ["hello", "hi", "hey", "namaste", "greetings"],
    "farewell": ["bye", "goodbye", "see you", "thanks", "thank you", "exit"]
}

def get_bot_response(user_input):
    """Generates the bot's response based on user input."""
    user = user_input.strip().lower()

    if user == "exit":
        return "🤖 CETPA Bot: Goodbye! Have a great day! 👋"

    if any(greet in user for greet in cetpa_chat["greetings"]):
        return random.choice([
            "🤖 CETPA Bot: Hello! How can I help you today?",
            "🤖 CETPA Bot: Hi there! Ask me about our courses.",
            "🤖 CETPA Bot: Welcome! Type 'courses' to see what we offer."
        ])

    if any(fare in user for fare in cetpa_chat["farewell"]):
        return random.choice([
            "🤖 CETPA Bot: Goodbye! Have a great day! 👋",
            "🤖 CETPA Bot: Thanks for chatting. See you soon!",
            "🤖 CETPA Bot: Take care!"
        ])

    if "timing" in user or "open" in user:
        return f"🤖 CETPA Bot: {cetpa_chat['faq']['timings']}"
    
    if "location" in user or "where" in user:
        return f"🤖 CETPA Bot: {cetpa_chat['faq']['location']}"
    
    if "contact" in user or "phone" in user or "email" in user:
        return f"🤖 CETPA Bot: {cetpa_chat['faq']['contact']}"

    if "all details" in user or "all courses" in user:
        response = "\n🤖 CETPA Bot: Here are all course details:\n"
        for cname, course in cetpa_chat["courses"].items():
            response += f"\n📘 {cname}\n"
            response += f"⏳ Duration: {course['Duration']}\n"
            response += f"💰 Fees: {course['Fees']}\n"
            response += f"🎓 Mode: {course['Mode']}\n"
            response += f"📖 Details: {course['Details']}\n"
        return response

    if "course" in user or "available" in user:
        response = "\n🤖 CETPA Bot: We offer the following courses:\n"
        for c in cetpa_chat["courses"]:
            response += f" - {c}\n"
        response += "👉 Type a course name to know full details or 'all details' for everything."
        return response

    for cname in cetpa_chat["courses"]:
        if cname.lower() in user:
            course = cetpa_chat["courses"][cname]
            response = f"\n📘 Course: {cname}\n"
            response += f"⏳ Duration: {course['Duration']}\n"
            response += f"💰 Fees: {course['Fees']}\n"
            response += f"🎓 Mode: {course['Mode']}\n"
            response += f"📖 Details: {course['Details']}"
            return response

    return random.choice([
        "🤖 CETPA Bot: Sorry, I didn’t understand. Try asking about 'courses', 'timings', or 'location'.",
        "🤖 CETPA Bot: Hmm, I couldn't get that. Type 'courses' or a course name for info.",
        "🤖 CETPA Bot: Please ask about our courses, timings, location, or contact info."
    ])


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("CETPA Chatbot")
        master.geometry("500x500")

        self.chat_display = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

        self.user_input = tk.Entry(self.input_frame)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=(5, 0))

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.bind("<Escape>", self.on_escape)

        self.add_message("🤖 CETPA Bot: " + cetpa_chat["intro"])

    def add_message(self, message):
        """Adds a message to the chat display."""
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

    def send_message(self, event=None):
        """Handles sending a message and getting a bot response."""
        user_message = self.user_input.get()
        if not user_message:
            return

        self.add_message("You: " + user_message)
        self.user_input.delete(0, tk.END)

        bot_response = get_bot_response(user_message)
        self.add_message(bot_response)

        if "Goodbye" in bot_response:
            self.master.after(2000, self.master.destroy)

    def on_closing(self):
        """Handles the window closing event."""
        self.master.destroy()

    def on_escape(self, event):
        """Allows for closing with the Escape key."""
        self.master.destroy()

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
