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
    print('ÚJ KIADÁS')
    ujKiadasNev=input('Nevezze meg a kiadást: ')
    ujKiadasOssz=input('Adja meg az összeget: ')
    kiadasokNev.append(ujKiadasNev)
    kiadasokOssz.append(ujKiadasOssz)
    kiadasMentes(ujKiadasNev)
    input('Sikeresen hozzá adva a listához')

def kiadasMentes(ujKiadas):
    file1=open(kiadas,'a',encoding='utf-8')
    file1.write(f'\n{ujKiadas[0]}: {ujKiadas[1]} Ft')
    file1.close()

def ujBevtel():
    system('cls')
    print('ÚJ BEVÉTEL')
    ujBevtelNev=input('Nevezze meg a bevételt: ')
    ujBevetelOssz=input('Adja meg az összeget: ')
    bevetelekNev.append(ujBevtelNev)
    bevetelekOssz.append(ujBevetelOssz)
    bevetelMentes(ujBevtelNev)
    input('Sikeresen hozzá adva a listához')

def bevetelMentes():
    file2=open(bevetel,'a',encoding='utf-8')
    file2.write(f'\n{ujBevtel[0]}: {ujBevtel[1]} Ft')
    file2.close()

def kiadasTorles():
    system('cls')
    print('KIADÁS TÖRLÉSE')
    KiadasKiir()
    toroltK=input('\nMelyik kiadást töröljük?: ')
    kiadasokNev.pop(toroltK-1)
    kiadasokOssz.pop(toroltK-1)
    mentKTorl()
    input('Sikeres törlés')

def mentKTorl():
    file1=open(kiadas,'w',encoding='utf-8')
    for i in range(len(kiadasokNev)):
        if i>0:
            file1.write('\n')
        file1.write(f'{kiadasokNev[i]}: {kiadasokOssz[i]} Ft')
    file1.close()

def bevetelTorles():
    system('cls')
    print('BEVÉTEL TÖRLÉSE')
    BevetelKiir()
    toroltB=input('\nMelyik bevételt töröljük?: ')
    bevetelekNev.pop(toroltB-1)
    bevetelekOssz.pop(toroltB-1)
    mentBTorl()
    input('Sikeres törlés')

def mentBTorl():
    file2=open(bevetel,'w',encoding='utf-8')
    for i in range(len(bevetelekNev)):
        if i>0:
            file2.write('\n')
        file2.write(f'{bevetelekNev[i]}: {bevetelekOssz[i]} Ft')
    file2.close()