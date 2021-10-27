from Domain.rezervare import get_nume, creeaza_rezervare, get_id, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare


def trecere_rezervare_upperclass(sub_nume, noua_clasa , lista):
    '''
    Trece rezervarea cu un anumit nume,la o clasa superioara
    :param sub_nume: Numele pe care se va modifica rezervarea
    :param noua_clasa: Noua clasa ce i se va atribui rezervarii
    :param lista: Lista de rezervari
    :return: Noua lista cu rezervarile cu numele cautat ce au acum o noua clasa de zbor
    '''
    lnew=[]
    for rezervare in lista:
        if sub_nume in get_nume(rezervare):
            rezervare_noua=creeaza_rezervare(
                get_id(rezervare),
                get_nume(rezervare),
                noua_clasa,
                get_pret(rezervare),
                get_checkin(rezervare)
            )
            lnew.append(rezervare_noua)
        else:
            lnew.append(rezervare)
    return lnew

def ieftinire_procentaj_checkin(procent, lista):
    '''
    Ieftineste pretul rezervarilor la care checkinul a fost facut
    :param procent: Procentul cu care se va ieftini pretul avionului
    :param lista: lista rezervarilor
    :return: Noua lista cu rezervarile cu pretul ieftinit cu procentajul dat
    '''
    lnew=[]
    for rezervare in lista:
        if get_checkin(rezervare)=="da":
            rezervare_noua=creeaza_rezervare(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                get_pret(rezervare)*(1-procent/100),
                get_checkin(rezervare)
            )
            lnew.append(rezervare_noua)
        else:
            lnew.append(rezervare)
    return lnew

def pret_maxim_per_clasa(clasa_data, lista):
    max_eco=0
    max_eco_plus=0
    max_bus=0
    for rezervare in lista:
        if get_clasa(rezervare) == "economy":
            if get_pret(rezervare)>max_eco:
                max_eco=get_pret(rezervare)
        if get_clasa(rezervare) == "economy plus":
            if get_pret(rezervare)>max_eco_plus:
                max_eco_plus=get_pret(rezervare)
        if get_clasa(rezervare) == "business":
            if get_pret(rezervare)>max_bus:
                max_bus=get_pret(rezervare)

    if clasa_data=="economy":
        return max_eco
    elif clasa_data=="economy plus":
        return max_eco_plus
    elif clasa_data=="business":
        return max_bus
    else:
        return "Clasa inexistenta"

def ordonare_descrescatoare_pret(lista):
    '''
    lpreturi=[]
    for rezervare in lista:
        lpreturi.append(get_pret(rezervare))
    lpreturi.sort(reverse=True)
    return lpreturi
    '''
    print(sorted(lista, key=lambda rezervare: get_pret(rezervare), reverse=True))
    return sorted(lista, key=lambda rezervare:get_pret(rezervare), reverse=True)




