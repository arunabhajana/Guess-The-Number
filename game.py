# The Guess class is a tkinter-based game where the user tries to guess a randomly generated number between 1 and 100.
import tkinter as tk
from tkinter import messagebox
import random

class Guess:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.master.iconphoto(True, tk.PhotoImage(file="guess.png"))

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.intro_label = tk.Label(master, text="Welcome to Guess the Number Game!", font=("Arial", 14, "bold"))
        self.instructions_label = tk.Label(master, text="Try to guess the number between 1 and 100.")
        self.instructions_label2 = tk.Label(master, text="Press Enter to submit your guess.")
        self.guess_label = tk.Label(master, text="Enter your guess:")
        self.guess_entry = tk.Entry(master)
        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.new_game_button = tk.Button(master, text="New Game", command=self.start_new_game)
        self.attempts_label = tk.Label(master, text="Attempts: 0", font=("Arial", 12))

        self.intro_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))
        self.instructions_label.grid(row=1, column=0, columnspan=2)
        self.instructions_label2.grid(row=2, column=0, columnspan=2)
        self.guess_label.grid(row=3, column=0, pady=10)
        self.guess_entry.grid(row=3, column=1, pady=10)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.new_game_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.attempts_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.instructions()

        self.master.bind("<Return>", lambda event: self.check_guess())

    def instructions(self):
        messagebox.showinfo("Instructions", "Welcome to Guess the Number Game!\n\n"
                                            "Try to guess the number between 1 and 100. "
                                            "After each guess, you will be informed if the number is too high, too low, or correct."
                                            "\n\nPress Enter to submit your guess.\nClick 'New Game' to start a new game.")

    def check_guess(self):
        user_guess = self.guess_entry.get()

        try:
            user_guess = int(user_guess)
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            if user_guess == self.secret_number:
                messagebox.showinfo("🎉 Congratulations! 🎉", f"You guessed the correct number in {self.attempts} attempts!")
                self.start_new_game()
            elif user_guess < self.secret_number:
                messagebox.showinfo("Try Again", "Too low! Try a higher number.")
            else:
                messagebox.showinfo("Try Again", "Too high! Try a lower number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def start_new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.guess_entry.delete(0, tk.END)
        messagebox.showinfo("New Game", "A new game has started! Try to guess the new number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = Guess(root)
    root.mainloop()
