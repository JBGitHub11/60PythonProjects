import json
import random
import tkinter as tk
from tkinter import messagebox

class FlashcardQuizGUI:
    def __init__(self, flashcards):
        self.flashcards = flashcards
        self.current_flashcard = None
        self.score = 0
        self.total_questions = len(flashcards)

        self.window = tk.Tk()
        self.window.title("Flashcard Quiz")

        self.question_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.window, font=("Arial", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="Submit", font=("Arial", 16), command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.flashcards:
            self.current_flashcard = random.choice(self.flashcards)
            self.flashcards.remove(self.current_flashcard)
            self.question_label.config(text=self.current_flashcard['question'])
            self.answer_entry.delete(0, tk.END)
        else:
            self.show_result()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == self.current_flashcard['answer'].lower():
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Wrong", f"The correct answer is: {self.current_flashcard['answer']}")
        self.next_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Quiz completed! Your score: {self.score}/{self.total_questions}")
        self.window.quit()

def load_flashcards(file_path):
    with open(file_path, 'r') as file:
        flashcards = json.load(file)
    return flashcards

def main():
    file_path = 'flashcards.json'
    flashcards = load_flashcards(file_path)
    FlashcardQuizGUI(flashcards)

if __name__ == '__main__':
    main()