import tkinter as tk

from mysql.connector import CMySQLConnection

from login_frame import LoginFrame
from database_frame import DatabaseFrame
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from typing import Optional

import tkinter as tk
from tkinter import ttk

# from app import MainWindow
from database import load_db_tables, load_table, load_listbox


class LoginFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        frame = tk.Frame(self.parent, background="skyblue")
        frame.pack(fill="both", expand=1)

        self.host_name = tk.StringVar()
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        host_label = tk.Label(master=frame, text="Enter host")
        host_label.pack(pady=20)

        host_enter = tk.Entry(
            master=frame, name="host_enter", textvariable=self.host_name
        )
        host_enter.pack(pady=20)

        user_label = tk.Label(master=frame, text="Enter user")
        user_label.pack(pady=20)

        user_enter = tk.Entry(
            master=frame, name="user_enter", textvariable=self.user_name
        )
        user_enter.pack(pady=20)

        password_label = tk.Label(master=frame, text="Enter password")
        password_label.pack(pady=20)

        password_enter = tk.Entry(
            master=frame, name="password_enter", textvariable=self.password
        )
        password_enter.pack(pady=20)

        sign_in_btn = tk.Button(master=parent, text="Sign in", command=self.check_data)
        sign_in_btn.pack(pady=20)

    def check_data(self) -> None:
        # ! Don't know if the False is needed or not, beacuse if in lambda everything works fine
        if (
            connection := connect_to_db(
                self.host_name.get(), self.user_name.get(), self.password.get()
            )
        ) != False:
            self.controller.frame_list[1].update_connection(connection)
            self.controller.change_frame("DatabaseFrame")
        else:
            showinfo(
                title="ERROR",
                message="Could not connect with Your database, please try again",
            )


class DatabaseFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        frame = tk.Frame(self.parent, background="red")
        frame.pack(fill="both", expand=1)

        db_label = tk.Label(frame, text="Choose Database")
        db_label.pack(pady=20)

        self.list_var = None

        self.db_listbox = tk.Listbox(
            master=frame,
            listvariable=self.list_var,
            height=6,
            selectmode=tk.SINGLE,
            exportselection=0,
        )
        self.db_listbox.bind(
            "<<ListboxSelect>>",
            lambda event: table_listbox.config(
                listvariable=load_db_tables(
                    db_listbox=self.db_listbox, connection=self.controller.connection
                ),
            ),
        )
        self.db_listbox.pack(pady=20)

        table_label = tk.Label(frame, text="Choose Table")
        table_label.pack(pady=20)

        table_listbox = tk.Listbox(
            master=frame, height=2, selectmode=tk.SINGLE, exportselection=0
        )
        table_listbox.bind(
            "<<ListboxSelect>>",
            lambda event: load_table(
                table_frame, table_listbox, self.controller.connection
            ),
        )
        table_listbox.pack(pady=20)

        table_frame = ttk.Treeview(frame, show="headings")
        table_frame.pack(pady=10)

    def update_connection(self, connection) -> None:
        self.list_var = load_listbox(connection)
        self.db_listbox.config(listvariable=self.list_var)
        print(self.list_var)


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("SQL Displayer")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.config(background="skyblue")

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.frames = {}

        for Frame in (LoginFrame, DatabaseFrame):
            frame_name = Frame.__name__
            self.frames[frame_name] = Frame(parent=self.main_frame, controller=self)

        self.change_frame("LoginFrame")

    def change_frame(self, frame_name):
        frame = self.frames[frame_name]
        self.connection = None
        frame.tkraise()


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
