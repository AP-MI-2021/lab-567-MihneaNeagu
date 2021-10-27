def creeaza_rezervare(id, nume,clasa,pret,checkin):
    '''
    creeaza un dictionar pentru rezervarea de avion
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return:
    '''

    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }

def get_id(rezervare):
    '''
    da id-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: id-ul rezervarii
    '''
    return rezervare["id"]

def get_nume(rezervare):
    return rezervare["nume"]

def get_clasa(rezervare):
    return rezervare["clasa"]

def get_pret(rezervare):
    return rezervare["pret"]

def get_checkin(rezervare):
    return rezervare["checkin"]

def to_string(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )



