from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import trecere_rezervare_upperclass, ieftinire_procentaj_checkin, pret_maxim_per_clasa, \
    ordonare_descrescatoare_pret


def ui_adauga_rezervare(l):
    try:
        id=input("Dati id-ul: ")
        nume=input("Dati numele: ")
        clasa=input("Dati clasa: ")
        pret=float(input("Dati pretul: "))
        checkin=input("Dati checkinul: ")
        return adauga_rezervare(id, nume, clasa, pret, checkin, l)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return l

def ui_sterge_rezervare(l):
    id=input("Dati id-ul rezervarii pe care doriti sa o stergeti: ")
    return sterge_rezervare(id,l)

def ui_modifica_rezervare(l):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati numele nou al rezervarii de modificat: ")
    clasa = input("Dati clasa noua a rezervarii de modificat: ")
    pret = float(input("Dati pretul nou al rezervarii de modificat: "))
    checkin = input("Dati checkinul nou al rezervarii de modificat: ")
    return modifica_rezervare(id, nume, clasa, pret, checkin, l)

def ui_schimbare_clasa(l):
    sub_nume=input("Dati numele clientului a carui rezervare doriti sa o modificati: ")
    noua_clasa=input("Dati noua clasa la care sa fie trecuta rezervarea clientului: ")
    return  trecere_rezervare_upperclass(sub_nume, noua_clasa, l)
def ui_ieftinire_procentaj_checkin(l):
    procentaj=float(input("Dati procentajul cu care sa se ieftineasca pretul rezervarii cu checkinul facut: "))
    return ieftinire_procentaj_checkin(procentaj, l)
def ui_pret_maxim_per_clasa(l):
    clasa_data=input("Dati clasa pentru care doriti sa stiti pretul maxim al rezervarii: ")
    return pret_maxim_per_clasa(clasa_data, l)
def ui_ordonare_descrescatoare(l):
    return ordonare_descrescatoare_pret(l)


def ui_show_all(l):
    for rezervare in l:
        print(to_string(rezervare))


def run_menu(l):
    while True:
        print("1. Adauga rezervare: ")
        print("2. Sterge rezervare: ")
        print("3. Mofidica rezervare: ")
        print("4. Schimbarea clasei de zbor la o rezervare cu un nume dat: ")
        print("5. Ieftinirea cu un procentaj dat a pretului unei rezervari cu checkinul facut: ")
        print("6. Determinarea pretului maxim pentru fiecare clasa: ")
        print("7. Ordonarea rezervarilor descrescator dupa pret: ")
        print("8. Afisarea sumelor preturilor dupa nume: ")
        print("a. Afiseaza toate rezervarile")  # show all

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = ui_adauga_rezervare(l)
        elif optiune == "2":
            l = ui_sterge_rezervare(l)
        elif optiune == "3":
            l = ui_modifica_rezervare(l)
        elif optiune == "4":
            l = ui_schimbare_clasa(l)
        elif optiune == "5":
            l = ui_ieftinire_procentaj_checkin(l)
        elif optiune == "6":
            l = ui_pret_maxim_per_clasa(l)
        elif optiune == "7":
            l = ui_ordonare_descrescatoare(l)

        #elif optiune == "8":

        elif optiune == "a":
            ui_show_all(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")