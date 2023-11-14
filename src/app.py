from typing import Optional

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from load_table import load_table
from connect_to_database import connect_to_database
from load_listbox import load_listbox
from load_db_tables import load_db_tables


def switch_window(from_window: Tk) -> None:
    host_enter, user_enter, password_enter = (
        from_window.children["host_enter"].get(),
        from_window.children["user_enter"].get(),
        from_window.children["password_enter"].get(),
    )
    from_window
    from_window.destroy()
    db_window(host_enter, user_enter, password_enter)


def db_window(host_enter: str, user_enter: str, password_enter: str) -> None:
    # ! Don't know if the False is needed or not, beacuse if in lambda everything works fine
    if (
        connection := connect_to_database(host_enter, user_enter, password_enter)
    ) == False:
        # * Sendng message to login screen and exiting db_window function with return statement before db_window is created
        login_window("Could not connect with Your database, please try again")
        return

    db_window = Tk()
    db_window.geometry(
        f"{db_window.winfo_screenwidth()}x{db_window.winfo_screenheight()}"
    )
    db_window.title("Database editor")
    db_window.config(background="skyblue")

    db_label = Label(text="Choose Database")
    db_label.pack(pady=20)

    db_listbox = Listbox(
        master=db_window,
        listvariable=load_listbox(connection),
        height=6,
        selectmode=SINGLE,
        exportselection=0,
    )
    db_listbox.bind(
        "<<ListboxSelect>>",
        lambda event: table_listbox.config(
            listvariable=load_db_tables(db_listbox=db_listbox, connection=connection),
        ),
    )
    db_listbox.pack(pady=20)

    table_label = Label(text="Choose Table")
    table_label.pack(pady=20)

    table_listbox = Listbox(
        master=db_window, height=2, selectmode=SINGLE, exportselection=0
    )
    table_listbox.bind(
        "<<ListboxSelect>>",
        lambda event: load_table(table_frame, table_listbox, connection),
    )
    table_listbox.pack(pady=20)

    table_frame = ttk.Treeview(db_window, show="headings")
    table_frame.pack(pady=10)
    # db_window.send()


def login_window(message: Optional[str] = None) -> None:
    login_window = Tk()
    login_window.geometry(
        f"{login_window.winfo_screenwidth()}x{login_window.winfo_screenheight()}"
    )
    login_window.title("Database editor")
    login_window.config(background="skyblue")

    host_label = Label(master=login_window, text="Enter host")
    host_label.pack(pady=20)

    host_enter = Entry(master=login_window, name="host_enter")
    host_enter.pack(pady=20)

    user_label = Label(master=login_window, text="Enter user")
    user_label.pack(pady=20)

    user_enter = Entry(master=login_window, name="user_enter")
    user_enter.pack(pady=20)

    password_label = Label(master=login_window, text="Enter password")
    password_label.pack(pady=20)

    password_enter = Entry(master=login_window, name="password_enter")
    password_enter.pack(pady=20)

    host_enter = Entry(master=login_window)

    if message != None:
        showinfo(title="ERROR", message=message)

    sign_in_btn = Button(
        master=login_window, text="Sign in", command=lambda: switch_window(login_window)
    )
    sign_in_btn.pack(pady=20)


def main():
    login_window()
    mainloop()


if __name__ == "__main__":
    main()
