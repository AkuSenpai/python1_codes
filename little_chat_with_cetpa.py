import random

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
    },
    "faq": {
        "timings": "We are open from 9am to 7pm, Monday to Saturday.",
        "location": "CETPA Infotech, Noida, India.",
        "contact": "You can call us at +91-120-4535353 or email info@cetpainfotech.com."
    },
    "greetings": ["hello", "hi", "hey", "namaste", "greetings"],
    "farewell": ["bye", "goodbye", "see you", "thanks", "thank you"]
}


def start_chat():
    print(cetpa_chat["intro"])
    while True:
        user = input("\nYou: ").strip().lower()

        # Greetings
        if any(greet in user for greet in cetpa_chat["greetings"]):
            print(random.choice([
                "🤖 CETPA Bot: Hello! How can I help you today?",
                "🤖 CETPA Bot: Hi there! Ask me about our courses or FAQs.",
                "🤖 CETPA Bot: Welcome! Type 'courses' to see what we offer."
            ]))
            continue

        # Farewell
        if any(fare in user for fare in cetpa_chat["farewell"]):
            print(random.choice([
                "🤖 CETPA Bot: Goodbye! Have a great day! 👋",
                "🤖 CETPA Bot: Thanks for chatting. See you soon!",
                "🤖 CETPA Bot: Take care!"
            ]))
            break

        # FAQ
        if "timing" in user or "open" in user:
            print(f"🤖 CETPA Bot: {cetpa_chat['faq']['timings']}")
            continue
        if "location" in user or "where" in user:
            print(f"🤖 CETPA Bot: {cetpa_chat['faq']['location']}")
            continue
        if "contact" in user or "phone" in user or "email" in user:
            print(f"🤖 CETPA Bot: {cetpa_chat['faq']['contact']}")
            continue

        # List all courses
        if "all details" in user or "all courses" in user:
            print("\n🤖 CETPA Bot: Here are all course details:")
            for cname, course in cetpa_chat["courses"].items():
                print(f"\n📘 {cname}")
                print(f"⏳ Duration: {course['Duration']}")
                print(f"💰 Fees: {course['Fees']}")
                print(f"🎓 Mode: {course['Mode']}")
                print(f"📖 Details: {course['Details']}")
            continue

        # List course names
        if "course" in user or "available" in user:
            print("\n🤖 CETPA Bot: We offer the following courses:")
            for c in cetpa_chat["courses"]:
                print(f" - {c}")
            print("👉 Type a course name to know full details or 'all details' for everything.")
            continue

        # Course details
        found = False
        for cname in cetpa_chat["courses"]:
            if cname.lower() in user:
                course = cetpa_chat["courses"][cname]
                print(f"\n📘 Course: {cname}")
                print(f"⏳ Duration: {course['Duration']}")
                print(f"💰 Fees: {course['Fees']}")
                print(f"🎓 Mode: {course['Mode']}")
                print(f"📖 Details: {course['Details']}")
                found = True
                break

        if not found:
            # Unknown input
            print(random.choice([
                "🤖 CETPA Bot: Sorry, I didn’t understand. Try asking about 'courses', 'timings', or 'location'.",
                "🤖 CETPA Bot: Hmm, I couldn't get that. Type 'courses' or a course name for info.",
                "🤖 CETPA Bot: Please ask about our courses, timings, location, or contact info."
            ]))


# ---------- Run Chat ----------
if __name__ == "__main__":
    while True:
        start_chat()
        again = input("\nDo you want to restart the chat? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Exiting CETPA Chat. Have a nice day!")
            break
