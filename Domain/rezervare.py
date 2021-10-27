def creeaza_rezervare(id, nume,clasa,pret,checkin):
    '''
    creeaza un o lista pentru rezervarea de avion
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return:
    '''
    lista_rez=[id, nume, clasa, pret, checkin]
    return lista_rez



def get_id(lista_rez):
    '''
    da id-ul unei rezervari
    :param rezervare: lista ce contine o rezervare
    :return: id-ul rezervarii
    '''
    return lista_rez[0]

def get_nume(lista_rez):
    return lista_rez[1]

def get_clasa(lista_rez):
    return lista_rez[2]

def get_pret(lista_rez):
    return lista_rez[3]

def get_checkin(lista_rez):
    return lista_rez[4]

def to_string(lista_rez):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        get_id(lista_rez),
        get_nume(lista_rez),
        get_clasa(lista_rez),
        get_pret(lista_rez),
        get_checkin(lista_rez)
    )



