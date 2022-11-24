from data import bevetelekOsszeg, bevetelMegnevezes, kiadadOsszeg, kiadasMegnevezes
from os import system
kiadas='kiadasok.txt'
bevetel='bevetelek.txt'

def menu():
    system('cls')
    print('MENÜ:')
    print('\t 0 - Kilépés')
    print('\t 1 - Kiadások')
    print('\t 2 - Bevételek')
    print('\t 3 - Új kiadás felvétele')
    print('\t 4 - Új bevétel felvétele')
    print('\t 5 - Kiadás törlése')
    print('\t 6 - Bevétel törlése')
    print('\t 7 - Kiadások összesen')
    print('\t 8 - Bevételek összesen')