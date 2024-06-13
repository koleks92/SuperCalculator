import tkinter as tk
import webbrowser


# Constants
WIDTH = 300
HEIGHT = 500
PADDING = 1
FONT = ("Digital-7", 20)

# Numbers, operator
first_number = ''
operator = ''
second_number = ''

# Menu bar functions
def exit_app():
    root.quit()

# Clear screen and variables
def clear_screen():
    global first_number
    global second_number
    global operator

    first_number = ''
    second_number = ''
    operator = ''

    print_screen(canvas, screen_text, '')

# Open the link
def open_link(link):
    webbrowser.open_new(link)

# Show popup window "About"
def about_window():
    popup = tk.Toplevel(root)
    popup.title("About")
    popup.geometry("300x200")

    # About title text
    title = tk.Label(popup, text="About", font=("Helvetica", 18))
    title.pack(pady=8)


    line_1 = tk.Label(popup, text="Created by koleks92", font=("Helvetica", 14))
    line_1.pack(pady=8)


    line_2 = tk.Label(popup, text="github", font=("Helvetica", 12, "bold"))
    line_2.pack(pady=2)
    line_2.bind("<Button-1>", lambda e: open_link('www.github.com/koleks92'))

    line_3 = tk.Label(popup, text="linkedin", font=("Helvetica", 12, "bold"))
    line_3.pack(pady=1)
    line_3.bind("<Button-1>", lambda e: open_link('www.linkedin.com/in/jan-konieczek'))



# Create a button
def create_button(value, canvas, screen_text):
    return tk.Button(root, text=value, command=lambda: on_button_click(canvas, value, screen_text), font=FONT)

# Create all buttons
def draw_one_row(v1, v2, v3, v4, row, canvas, screen_text):
    button1 = create_button(v1, canvas, screen_text)
    button1.grid(row=row, column=0, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button2 = create_button(v2, canvas, screen_text)
    button2.grid(row=row, column=1, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button3 = create_button(v3, canvas, screen_text)
    button3.grid(row=row, column=2, padx=PADDING, pady=PADDING, sticky="nsew")
    
    button4 = create_button(v4, canvas, screen_text)
    button4.grid(row=row, column=3, padx=PADDING, pady=PADDING, sticky="nsew")


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
            print_screen(canvas, screen_text, round((first + second), 6))
        elif operator == '-':
            print_screen(canvas, screen_text, round((first - second), 6))
        elif operator == '/':
            print_screen(canvas, screen_text, round((first / second), 6))
        elif operator == '*':
            print_screen(canvas, screen_text, round((first * second), 6))

        operator = '='

        
# Main function
def main():
    # Make root and canvas global
    global root
    global canvas, screen_text

    # Create main window
    root = tk.Tk()
    root.title("SuperCalculator")
    root.resizable(False, False)

    # Create a menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Create a Calculator menu
    calculator_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Calculator", menu=calculator_menu)


    # Add menu items to Calculator menu
    calculator_menu.add_command(label="Clear screen", command=clear_screen)
    calculator_menu.add_separator()
    calculator_menu.add_command(label="About", command=about_window)
    calculator_menu.add_separator()
    calculator_menu.add_command(label="Exit", command=exit_app)

    
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
    draw_one_row("1", "2", "3", "+", 1, canvas, screen_text)
    draw_one_row("4", "5", "6", "-", 2, canvas, screen_text)
    draw_one_row("7", "8", "9", "/", 3, canvas, screen_text)
    draw_one_row("0", ".", "=", "*", 4, canvas, screen_text)

    # Run graphics
    root.mainloop()

if __name__ == "__main__":
    main()
