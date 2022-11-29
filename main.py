from functions import *
from os import system
KiadasBetoltes()
BevetelBetoltes()

valasztas=''
while valasztas!='0':
    valasztas=menu()
    if valasztas=='1':
        BevetelKiir()
    elif valasztas=='2':
        KiadasKiir()
    elif valasztas=='3':
        ujKiadas()
    elif valasztas=='4':
        ujBevtel()
    elif valasztas=='5':
        kiadasTorles()
    elif valasztas=='6':
        pass
    