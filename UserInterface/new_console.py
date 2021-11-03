from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from UserInterface.console import ui_show_all


def help():
    '''
    In meniu comenzile sunt separate prin ; iar variabilele ce trebuie atribuite prin ,
    :return:
    '''
    print("add,id,nume,clasa,pret,checkin")
    print("delete,id")
    print("showall")
    print("update,id,nume,clasa,pret,checkin")
    print("stop")


def run_menu_2(lista):

    while True:
        option = input("Introduceti comanda: ")
        if option == "help":
            help()
        elif option == "stop":
            break
        else:
            part_split = option.split(";")
            for comanda in part_split:
                comanda_split = comanda.split(',')
                if comanda_split[0] == "add":
                    try:
                        lista=adauga_rezervare(comanda_split[1], comanda_split[2], comanda_split[3], comanda_split[4], comanda_split[5], lista)
                    except ValueError as ve:
                        print("eroare {}".format(ve))
                        return lista
                elif comanda_split[0] == "delete":
                    lista=sterge_rezervare(comanda_split[1], lista)
                elif comanda_split[0] == "update":
                    try:
                        lista=modifica_rezervare(comanda_split[1], comanda_split[2], comanda_split[3], comanda_split[4], comanda_split[5], lista)
                    except ValueError as ve:
                        print("eroare {}".format(ve))
                        return lista
                elif comanda_split[0] == "showall":
                    ui_show_all(lista)
                elif comanda_split[0] == "Help":
                    help()