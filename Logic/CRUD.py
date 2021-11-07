from Domain.rezervare import creeaza_rezervare, get_id, get_pret


def adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    '''
    Adauga o rezervare in lista
    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:lista de rezervari
    :return:O lista continand vechile rezervari si noua rezervare
    '''
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]

def get_by_id(id,lista):
    '''
    Da elementul din lista cu un id dat
    :param id:
    :param lista:
    :return:rezervarea cu id-ul dat sau None daca nu exista rezervare cu id-ul dat
    '''

    for rezervare in lista:
        if get_pret(rezervare)<0:
            raise ValueError("Pretul nu poate fi mai mic decat 0")
        if get_id(rezervare) == id:
            return rezervare
    return None

def sterge_rezervare(id,lista):
    '''
    sterge rezervarea cu id-ul dat dintr-o lista
    :param id:
    :param lista:
    :return:lista cu rezervari fara rezervarea cu id-ul dat
    '''
    try:
        if get_by_id(id, lista) is None:
            raise ValueError("Id-ul nu exista")
    except TypeError as te:
        print("Error {}".format(te))
        return [rezervare for rezervare in lista if get_id(rezervare) != id]

def modifica_rezervare(id, nume, clasa, pret, checkin, lista):
    '''

    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''
    if get_by_id(id, lista) is None:
        raise ValueError("Id-ul nu exista")
    l_noua=[]
    for rezervare in lista:
        if get_id(rezervare)==id:
            rezervare_noua=creeaza_rezervare(id, nume, clasa, pret, checkin)
            l_noua.append(rezervare_noua)
        else:
            l_noua.append(rezervare)
    return l_noua
