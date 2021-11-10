from Tests.test_CRUD import test_sterge_rezervare, test_modifica_rezervare
from Tests.test_domain import test_rezervare
from Tests.tests_functionalitati import test_trecere_rezervare_upperclass, test_ieftinire_procentaj_checkin, \
    test_pret_maxim_per_clasa, test_ordonare_descrescatoare_pret, test_suma_preturi_nume, test_undo_redo


def run_all_tests():
    test_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_trecere_rezervare_upperclass()
    test_ieftinire_procentaj_checkin()
    test_pret_maxim_per_clasa()
    test_ordonare_descrescatoare_pret()
    test_suma_preturi_nume()
    test_undo_redo()
