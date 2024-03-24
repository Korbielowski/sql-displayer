from typing import Optional

import tkinter as tk
from tkinter import ttk

# from app import MainWindow
from database import load_db_tables, load_table, load_listbox


class DatabaseFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        self.connection = None

        db_label = tk.Label(self, text="Choose Database")
        db_label.pack(pady=20)

        self.list_var = None

        self.db_listbox = tk.Listbox(
            master=self,
            listvariable=self.list_var,
            height=6,
            selectmode=tk.SINGLE,
            exportselection=0,
        )
        self.db_listbox.bind(
            "<<ListboxSelect>>",
            lambda event: table_listbox.config(
                listvariable=load_db_tables(
                    db_listbox=self.db_listbox, connection=self.connection
                ),
            ),
        )
        self.db_listbox.pack(pady=20)

        table_label = tk.Label(self, text="Choose Table")
        table_label.pack(pady=20)

        table_listbox = tk.Listbox(
            master=self, height=2, selectmode=tk.SINGLE, exportselection=0
        )
        table_listbox.bind(
            "<<ListboxSelect>>",
            lambda event: load_table(table_frame, table_listbox, self.connection),
        )
        table_listbox.pack(pady=20)

        table_frame = ttk.Treeview(self, show="headings")
        table_frame.pack(pady=10)

    def update_connection(self, connection) -> None:
        self.connection = connection
        self.list_var = load_listbox(connection)
        self.db_listbox.config(listvariable=self.list_var)
