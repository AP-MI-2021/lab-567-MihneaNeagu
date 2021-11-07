from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import trecere_rezervare_upperclass, ieftinire_procentaj_checkin, pret_maxim_per_clasa, \
    ordonare_descrescatoare_pret, suma_preturi_nume


def ui_adauga_rezervare(l, undo_list, redo_list):
    try:
        id=input("Dati id-ul: ")
        nume=input("Dati numele: ")
        clasa=input("Dati clasa: ")
        pret=float(input("Dati pretul: "))
        checkin=input("Dati checkinul: ")
        rezultat= adauga_rezervare(id, nume, clasa, pret, checkin, l)
        undo_list.append(l)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Error: {}".format(ve))
        return l

def ui_sterge_rezervare(l,undo_list, redo_list):
    try:
        id=input("Dati id-ul rezervarii pe care doriti sa o stergeti: ")
        rezultat = sterge_rezervare(id, l)
        undo_list.append(l)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Error: {}".format(ve))
        return l

def ui_modifica_rezervare(l, undo_list, redo_list):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati numele nou al rezervarii de modificat: ")
        clasa = input("Dati clasa noua a rezervarii de modificat: ")
        pret = float(input("Dati pretul nou al rezervarii de modificat: "))
        checkin = input("Dati checkinul nou al rezervarii de modificat: ")
        rezultat = modifica_rezervare(id, nume, clasa, pret, checkin, l)
        undo_list.append(l)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Error: {}".format(ve))
        return l

def ui_schimbare_clasa(l, undo_list, redo_list):
    sub_nume=input("Dati numele clientului a carui rezervare doriti sa o modificati: ")
    noua_clasa=input("Dati noua clasa la care sa fie trecuta rezervarea clientului: ")
    rezultat= trecere_rezervare_upperclass(sub_nume, noua_clasa, l)
    undo_list.append(l)
    redo_list.clear()
    return rezultat
def ui_ieftinire_procentaj_checkin(l, undo_list, redo_list):
    try:
        procentaj=int(input("Dati procentajul cu care sa se ieftineasca pretul rezervarii cu checkinul facut: "))
        rezultat= ieftinire_procentaj_checkin(procentaj, l)
        undo_list.append(l)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Error: {}".format(ve))
        return l
def ui_pret_maxim_per_clasa(l, undo_list, redo_list):
    clasa_data=input("Dati clasa pentru care doriti sa stiti pretul maxim al rezervarii: ")
    rezultat= pret_maxim_per_clasa(clasa_data, l)
    undo_list.append(l)
    redo_list.clear()
    return rezultat
def ui_ordonare_descrescatoare(l, undo_list, redo_list):
    rezultat= ordonare_descrescatoare_pret(l)
    undo_list.append(l)
    redo_list.clear()
    return rezultat
def ui_suma_preturi_nume(l, undo_list, redo_list):
    rezultat= suma_preturi_nume(l)
    undo_list.append(l)
    redo_list.clear()
    return rezultat



def ui_show_all(l):
    for rezervare in l:
        print(to_string(rezervare))


def run_menu(l):
    undo_list = []
    redo_list = []
    while True:
        print("1. Adauga rezervare: ")
        print("2. Sterge rezervare: ")
        print("3. Mofidica rezervare: ")
        print("4. Schimbarea clasei de zbor la o rezervare cu un nume dat: ")
        print("5. Ieftinirea cu un procentaj dat a pretului unei rezervari cu checkinul facut: ")
        print("6. Determinarea pretului maxim pentru fiecare clasa: ")
        print("7. Ordonarea rezervarilor descrescator dupa pret: ")
        print("8. Afisarea sumelor preturilor dupa nume: ")
        print("u. Undo: ")
        print("r. Redo: ")
        print("a. Afiseaza toate rezervarile")  # show all

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = ui_adauga_rezervare(l, undo_list, redo_list)
        elif optiune == "2":
            l = ui_sterge_rezervare(l, undo_list, redo_list)
        elif optiune == "3":
            l = ui_modifica_rezervare(l, undo_list, redo_list)
        elif optiune == "4":
            l = ui_schimbare_clasa(l, undo_list, redo_list)
        elif optiune == "5":
            l = ui_ieftinire_procentaj_checkin(l, undo_list, redo_list)
        elif optiune == "6":
            l = ui_pret_maxim_per_clasa(l, undo_list, redo_list)
        elif optiune == "7":
            l = ui_ordonare_descrescatoare(l, undo_list, redo_list)
        elif optiune == "8":
            l = ui_suma_preturi_nume(l, undo_list, redo_list)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(l)
                l= undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(l)
                l = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            ui_show_all(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")