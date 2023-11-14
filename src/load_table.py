from tkinter import Listbox, END
from tkinter.ttk import Treeview

from mysql.connector import CMySQLConnection


def load_table(
    root: Treeview, table_listbox: Listbox, connection: CMySQLConnection
) -> None:
    if not isinstance(root, Treeview):
        print("Bad root widget given, therefore cannot load database")
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_listbox.get(table_listbox.curselection())}'"
    )
    columns = []
    for db_element in cursor:
        columns.append(db_element[3])
    # TODO: Add buttons for editing and deleting existing records in table / columns.append()
    root.configure(columns=tuple(columns))
    for heading in columns:
        root.heading(f"{heading}", text=f"{heading}")

    cursor.execute(f"SELECT * FROM {table_listbox.get(table_listbox.curselection())};")
    for row in cursor:
        root.insert("", END, values=row)
