from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, get_by_id, sterge_rezervare, modifica_rezervare


def test_adauga_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)

    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "Obama"
    assert get_clasa(get_by_id("1", lista)) == "business"
    assert get_pret(get_by_id("1", lista)) == 900
    assert get_checkin(get_by_id("1", lista)) == "da"

def test_sterge_rezervare():
    lista=[]
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)
    lista = adauga_rezervare("2", "Trump", "business", 1500, "nu", lista)

    lista=sterge_rezervare("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

def test_modifica_rezervare():
    lista=[]
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)
    lista = adauga_rezervare("2", "Trump", "business", 1500, "nu", lista)

    lista=modifica_rezervare("1", "Ronaldo", "business", 4000, "da", lista)

    rezervare_updated=get_by_id("1" ,lista)
    assert get_id(rezervare_updated)=="1"
    assert get_nume(rezervare_updated)=="Ronaldo"
    assert get_clasa(rezervare_updated)=="business"
    assert get_pret(rezervare_updated)==4000
    assert get_checkin(rezervare_updated)=="da"

    rezervare_not_updated = get_by_id("2", lista)
    assert get_id(rezervare_not_updated) == "2"
    assert get_nume(rezervare_not_updated) == "Trump"
    assert get_clasa(rezervare_not_updated) == "business"
    assert get_pret(rezervare_not_updated) == 1500
    assert get_checkin(rezervare_not_updated) == "nu"







