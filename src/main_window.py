import tkinter as tk

from mysql.connector import CMySQLConnection

from login_frame import LoginFrame
from database_frame import DatabaseFrame


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("SQL Displayer")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        # self.config(background="skyblue")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(background="skyblue")

        self.frames = {}

        for Frame in (LoginFrame, DatabaseFrame):
            frame_name = Frame.__name__
            frame = Frame(parent=container, controller=self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.change_frame("LoginFrame")

    def change_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
