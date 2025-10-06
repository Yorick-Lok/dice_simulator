from random import randint
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk

class DiceGameApp:
    """Class for the dice simulator app."""
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Simulator")
        self.root.geometry("400x500")
        self.create_widgets()

        # Load Dice Face Images.
        self.dice_images = self.load_dice_images()

    def load_dice_images(self, size=64):
        """Preload dice images into a dictionary."""
        dice_images = {}
        for i in range(1, 7):
            try:
                img = Image.open(f"dice{i}.png").resize((size, size), Image.Resampling.LANCZOS)
                dice_images[i] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error loading dice{i}.png: {e}")
                dice_images[i] = None  # Use None if image is missing
        return dice_images

    def create_widgets(self):
        """Create the widgets here."""
        self.instruction_label = tk.Label(self.root, text="How many dice would you like to roll? (1 to 100)")
        self.instruction_label.pack(pady=10)

        self.dice_entry = tk.Entry(self.root, width=5)
        self.dice_entry.pack()

        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack(pady=10)

        # Directly pack dice_frame inside root, no scrollbar, no canvas
        self.dice_frame = tk.Frame(self.root)
        self.dice_frame.pack(pady=5)

        self.output_area = scrolledtext.ScrolledText(self.root, width=45, height=15, wrap=tk.WORD)
        self.output_area.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

    def roll_dice(self):
        """Roll the dice and display results."""
        self.output_area.delete(1.0, tk.END)
        for widget in self.dice_frame.winfo_children():
            widget.destroy()

        try:
            num_dice = int(self.dice_entry.get())
            if num_dice < 1 or num_dice > 100:
                messagebox.showerror("Invalid Input", "Please choose a number between 1 and 100")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        # Dynamically choose image size based on number of dice
        if num_dice <= 5:
            size = 64
        elif num_dice <= 10:
            size = 48
        elif num_dice <= 20:
            size = 36
        else:
            size = 24

        # Reload images with new size
        self.dice_images = self.load_dice_images(size)

        results = []
        bottom_results = []
        six_rolls = 0

        self.output_area.insert(tk.END, f"Rolling {num_dice} dice...\n\n")

        dice_per_row = 10

        # Number of rows needed
        total_rows = (num_dice + dice_per_row - 1) // dice_per_row

        for i in range(num_dice):
            roll = randint(1, 6)
            bottom = 7 - roll
            results.append(roll)
            bottom_results.append(bottom)

            row = i // dice_per_row
            # Determine dice count in this row
            if row == total_rows - 1:  # last row
                dice_in_row = num_dice % dice_per_row if num_dice % dice_per_row != 0 else dice_per_row
            else:
                dice_in_row = dice_per_row

            # Calculate left padding to center dice in the row
            padding = (dice_per_row - dice_in_row) // 2

            col = i % dice_per_row + padding

            # Check if image exists for this roll
            img = self.dice_images.get(roll)
            if img:
                img_label = tk.Label(self.dice_frame, image=img)
                img_label.image = img  # keep a reference
            else:
                img_label = tk.Label(self.dice_frame, text=str(roll), font=("Arial", 16), width=2, height=1)

            img_label.grid(row=row, column=col, padx=2, pady=2)

            self.output_area.insert(tk.END, f"Dice {i+1}: {roll}\n")
            self.output_area.insert(tk.END, f"Bottom of Dice {i+1}: {bottom}\n\n")

            if roll == 6:
                six_rolls += 1

        if six_rolls >= 3:
            self.output_area.insert(tk.END, f"You rolled a six {six_rolls} times!\n\n")

        total = sum(results)
        bottom_total = sum(bottom_results)

        self.output_area.insert(tk.END, f"Your dice add up to: {total}\n")
        self.output_area.insert(tk.END, f"The bottom of your dice add up to: {bottom_total}\n")

        self.roll_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        """Reset the game if the user wants to play again."""
        self.dice_entry.delete(0, tk.END)
        self.output_area.delete(1.0, tk.END)

        for widget in self.dice_frame.winfo_children():
            widget.destroy()

        self.roll_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceGameApp(root)
    root.mainloop()
