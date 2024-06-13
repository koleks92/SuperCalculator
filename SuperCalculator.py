import tkinter as tk

# Constants
WIDTH = 300
HEIGHT = 500
PADDING = 1
FONT = ("Digital-7", 18)

# Create a button
def create_button(root, value, canvas, screen_text):
    return tk.Button(root, text=value, command=lambda: on_button_click(canvas, value, screen_text), font=FONT)

# Create all buttons
def draw_one_row(root, v1, v2, v3, v4, row, canvas, screen_text):
    button1 = create_button(root, v1, canvas, screen_text)
    button1.grid(row=row, column=0, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button2 = create_button(root, v2, canvas, screen_text)
    button2.grid(row=row, column=1, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button3 = create_button(root, v3, canvas, screen_text)
    button3.grid(row=row, column=2, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button4 = create_button(root, v4, canvas, screen_text)
    button4.grid(row=row, column=3, padx=PADDING, pady=PADDING, sticky="nsew")

# Numbers, operator
first_number = ''
operator = ''
second_number = ''

# Print on screen
def print_screen(canvas, screen_text, value):
    canvas.itemconfig(screen_text, text=value)

# Operations function
def on_button_click(canvas, value, screen_text):
    global first_number
    global second_number
    global operator

    # Assign first number, if operator is ''
    if operator == '' and value in '0123456789.':
        if len(first_number) <= 9:
            # Do not allow first number to be 0
            if first_number == '' and value == '0':
                print_screen(canvas, screen_text, first_number)
            # Do not allow more than one '.'
            elif value == '.' and '.' in first_number:
                print_screen(canvas, screen_text, first_number)
            else:                    
                first_number += value
                print_screen(canvas, screen_text, first_number)
    # Clear screen and variables on double '='
    elif value == '=' and operator == '=':
        print_screen(canvas, screen_text, '')
        operator = ''
        first_number = ''
        second_number = ''
    # If first number is provided, set operator
    elif value in '+-/*':
        operator = value
        print_screen(canvas, screen_text, operator)
    # Assign second number, if operator is provided
    elif operator in '+-/*' and value in '0123456789.':
        if len(second_number) <= 9:
            # Do not allow first number to be 0
            if second_number == '' and value == '0':
                print_screen(canvas, screen_text, second_number)
            # Do not allow more than one '.'
            elif value == '.' and '.' in second_number:
                print_screen(canvas, screen_text, second_number)
            else:                    
                second_number += value
                print_screen(canvas, screen_text, second_number)
    # Calcualte result if '=' is clicked, and all three variables are provided
    elif value == '=' and first_number != '' and second_number != '':
        first = float(first_number)
        second = float(second_number)
        
        if operator == '+':
            print_screen(canvas, screen_text, (first + second))
        elif operator == '-':
            print_screen(canvas, screen_text, (first - second))
        elif operator == '/':
            print_screen(canvas, screen_text, round((first / second), 6))
        elif operator == '*':
            print_screen(canvas, screen_text, round((first * second), 6))

        operator = '='

        
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

    # Create a canvas
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT / 8)
    canvas.grid(row=0, column=0, columnspan=4, sticky="s")

    # Create screen
    screen = canvas.create_rectangle(2,2, WIDTH, HEIGHT / 8, fill='black')
    screen_text = canvas.create_text(10, HEIGHT / 14, text='', font=FONT, fill="white", anchor="w")
    

    # Draw all buttons
    draw_one_row(root, "1", "2", "3", "+", 1, canvas, screen_text)
    draw_one_row(root, "4", "5", "6", "-", 2, canvas, screen_text)
    draw_one_row(root, "7", "8", "9", "/", 3, canvas, screen_text)
    draw_one_row(root, "0", ".", "=", "*", 4, canvas, screen_text)

    # Run graphics
    root.mainloop()

if __name__ == "__main__":
    main()
