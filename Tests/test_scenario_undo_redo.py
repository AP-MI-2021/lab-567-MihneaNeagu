from Logic.CRUD import adauga_rezervare
from UserInterface.console import ui_sterge_rezervare


def test_programme():
    lista = []
    undo_list = []
    redo_list = []
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)
    lista = adauga_rezervare("2", "Trump", "economy", 1500, "nu", lista)
    lista = adauga_rezervare("3", "Messi", "economy", 25, "nu ", lista)
    assert ui_sterge_rezervare(lista, undo_list, redo_list) == [{"1", "Obama", "business", 900, "da"},{"2", "Trump", "economy", 1500, "nu"}]

