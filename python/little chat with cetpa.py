# CETPA Chat Program using only Dictionary

cetpa_chat = {
    "intro": "👋 Welcome to CETPA Infotech!\nWe provide training in various IT & software domains.",
    
    "courses": {
        "Python": {
            "Duration": "3 months (weekend & weekday batches available)",
            "Fees": "₹12,000",
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
    }
}


def start_chat():
    print(cetpa_chat["intro"])
    while True:
        user = input("\nYou: ").lower()
        
        if "course" in user or "available" in user:
            print("\n🤖 CETPA Bot: We offer the following courses:")
            for c in cetpa_chat["courses"]:
                print(f" - {c}")
            print("👉 Type a course name to know full details.")
        
        elif user.capitalize() in cetpa_chat["courses"]:
            course = cetpa_chat["courses"][user.capitalize()]
            print(f"\n📘 Course: {user.capitalize()}")
            print(f"⏳ Duration: {course['Duration']}")
            print(f"💰 Fees: {course['Fees']}")
            print(f"🎓 Mode: {course['Mode']}")
            print(f"📖 Details: {course['Details']}")
        
        elif "exit" in user or "quit" in user:
            print("\n🤖 CETPA Bot: Thank you! Visit again. 👋")
            break
        else:
            print("\n🤖 CETPA Bot: Sorry, I didn’t understand. Try asking about 'courses'.")


# ---------- Run Chat ----------
start_chat()