import tkinter as tk
from tkinter import messagebox
import json
from logic.rules import recommend_career
from report_generator import generate_report

with open('utils/questions.json') as f:
    questions = json.load(f)

with open('data/careers.json') as f:
    career_data = json.load(f)

class CareerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Career Counselling System")
        self.responses = []
        self.current = 0
        self.name_var = tk.StringVar()
        self.build_intro()

    def build_intro(self):
        tk.Label(self.root, text="Enter your name:").pack()
        tk.Entry(self.root, textvariable=self.name_var).pack()
        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack()

    def start_quiz(self):
        self.name = self.name_var.get().strip()
        if not self.name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        for widget in self.root.winfo_children():
            widget.destroy()
        self.show_question()

    def show_question(self):
        if self.current >= len(questions):
            self.finish()
            return

        q = questions[self.current]
        self.var = tk.IntVar()
        tk.Label(self.root, text=q["question"]).pack()
        tk.Button(self.root, text="Yes", command=lambda: self.record_answer(q["category"])).pack()
        tk.Button(self.root, text="No", command=self.skip_question).pack()

    def record_answer(self, category):
        self.responses.append({"category": category})
        self.current += 1
        self.clear_screen()
        self.show_question()

    def skip_question(self):
        self.current += 1
        self.clear_screen()
        self.show_question()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def finish(self):
        career = recommend_career(self.responses)
        details = career_data[career]
        report_file = generate_report(self.name, career, details)
        messagebox.showinfo("Recommendation", f"Recommended Career: {career}\nReport saved as {report_file}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = CareerApp(root)
    root.mainloop()
