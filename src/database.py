from mysql.connector import connect, Error, CMySQLConnection
from tkinter import Variable, Event, Listbox, END
from tkinter.ttk import Treeview
from typing import Union


def connect_to_db(
    host_enter: str, user_enter: str, password_enter: str
) -> Union[CMySQLConnection, bool]:
    try:
        connection = connect(
            host=f"{host_enter}", user=f"{user_enter}", password=f"{password_enter}"
        )
        return connection
    except Error:
        return False


def load_db_tables(db_listbox: Listbox, connection: CMySQLConnection) -> Variable:
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {db_listbox.get(db_listbox.curselection())};")
        cursor.execute("SHOW TABLES;")
        table_names = []
        for table_name in cursor:
            table_names.append(*table_name)
        return Variable(value=table_names)
    except Error:
        print("Could not load tables")


def load_listbox(connection: CMySQLConnection) -> Variable:
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW SCHEMAS;")
        db_names = []
        for db_name in cursor:
            db_names.append(*db_name)

        return Variable(
            value=db_names,
        )
    except AttributeError:
        print("Could not load listbox")


def load_table(
    root: Treeview, table_listbox: Listbox, connection: CMySQLConnection
) -> None:
    try:
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

        cursor.execute(
            f"SELECT * FROM {table_listbox.get(table_listbox.curselection())};"
        )
        for row in cursor:
            root.insert("", END, values=row)
    except Error:
        print("Could not load table")


def add_element() -> None:
    pass


def edit_element() -> None:
    pass


def delete_element() -> None:
    pass


def drop_database() -> None:
    pass
