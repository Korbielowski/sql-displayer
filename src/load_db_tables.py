from mysql.connector import CMySQLConnection

from tkinter import Variable, Event, Listbox


def load_db_tables(db_listbox: Listbox, connection: CMySQLConnection) -> Variable:
    cursor = connection.cursor()
    cursor.execute(f"USE {db_listbox.get(db_listbox.curselection())};")
    cursor.execute("SHOW TABLES;")
    table_names = []
    for table_name in cursor:
        table_names.append(*table_name)
    return Variable(value=table_names)
