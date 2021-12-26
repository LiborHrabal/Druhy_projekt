from Druhy_projekt_pomocne import *
import time
import ast

def bulls_and_cows():
    # vycteni statistik
    pocet_pokusu,casy_her,statistika = nacteni_souboru("D:/Python/Projects/Druhy_projekt/statistika.txt","r")

    # funkce hry
    uvadec()
    hadane_cislo = nahodne_cislo()
    # print(hadane_cislo)
    postup = 1 # promenna pro vyhodnoceni ukonceni hry
    pocitadlo_kol = 0 # pocitadlo kol potrebnych k uhadnuti cisel
    start_time = time.time() # start mereni casu hry
    while postup:
        postup = hraci_kolo(hodnoceni_hadani(hrac_hada(),hadane_cislo))
        pocitadlo_kol += 1
    stop_time = time.time() # konec mereni casu
    cas_hry = stop_time-start_time

    #Statistika
    statistika,pocet_pokusu,casy_her = statistika_nova(pocet_pokusu,pocitadlo_kol,cas_hry,casy_her,statistika)

    # Ulozeni statistik do souboru
    ulozeni_souboru("D:/Python/Projects/Druhy_projekt/statistika.txt","w",statistika)

    #Ukonceni - vyhodnoceni hry a porovnani
    vyhodnoceni(pocet_pokusu,pocitadlo_kol,cas_hry,casy_her)

if __name__ == "__main__":
    bulls_and_cows()

