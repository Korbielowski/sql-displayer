from load_databse import load_database
from tkinter import Tk


# ? How to run tests in venv
def test_load_database():
    assert (
        load_database("dad")
    ) == "Bad root widget given, therefore cannot load database"
    assert (load_database(1)) == "Bad root widget given, therefore cannot load database"
    assert (load_database(Tk)) == None
