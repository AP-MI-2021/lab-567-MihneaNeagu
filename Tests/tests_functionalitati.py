from Domain.rezervare import get_clasa, get_pret
from Logic.CRUD import adauga_rezervare, get_by_id
from Logic.functionalitati import trecere_rezervare_upperclass, ieftinire_procentaj_checkin, pret_maxim_per_clasa, \
    ordonare_descrescatoare_pret


def test_trecere_rezervare_upperclass():
    lista=[]
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)
    lista = adauga_rezervare("2", "Trump", "economy", 1500, "nu", lista)
    lista= trecere_rezervare_upperclass("Trump", "business", lista)
    rezervare_updated = get_by_id("2", lista)
    rezervare_not_updated= get_by_id("1", lista)
    assert get_clasa(rezervare_updated) == "business"
    assert get_clasa(rezervare_not_updated) == "business"

def test_ieftinire_procentaj_checkin():
    lista=[]
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)
    lista = adauga_rezervare("2", "Trump", "economy", 1500, "nu", lista)
    lista=ieftinire_procentaj_checkin(25, lista)
    rezervare_updated = get_by_id("1", lista)
    rezervare_not_updated=get_by_id("2", lista)
    assert get_pret(rezervare_updated) == 675
    assert get_pret(rezervare_not_updated) == 1500

def test_pret_maxim_per_clasa():
    lista = []
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)
    lista = adauga_rezervare("2", "Trump", "economy", 1500, "nu", lista)
    lista = adauga_rezervare("3", "Messi", "economy", 25, "nu ", lista)
    lista = adauga_rezervare("4", "Ronaldo", "business", 4000, "da", lista)
    lista = adauga_rezervare("5", " Neymar", "economy plus", 800, "da", lista)
    lista = adauga_rezervare("6", "Mbappe", "business", 3200, "da", lista)
    lista = adauga_rezervare("7", "Haaland", "economy plus", 3000, "nu", lista)
    assert pret_maxim_per_clasa("economy", lista) == 1500
    assert pret_maxim_per_clasa("economy plus", lista) == 3000
    assert pret_maxim_per_clasa("business", lista) == 4000

def test_ordonare_descrescatoare_pret():
    lista=[]
    lista = adauga_rezervare("1", "Obama", "business", 900, "da", lista)
    lista = adauga_rezervare("2", "Trump", "economy", 1500, "nu", lista)
    lista = adauga_rezervare("3", "Messi", "economy", 25, "nu ", lista)
    lista = adauga_rezervare("4", "Ronaldo", "business", 4000, "da", lista)
    lista = adauga_rezervare("5", " Neymar", "economy plus", 800, "da", lista)
    lista = adauga_rezervare("6", "Mbappe", "business", 3200, "da", lista)
    lista = adauga_rezervare("7", "Haaland", "economy plus", 3000, "nu", lista)
    assert ordonare_descrescatoare_pret(lista) ==[{'id': '4', 'nume': 'Ronaldo', 'clasa': 'business', 'pret': 4000, 'checkin': 'da'}, {'id': '6', 'nume': 'Mbappe', 'clasa': 'business', 'pret': 3200, 'checkin': 'da'}, {'id': '7', 'nume': 'Haaland', 'clasa': 'economy plus', 'pret': 3000, 'checkin': 'nu'}, {'id': '2', 'nume': 'Trump', 'clasa': 'economy', 'pret': 1500, 'checkin': 'nu'}, {'id': '1', 'nume': 'Obama', 'clasa': 'business', 'pret': 900, 'checkin': 'da'}, {'id': '5', 'nume': ' Neymar', 'clasa': 'economy plus', 'pret': 800, 'checkin': 'da'}, {'id': '3', 'nume': 'Messi', 'clasa': 'economy', 'pret': 25, 'checkin': 'nu '}]



