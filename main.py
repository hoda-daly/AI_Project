
import tkinter as tk
from tkinter import messagebox
import random
import timeit
import matplotlib.pyplot as plt
import pygame
from minimax_algorithm import minimax
from minimax_heuristic_algorithm import minimax_with_heuristic
from alpha_beta_algorithm import alpha_beta_pruning
from symmetry_reduction_algorithm import symmetry_reduction
from heuristic_reduction_algorithm import heuristic_reduction

pygame.init()

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.ai_algorithm = None  # Placeholder for the selected AI algorithm

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text="", font=("Helvetica", 16), width=10, height=4,
                                   command=lambda i=i, j=j: self.make_move(i, j),bg='black', fg='black')
                button.grid(row=i, column=j)
                self.buttons.append(button)

        # Dropdown menu for selecting AI algorithm
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Random")  # Default algorithm
        algorithms = ["Random", "Minimax", "Minimax with Heuristic", "Alpha-Beta Pruning", "Symmetry Reduction", "Heuristic Reduction"]
        algorithm_menu = tk.OptionMenu(self.master, self.algorithm_var, *algorithms, command=self.select_algorithm)
        algorithm_menu.grid(row=3, column=0, columnspan=3, pady=10)

        # Button for comparing algorithm time complexity
        compare_button = tk.Button(self.master, text="Compare Algorithms", command=self.compare_algorithms)

        compare_button.grid(row=4, column=0, columnspan=3, pady=10)

    def select_algorithm(self, algorithm):
        self.ai_algorithm = algorithm

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.play_sound("win")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.play_sound("tie")
                self.reset_game()
            else:
                self.switch_player()
                if self.current_player == "O" and self.ai_algorithm:
                    self.computer_move()

    def computer_move(self):
        if self.ai_algorithm == "Random":
            self.random_move()
        elif self.ai_algorithm == "Minimax":
            self.minimax_move(minimax)
        elif self.ai_algorithm == "Minimax with Heuristic":
            self.minimax_move(minimax_with_heuristic)
        elif self.ai_algorithm == "Alpha-Beta Pruning":
            self.minimax_move(alpha_beta_pruning)
        elif self.ai_algorithm == "Symmetry Reduction":
            self.minimax_move(symmetry_reduction)
        elif self.ai_algorithm == "Heuristic Reduction":
            self.minimax_move(heuristic_reduction)

    def random_move(self):
        available_moves = [i for i in range(9) if self.board[i] == " "]
        if available_moves:
            index = random.choice(available_moves)
            self.master.after(500, lambda: self.make_move(index // 3, index % 3))

    def minimax_move(self, algorithm):
        if self.ai_algorithm != "Random":
            best_move = algorithm(self.board, "O")
            self.master.after(500, lambda: self.make_move(best_move // 3, best_move % 3))

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text="", state=tk.NORMAL)
        self.current_player = "X"

    def compare_algorithms(self):
        repetitions = 10  # Adjust the number of repetitions as needed

        minimax_time = timeit.timeit(lambda: self.run_algorithm(minimax), number=repetitions)
        minimax_heuristic_time = timeit.timeit(lambda: self.run_algorithm(minimax_with_heuristic), number=repetitions)
        alpha_beta_time = timeit.timeit(lambda: self.run_algorithm(alpha_beta_pruning), number=repetitions)
        symmetry_reduction_time = timeit.timeit(lambda: self.run_algorithm(symmetry_reduction), number=repetitions)
        heuristic_time = timeit.timeit(lambda: self.run_algorithm(heuristic_reduction), number=repetitions)

        print(f"Minimax Time: {minimax_time} seconds")
        print(f"Minimax with Heuristic Time: {minimax_heuristic_time} seconds")
        print(f"Alpha-Beta Pruning Time: {alpha_beta_time} seconds")
        print(f"Symmetry Reduction Time: {symmetry_reduction_time} seconds")
        print(f"Heuristic Reduction Time: {heuristic_time} seconds")

        self.plot_comparison(["Minimax", "Minimax with Heuristic", "Alpha-Beta Pruning", "Symmetry Reduction", "Heuristic Reduction"],
                             [minimax_time, minimax_heuristic_time, alpha_beta_time, symmetry_reduction_time, heuristic_time])

    def run_algorithm(self, algorithm_func):
        start_time = timeit.default_timer()
        move = algorithm_func(self.board, "O")
        end_time = timeit.default_timer()
        return end_time - start_time

    def plot_comparison(self, algorithms, execution_times):
        plt.bar(algorithms, execution_times)
        plt.xlabel('Algorithms')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Comparison of Algorithms')
        plt.show()

    def play_sound(self, sound_type):
        if sound_type == "win":
            sound_file = "win_sound.wav"
        elif sound_type == "tie":
            sound_file = "tie_sound.wav"
        else:
            return

        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

