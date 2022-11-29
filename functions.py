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
    return input('Választás: ')

def KiadasBetoltes():
    file1=open(kiadas, 'r', encoding='utf-8')
    for row in file1:
        darabolt1=row.strip().split(';')
        kiadasokNev.append(darabolt1[0])
        kiadasokOssz.append(float(darabolt1[1]))
    file1.close()

def BevetelBetoltes():
    file2=open(bevetel, 'r', encoding='utf-8')
    for row in file2:
        darabolt2=row.strip().split(';')
        bevetelekNev.append(darabolt2[0])
        bevetelekOssz.append(float(darabolt2[1]))
    file2.close()

def BevetelKiir():
    system('cls')
    print('BEVÉTELEK')
    for i in range(0,len(bevetelekNev)):
        print(f'\t{bevetelekNev[i]}: {bevetelekOssz[i]} Ft')
    input()

def KiadasKiir():
    system('cls')
    print('KIADÁSOK')
    for i in range(0,len(kiadasokNev)):
        print(f'\t{kiadasokNev[i]}: {kiadasokOssz[i]} Ft')
    input()

def ujKiadas():
    system('cls')
    print('ÚJ EREDMÉNY')
    bekertMegnevezés=input('Kiadás megnevezése: ')
    bekertOsszeg=input('Összeg: ')  
    kiadasok.append(bekertMegnevezés,bekertOsszeg)      
    #kiadasMentes(bekertMegnevezes,bekertOsszeg)

def kiadasMentes():
    file1=open(kiadas,'a',encoding='utf-8')
    file1.write(f'\n')