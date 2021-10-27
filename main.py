from Logic.CRUD import adauga_rezervare
from Tests.test_all import run_all_tests
from UserInterface.console import run_menu

def main():
    run_all_tests()
    lista = []
    lista = adauga_rezervare("1", "Messi", "economy", 25, "nu ", lista)
    lista = adauga_rezervare("2", "Ronaldo", "business", 4000 , "da", lista)
    lista = adauga_rezervare("3", " Neymar", "economy plus", 800, "da", lista)
    lista = adauga_rezervare("4", "Mbappe", "business", 3200, "da", lista)
    lista= adauga_rezervare("5", "Haaland", "economy plus", 3000, "nu", lista)
    run_menu(lista)

main()
'''
Documentatie organizatorica(platforma de organizare a proiectului)
link:
https://app.asana.com/0/1201256849044949/1201256849044949
'''