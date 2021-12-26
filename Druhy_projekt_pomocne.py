import random
import ast

def nacteni_souboru(soubor: str, mode: str)-> tuple:
    file = open(soubor,mode) # open file
    data1 = file.read() # read file in string
    file.close() # close file
    data2 = ast.literal_eval(data1) #change file from string to dict
    pocet_pokusu = data2['Hra_pocet_pokusu'] # vycteni klice slovniku
    casy_her = data2["casy_her"]# vycteni klice slovniku
    return pocet_pokusu,casy_her,data2

def ulozeni_souboru(soubor:str, mode: str,statistika: dict):
    file = open(soubor, mode)
    file.write(str(statistika))
    file.close()

def statistika_nova(pocet_pokusu: list,pocitadlo_kol: int,cas_hry: float,casy_her: list,statistika: dict)->tuple:
    pocet_pokusu.append(pocitadlo_kol)
    casy_her.append(cas_hry)
    statistika["Hra_pocet_pokusu"] = pocet_pokusu
    statistika["casy_her"] = casy_her
    return statistika, pocet_pokusu, casy_her

def vyhodnoceni(pocet_pokusu,pocitadlo_kol:int,cas_hry:float,casy_her: list):
    oddelovac1 = "-" * 47
    oddelovac2 = "=" * 47
    prumer_pokusy = sum(pocet_pokusu) / len(pocet_pokusu)
    prumer_casy = sum(casy_her)/len(casy_her)
    print(f"It took you {round((cas_hry), 0)} seconds to solve the puzzle.")
    print("Avreage time for a game is: ", round(prumer_casy, 0))
    print(oddelovac1)
    print(f"You needed {pocitadlo_kol} rounds.")
    print("Avreage rounds number of all games is: ", round(prumer_pokusy, 3))
    print( oddelovac2,"THE END. Try it again.".center(len(oddelovac2)),oddelovac2, sep="\n")

def uvadec():
    oddelovac = "-"*47
    uvitani = "Hi there!"
    zprava = """I've generated a random 4 digit number for you.
Let's play a bulls and cows game."""
    print(oddelovac,uvitani,oddelovac,zprava,oddelovac, sep= "\n")

def hrac_hada()-> str:
    oddelovac = "-" * 47
    # Vstup hrace. Hrac zada svuj tip. Funkce kontroluje jestli je vstup ctyrmistny, jestli obsahuje jen cislovky,
    # jestli cislo neyacina nulou, jestli jsou cislice unikatni.
    cislo = input("Enter a number: ")
    while len(cislo) != 4 or not cislo.isdigit() or cislo.startswith("0") or len(cislo) != len(set(cislo)):
        print(oddelovac)
        print("! ! ! Your input is not four digits number or \nstartwith 0 or contains duplications.\nPlease, enter a number again ! ! !")
        print(oddelovac)
        cislo = input("Enter a number: ")
    return cislo

def nahodne_cislo()-> list:
    # vytvori ctyrmistne nahodne unikatni cislo
    seznam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cislo = random.sample(seznam, 4)
    while cislo[0] == 0:
        cislo = random.sample(seznam, 4)
    return cislo

def hodnoceni_hadani(hracovo_cislo: str, hadane_cislo: list )-> tuple:
    cows = 0
    bulls = 0
    for i,n in enumerate(hracovo_cislo):
        for j, m in enumerate(hadane_cislo):
            if int(n) == m:
                cows += 1
            if i == j and int(n) == m:
                bulls += 1
    return cows,bulls

def hraci_kolo(hodnoceni_hadani)-> int:
    oddelovac = "-" * 47
    if hodnoceni_hadani[0] == 1:
        text1 = "Cow"
    else:
        text1 = "Cows"
    if hodnoceni_hadani[1] == 1:
        text2 = "Bull"
    else:
        text2 = "Bulls"
    print(f"{text1} = {hodnoceni_hadani[0]}, {text2} = {hodnoceni_hadani[1]}")
    print(oddelovac)

    if hodnoceni_hadani[0] == 4 and hodnoceni_hadani[1] == 4:
        print("Correct, you've guessed the right number \nin 4 guesses!")
        print(oddelovac)
        postup = 0
    else:
        postup = 1
    return postup


if __name__ == "__main__":
    print(hrac_hada())




