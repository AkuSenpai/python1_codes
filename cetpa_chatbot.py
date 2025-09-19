#!/usr/bin/env python3
"""
cetpa_chat.py

CETPA Infotech chatbot with OpenAI fallback.
Save your OpenAI API key in a .env file as:
    OPENAI_API_KEY=sk-...

Usage:
    pip install -r requirements.txt
    python cetpa_chat.py
"""

import os
import random
import sys
from dotenv import load_dotenv

# Attempt to import the modern OpenAI client; fall back to the older openai module usage if needed.
USE_MODERN_CLIENT = False
client = None
openai_module = None

try:
    # Modern client (preferred)
    from openai import OpenAI
    USE_MODERN_CLIENT = True
except Exception:
    # We'll try to import the legacy openai library (still commonly used)
    try:
        import openai as openai_module
    except Exception:
        openai_module = None

# Load .env (if present)
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")  # read from environment

# If API key not found, prompt the user to paste it (safer than hardcoding)
if not API_KEY:
    print("⚠️  OPENAI_API_KEY not found in environment.")
    key_input = input("Paste your OpenAI API key here (or press Enter to continue without API): ").strip()
    if key_input:
        API_KEY = key_input
        # Optionally export to environment for this run
        os.environ["OPENAI_API_KEY"] = API_KEY

# Initialize client according to available library
if API_KEY:
    if USE_MODERN_CLIENT:
        try:
            client = OpenAI(api_key=API_KEY)
        except Exception as e:
            print(f"❗ Failed to initialize modern OpenAI client: {e}")
            client = None
    else:
        if openai_module:
            try:
                openai_module.api_key = API_KEY
            except Exception as e:
                print(f"❗ Failed to set api_key on legacy openai module: {e}")
        else:
            print("❗ No OpenAI library found. Install 'openai' or upgrade it.")
else:
    print("ℹ️  Running without OpenAI API access. ChatGPT fallback will be disabled.")

# ----------------------------
# Your CETPA data dictionary
# ----------------------------
cetpa_chat = {
    "intro": "👋 Welcome to CETPA Infotech!\nWe provide training in various IT & software domains.",
    "courses": {
        "Python": {
            "Duration": "3 months (weekend & weekday batches available)",
            "Fees": "₹12,000",
            "Mode": "Online / Offline",
            "Details": "Python programming from basics to advanced, covering OOP, data structures, web development (Flask/Django), and project work."
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

# ----------------------------
# ChatGPT / OpenAI fallback
# ----------------------------
def ask_chatgpt(prompt: str, model: str = "gpt-3.5-turbo"):
    """
    Sends prompt to OpenAI and returns string reply.
    Supports both modern client (OpenAI) and legacy openai module.
    If API not configured, returns an informative message.
    """
    if not API_KEY:
        return "⚠️ ChatGPT fallback unavailable: OPENAI_API_KEY is not set."

    system_msg = (
        "You are a helpful assistant for CETPA Infotech. "
        "Answer user queries based on the following data:\n"
        f"{cetpa_chat}"
    )

    # Modern client usage: client.chat.completions.create(...)
    if client:
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=512
            )
            # New SDK usually returns: resp.choices[0].message.content
            # Some versions return resp.choices[0].message["content"] - handle both
            content = None
            try:
                content = resp.choices[0].message.content
            except Exception:
                try:
                    content = resp.choices[0].message["content"]
                except Exception:
                    content = str(resp)
            return content.strip() if isinstance(content, str) else str(content)
        except Exception as e:
            return f"⚠️ ChatGPT Error (modern client): {e}"

    # Legacy openai module usage
    if openai_module:
        try:
            response = openai_module.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=512
            )
            # response.choices[0].message["content"] or .choices[0].text depending on version
            try:
                return response.choices[0].message["content"].strip()
            except Exception:
                try:
                    return response.choices[0].text.strip()
                except Exception:
                    return str(response)
        except Exception as e:
            return f"⚠️ ChatGPT Error (legacy client): {e}"

    return "⚠️ ChatGPT fallback unavailable: no client/library initialized."

# ----------------------------
# Chat logic
# ----------------------------
def handle_user_input(user_input: str):
    text = user_input.strip().lower()

    # Greetings
    if any(greet in text for greet in cetpa_chat["greetings"]):
        return random.choice([
            "🤖 CETPA Bot: Hello! How can I help you today?",
            "🤖 CETPA Bot: Hi there! Ask me about our courses or FAQs.",
            "🤖 CETPA Bot: Welcome! Type 'courses' to see what we offer."
        ])

    # Farewell
    if any(fare in text for fare in cetpa_chat["farewell"]):
        return random.choice([
            "🤖 CETPA Bot: Goodbye! Have a great day! 👋",
            "🤖 CETPA Bot: Thanks for chatting. See you soon!",
            "🤖 CETPA Bot: Take care!"
        ])

    # FAQ
    if "timing" in text or "open" in text or "timings" in text:
        return f"🤖 CETPA Bot: {cetpa_chat['faq']['timings']}"
    if "location" in text or "where" in text:
        return f"🤖 CETPA Bot: {cetpa_chat['faq']['location']}"
    if "contact" in text or "phone" in text or "email" in text:
        return f"🤖 CETPA Bot: {cetpa_chat['faq']['contact']}"

    # List all courses
    if "all details" in text or "all courses" in text:
        lines = ["\n🤖 CETPA Bot: Here are all course details:"]
        for cname, course in cetpa_chat["courses"].items():
            lines.append(f"\n📘 {cname}")
            lines.append(f"⏳ Duration: {course['Duration']}")
            lines.append(f"💰 Fees: {course['Fees']}")
            lines.append(f"🎓 Mode: {course['Mode']}")
            lines.append(f"📖 Details: {course['Details']}")
        return "\n".join(lines)

    # List course names
    if "course" in text or "available" in text:
        course_names = "\n".join([f" - {c}" for c in cetpa_chat["courses"]])
        return f"\n🤖 CETPA Bot: We offer the following courses:\n{course_names}\n👉 Type a course name to know full details or 'all details' for everything."

    # Course details
    for cname in cetpa_chat["courses"]:
        if cname.lower() in text:
            course = cetpa_chat["courses"][cname]
            return (
                f"\n📘 Course: {cname}\n"
                f"⏳ Duration: {course['Duration']}\n"
                f"💰 Fees: {course['Fees']}\n"
                f"🎓 Mode: {course['Mode']}\n"
                f"📖 Details: {course['Details']}"
            )

    # If not handled, use ChatGPT fallback (if available)
    if API_KEY:
        return ask_chatgpt(user_input)
    else:
        return "🤖 CETPA Bot: Sorry, I don't know that. (Enable OpenAI API to get a smarter fallback.)"

# ----------------------------
# Chat runner
# ----------------------------
CHAT_HISTORY_FILE = "chat_history.txt"

def save_chat(user_text: str, bot_reply: str):
    try:
        with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write("USER: " + user_text + "\n")
            f.write("BOT:  " + bot_reply + "\n")
            f.write("-" * 40 + "\n")
    except Exception:
        pass  # non-fatal if logging fails

def start_chat():
    print(cetpa_chat["intro"])
    while True:
        try:
            user = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Exiting CETPA Chat. Goodbye!")
            break

        if not user:
            continue

        reply = handle_user_input(user)
        print(f"\n{reply}")

        save_chat(user, reply)

        # If the reply was a farewell variant, exit
        if any(fare in user.lower() for fare in cetpa_chat["farewell"]):
            break

# ----------------------------
# Main entry
# ----------------------------
if __name__ == "__main__":
    # Simple arg: --no-openai to force disabling API even if key present
    if "--no-openai" in sys.argv:
        API_KEY = None
        client = None
        openai_module = None
        print("ℹ️  OpenAI API disabled by --no-openai")

    start_chat()