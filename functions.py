from data import *
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

def KiadasBetoltes():
    file1=open(kiadas, 'r', encoding='utf-8')
    for row in file1:
        darabolt1=row.strip().split(';')
        kiadasok.append(darabolt1[0])
    file1.close()

def BevetelBetoltes():
    file2=open(bevetel, 'r', encoding='utf-8')
    for row in file2:
        darabolt2=row.strip().split(';')
        bevetelek.append(darabolt2[0])
    file2.close()

def BevetelKiir():
    for i in range(0,len(bevetelek)):
        print(f'\t{bevetelek[i]} Ft')