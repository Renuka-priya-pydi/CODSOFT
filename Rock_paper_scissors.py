
import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.master.geometry("1000x1000")
        self.master.configure(bg="#FFDB58")  # Mustard background color

        self.user_score = 0
        self.comp_score = 0
        self.round = 1

        self.page1()

    def page1(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Rock Paper Scissors Game", font=("Helvetica", 24), bg="#FFDB58")
        label.pack(pady=50)
        label.place(x=300,y=300)


        start_button = tk.Button(self.master, text="Start", command=self.page2, font=("Helvetica", 16))
        start_button.pack()
        start_button.place(x=495,y=360)

    def page2(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Choose: Rock, Paper, or Scissors", font=("Helvetica", 20), bg="#FFDB58")
        label.pack(pady=50)

        self.user_choice_var = tk.StringVar()

        choices_frame = tk.Frame(self.master, bg="#FFDB58")
        choices_frame.pack()

        rock_button = tk.Radiobutton(choices_frame, text="Rock", variable=self.user_choice_var, value="rock", font=("Helvetica", 16))
        rock_button.grid(row=0, column=0, padx=20)
       
        paper_button = tk.Radiobutton(choices_frame, text="Paper", variable=self.user_choice_var, value="paper", font=("Helvetica", 16))
        paper_button.grid(row=0, column=1, padx=20)
       
        scissors_button = tk.Radiobutton(choices_frame, text="Scissors", variable=self.user_choice_var, value="scissors", font=("Helvetica", 16))
        scissors_button.grid(row=0, column=2, padx=20)
        
        play_button = tk.Button(self.master, text="Play", command=self.play, font=("Helvetica", 16))
        play_button.pack(pady=20)
        

    def play(self):
        user_choice = self.user_choice_var.get()
        comp_choice = random.choice(["rock", "paper", "scissors"])

        result = self.determine_winner(user_choice, comp_choice)

        self.page3(user_choice, comp_choice, result)

    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "tie"
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "scissors" and comp_choice == "paper") or \
             (user_choice == "paper" and comp_choice == "rock"):
            self.user_score += 1
            return "win"
        else:
            self.comp_score += 1
            return "lose"

    def page3(self, user_choice, comp_choice, result):
        self.clear_screen()

        label = tk.Label(self.master, text="Result", font=("Helvetica", 24), bg="#FFDB58")
        label.pack(pady=50)

        result_label = tk.Label(self.master, text=f"User's choice: {user_choice}\nComputer's choice: {comp_choice}", font=("Helvetica", 16), bg="#FFDB58")
        result_label.pack()

        if result == "win":
            result_text = "You win!"
        elif result == "lose":
            result_text = "You lose!"
        else:
            result_text = "It's a tie!"
        result_label = tk.Label(self.master, text=result_text, font=("Helvetica", 16), bg="#FFDB58")
        result_label.pack(pady=20)

        score_button = tk.Button(self.master, text="Score Board", command=self.page4, font=("Helvetica", 16))
        score_button.pack(pady=20)

        play_again_button = tk.Button(self.master, text="Play Again", command=self.page2, font=("Helvetica", 16))
        play_again_button.pack(pady=20)

    def page4(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Score Board", font=("Helvetica", 24), bg="#FFDB58")
        label.pack(pady=50)

        score_label = tk.Label(self.master, text=f"User Score: {self.user_score}\nComputer Score: {self.comp_score}", font=("Helvetica", 20), bg="#FFDB58")
        score_label.pack(pady=20)

        back_button = tk.Button(self.master, text="Back to Game", command=self.page2, font=("Helvetica", 16))
        back_button.pack(pady=20)

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    root.configure(bg="black")  # Black background color for all pages
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

