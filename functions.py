from tkinter import messagebox, END
from random import choice, randint, shuffle
import string
import json
import pyperclip


def generate_password(pass_entry):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", "_", "@", "?"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(END, password)
    pyperclip.copy(password)


def load_data():
    try:
        with open("data.json", "r") as data_file:
            return json.load(data_file)
    except FileNotFoundError:
        return {}
    
def confirm_save(website, user, password):
    return messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nUser: {user} \nPassword:{password} \nShall we save? ",
        )

def confirm_overwrite(website):
    return messagebox.askokcancel(
            title=website,
            message=f"There is an existing {website.capitalize()} in the data. Do you want to overwrite it?",
        )

def save_data(web_entry, user_entry, pass_entry):
    web_data = web_entry.get().lower()
    user_data = user_entry.get()
    pass_data = pass_entry.get()

    if not web_data or not pass_data:
        messagebox.showinfo(
            title="Ouh maaamma", message="Don't let the fields empty my man"
        )
        return
    
    data = load_data()

    if web_data in data:
        if not confirm_overwrite(web_data):
            return

    if not confirm_save(web_data, user_data, pass_data):
            return
    
    data[web_data] = {"email": user_data, "password": pass_data}

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    web_entry.delete(0, END)
    pass_entry.delete(0, END)


def find_data(web_entry):
    website = web_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            user = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=f"{website.capitalize()}",
                message=f"User: {user} \nPassword: {password}",
            )
        else:
            messagebox.showinfo(
                title="Sorry",
                message=f"No details of the {website.capitalize()} exists",
            )
