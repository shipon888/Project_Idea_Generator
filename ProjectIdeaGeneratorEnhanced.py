import json
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Load the project ideas from the JSON file
with open('cse_project_ideas.json', 'r') as file:
    project_ideas = json.load(file)

# Load the conversation log from the JSON file
with open('conversation_log.json', 'r') as file:
    conversation_log = json.load(file)

# Combine all project ideas into a single list
all_project_ideas = []
for category in project_ideas.values():
    all_project_ideas.extend(category["project_ideas"])

class ProjectIdeaGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Project Idea Generator")
        self.master.geometry("300x600")

        # GUI elements
        self.chat_window = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.chat_window.pack(pady=10, fill=tk.BOTH, expand=True)
        self.chat_window.config(state=tk.DISABLED)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10, fill=tk.X, padx=10)

        self.send_button = tk.Button(master, text="Send Message", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self):
        user_message = self.entry.get().strip()
        if user_message:
            self.display_message("User", user_message)
            self.entry.delete(0, tk.END)
            self.generate_idea(user_message)
    
    def display_message(self, sender, message):
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, f"{sender}: {message}\n")
        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.yview(tk.END)

    def generate_idea(self, user_message):
        # Check for project idea request
        if "project idea" in user_message.lower():
            import random
            idea = random.choice(all_project_ideas)
            self.display_message("PIG", f"Project Idea: {idea}")
        else:
            self.display_message("PIG", "Sorry, I can only provide project ideas. Please ask for a project idea.")

# Main application
root = tk.Tk()
app = ProjectIdeaGenerator(root)
root.mainloop()
