import tkinter as tk
from tkinter import simpledialog, messagebox

def exit_program():
    if confirmation_var.get():
        messagebox.showinfo("Confirmation", "Thank you! The information you provided have been submitted. Have a Nice Day :)).")
        root.destroy()
    else:
        messagebox.showwarning("Error", "Check the box if you confirm that you entered correct information.")

root = tk.Tk()
root.title("GETTING TO KNOW YOU!!")

def popup():
    name = simpledialog.askstring("Name", "What is your name?")
    age = simpledialog.askinteger("Age", "How old are you?")
    address = simpledialog.askstring("Address", "Please input your address")

    label1.config(text="Mabuhay! My name is {}".format(name))
    label2.config(text="I am {} years of age".format(age))
    label3.config(text="I am from {}".format(address))

# Styling
root.configure(bg="#8b00ff")  # Violet background color
button_color = "#00ff00"      # Green button color
label_bg_color = "#c6e2ff"    # Light blue label background color
font_style = ('Century Gothic', 12)

# Labels
label1 = tk.Label(root, width=50, height=1, bg=label_bg_color, font=font_style)
label2 = tk.Label(root, width=50, height=1, bg=label_bg_color, font=font_style)
label3 = tk.Label(root, width=50, height=1, bg=label_bg_color, font=font_style)

# Checkbox for confirmation
confirmation_var = tk.BooleanVar()
confirmation_check = tk.Checkbutton(root, width=60, height=1, text="I confirm that all the information I entered is correct.", font=font_style, bg=label_bg_color, variable=confirmation_var)

# Buttons
button = tk.Button(root, width=55, text="Enter Personal Information", command=popup, bg=button_color, font=font_style)
submit_button = tk.Button(root, width=55, text="Submit", command=exit_program, bg=button_color, font=font_style)

# Layout
label1.grid(row=1, column=0, columnspan=2, pady=(10, 0))
label2.grid(row=2, column=0, columnspan=2)
label3.grid(row=3, column=0, columnspan=2)
button.grid(row=0, column=0, columnspan=2, pady=(20, 10))
confirmation_check.grid(row=4, column=0, columnspan=2, pady=(0, 10))
submit_button.grid(row=5, column=0, columnspan=2, pady=(0, 20))

root.mainloop()
