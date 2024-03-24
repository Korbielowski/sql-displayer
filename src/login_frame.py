from typing import Optional

from database import connect_to_db

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from main_window import MainWindow


class LoginFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: MainWindow) -> None:
        super().__init__(parent)
        self.parent: tk.Frame = parent
        self.controller: MainWindow = controller

        self.host_name = tk.StringVar()
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        host_label = tk.Label(master=self, text="Enter host")
        host_label.pack(pady=20)

        host_enter = tk.Entry(
            master=self, name="host_enter", textvariable=self.host_name
        )
        host_enter.pack(pady=20)

        user_label = tk.Label(master=self, text="Enter user")
        user_label.pack(pady=20)

        user_enter = tk.Entry(
            master=self, name="user_enter", textvariable=self.user_name
        )
        user_enter.pack(pady=20)

        password_label = tk.Label(master=self, text="Enter password")
        password_label.pack(pady=20)

        password_enter = tk.Entry(
            master=self, name="password_enter", textvariable=self.password
        )
        password_enter.pack(pady=20)

        sign_in_btn = tk.Button(master=self, text="Sign in", command=self.check_data)
        sign_in_btn.pack(pady=20)

    def check_data(self) -> None:
        # ! Don't know if the False is needed or not, beacuse if in lambda everything works fine
        if (
            connection := connect_to_db(
                self.host_name.get(), self.user_name.get(), self.password.get()
            )
        ) != False:
            self.controller.frames["DatabaseFrame"].update_connection(connection)
            self.controller.change_frame("DatabaseFrame")
        else:
            showinfo(
                title="ERROR",
                message="Could not connect with Your database, please try again",
            )
