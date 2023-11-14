from mysql.connector import CMySQLConnection

from tkinter import Variable


def load_listbox(connection: CMySQLConnection) -> Variable:
    cursor = connection.cursor()
    cursor.execute("SHOW SCHEMAS;")
    db_names = []
    for db_name in cursor:
        db_names.append(*db_name)
    return Variable(
        value=db_names,
    )
