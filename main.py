from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

BG_COLOR = "#616F39"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    psw_letters = [choice(letters) for _ in range(randint(8, 10))]
    psw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    psw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = psw_letters + psw_symbols + psw_numbers

    shuffle(password_list)

    password = "".join(password_list)

    if len(password_entry.get()) == 0:
        password_entry.insert(0, password)
        pyperclip.copy(password)  # copia automaticamente il testo della password non appena viene generata
    else:
        messagebox.showinfo(title="Error", message="You already have a password"
                                                   "\nDelete the old one before")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Salva i dati inseriti e pulisce i campi per una nuova immissione"""
    website_data = website_entry.get()
    username_data = username_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(username_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please fill empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"Username: {username_data}"
                                                                   f"\nPassword: {password_data}"
                                                                   f"\n"f"Correct?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_data} | {username_data} | {email_data} | {password_data}\n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- MASK PASSWORD ------------------------------- #
click = 0


def mask_psw():
    global click
    if click % 2 == 0:
        password_entry.config(show="*")
        mask_psw_button.config(text="🔒")
        click += 1
    else:
        password_entry.config(show="")
        mask_psw_button.config(text="🔓")
        click += 1


def data():
    new_window = Toplevel(window)
    new_window.title("Elenco Account")
    new_window.config(padx=30, pady=30)

    title_label = Label(new_window, text="Elenco Account")
    title_label.pack()

    with open("data.txt", "r") as data:
        data_file = Text(new_window)
        data_file.insert(1.0, data.read())
        data_file.pack()

    close_button = Button(new_window, text="Close", bg="red", width=30, command=new_window.destroy)
    close_button.pack()

    new_window.mainloop()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

# Labels
website_label = Label(text="Website:")
username_label = Label(text="Username:")
email_label = Label(text="Email:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
email_label.grid(column=0, row=3)
password_label.grid(column=0, row=4)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
username_entry = Entry(width=35)
email_entry = Entry(width=35)
email_entry.insert(END, "lollo.m_96@hotmail.it")  # Se si desidera inserire una mail usata spesso
password_entry = Entry(width=25)

website_entry.grid(column=1, row=1, columnspan=2)
username_entry.grid(column=1, row=2, columnspan=2)
email_entry.grid(column=1, row=3, columnspan=2)
password_entry.place(x=161, y=270)

# Buttons
gen_psw_button = Button(text="⚀⚂⚅", command=generate_password)
gen_psw_button.grid(column=2, row=4)
mask_psw_button = Button(text="🔓", command=mask_psw)
mask_psw_button.place(x=450, y=270)
add_button = Button(text="Add", width=25, bg="green", command=save)
add_button.grid(column=2, row=5)
data_button = Button(text="Elenco Account", width=25, command=data)
data_button.grid(column=1, row=5)
close_button = Button(text="Close", width=5, bg="red", command=window.destroy)
close_button.grid(column=4, row=6)

window.mainloop()
