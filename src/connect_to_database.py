from mysql.connector import connect, Error, CMySQLConnection
from typing import Union


def connect_to_database(
    host_enter: str, user_enter: str, password_enter: str
) -> Union[CMySQLConnection, bool]:
    try:
        if host_enter == "" or user_enter == "" or password_enter == "":
            return False
        connection = connect(
            host=f"{host_enter}", user=f"{user_enter}", password=f"{password_enter}"
        )
        return connection
    except Error:
        return False
