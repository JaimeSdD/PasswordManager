from tkinter import *
from functions import generate_password, save_data, find_data

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_text = Label(text="Website")
web_text.grid(row=1, column=0)
user_text = Label(text="Email/Username")
user_text.grid(row=2, column=0)
pass_text = Label(text="Password")
pass_text.grid(row=3, column=0)

web_entry = Entry(width=30)
web_entry.grid(row=1, column=1)
web_entry.focus()
user_entry = Entry(width=48)
user_entry.insert(END, "Prueba")
user_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=30)
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Search", width=14, command=lambda: find_data(web_entry))
generate_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=lambda: generate_password(pass_entry))
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=41, command=lambda: save_data(web_entry, user_entry, pass_entry))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
