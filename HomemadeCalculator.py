import tkinter as tk
from tkinter import ttk, messagebox

# Function to handle button clicks and keyboard inputs
def button_click(value):
    global new_input
    if value == "C":
        entry.delete(0, tk.END)  # Clear the display
        new_input = False
    elif value == "=" or value == "<Return>":
        try:
            result = eval(entry.get())  # Evaluate the expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            global last_result
            last_result = str(result)
            new_input = True
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
    else:
        if new_input and value.isdigit():
            entry.delete(0, tk.END)  # Clear previous result if a number is pressed
            new_input = False
        entry.insert(tk.END, value)  # Add the button value to the display

# Function to handle keypress events
def key_press(event):
    allowed_keys = "0123456789+-*/."
    if event.keysym in ["Return", "KP_Enter"]:
        button_click("=")
    elif event.char in allowed_keys:
        button_click(event.char)
    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get()) - 1, tk.END)
    elif event.keysym == "Escape":
        button_click("C")

# Create the main window
window = tk.Tk()
window.title("🐸 Ribas' Calculator")  # Title with a frog emoji
window.geometry("400x600")  # Increased size for better layout
window.resizable(False, False)  # Disable resizing

# Use ttk for modern themed widgets
style = ttk.Style()
style.theme_use("clam")  # Choose a modern theme
style.configure("TButton", font=("Arial", 18), padding=5)

# Entry widget to display the current expression
entry = ttk.Entry(window, font=("Arial", 30), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Global variable to track if a new input starts after showing the result
new_input = False

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Configure row and column weights for resizing
for i in range(5):  # 4 rows for buttons + 1 for entry
    window.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 columns
    window.grid_columnconfigure(i, weight=1)

# Create buttons and place them on the grid
for text, row, col in buttons:
    button = ttk.Button(
        window,
        text=text,
        command=lambda value=text: button_click(value),
    )
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

window.bind("<Key>", key_press)

# Run the main loop
window.mainloop()
