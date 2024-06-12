import tkinter as tk

# Constants
WIDTH = 400
HEIGHT = 500
PADDING = 1
FONT = ("Helvetica", 18)

# Create a button
def create_button(root, label):
    return tk.Button(root, text=label, command=lambda: on_button_click(label), font=FONT)

# Create buttons
def draw_one_row(root, v1, v2, v3, v4, row):
    button1 = create_button(root, v1)
    button1.grid(row=row, column=0, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button2 = create_button(root, v2)
    button2.grid(row=row, column=1, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button3 = create_button(root, v3)
    button3.grid(row=row, column=2, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button4 = create_button(root, v4)
    button4.grid(row=row, column=3, padx=PADDING, pady=PADDING, sticky="nsew")

# On button click function
def on_button_click(value):
    print(f"Click: {value}")

# Main function
def main():
    # Create main window
    root = tk.Tk()
    root.title("SuperCalculator")
    

    # Create grid
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    for i in range(5):
        root.grid_rowconfigure(i, weight=1)

    # Create a canvas and screen
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT / 5)
    canvas.grid(row=0, column=0, columnspan=4, sticky="s")

    rect = canvas.create_rectangle(0, 0, WIDTH, HEIGHT / 5, fill='black')

    # Draw all buttons
    draw_one_row(root, 1, 2, 3, "+", 1)
    draw_one_row(root, 4, 5, 6, "-", 2)
    draw_one_row(root, 7, 8, 9, "/", 3)
    draw_one_row(root, 0, ".", "=", "*", 4)

    # Run graphics
    root.mainloop()

if __name__ == "__main__":
    main()
