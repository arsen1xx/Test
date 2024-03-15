def inform():
    menu = (True)
    while menu == True:
        name = str(input("Введіть ім'я персонажа: "))
        if name == "Eren" or name == "eren":
            erens = Eren()
            print(f"Name: {erens.nameeren} \nAge: {erens.ageeren} \nTitan: {erens.titaneren} ")
        elif name == "Armin" or name == "armin":
            armins = Armin()
            print(f"Name: {armins.namearmin} \nAge: {armins.agearmin} \nTitan: {armins.titanarmin} ")
        elif name == "Eren Kruger" or name == "erenk kruger":
            erenks = Erenk()
            print(f"Name: {erenks.nameerenk} \nAge: {erenks.ageerenk} \nTitan: {erenks.titanerenk} ")


class Eren:
    nameeren = "Eren Yeager"
    ageeren = 19
    titaneren = "Attack Titan, Founding Titan, War Hammer Titan"
class Armin:
    namearmin = "Armin Arlert"
    agearmin = 19
    titanarmin = "Colossal Titan"
class Erenk:
    nameerenk = "Eren Kruger"
    ageerenk = 55
    titanerenk = "Attack Titan"
class Grisha:
    namegrisha = "Grisha Jaeger"
    agegrisha = 39
    titangrisha = "Attack Titan, Founding Titan"
class Ymir:
    nameymir = "Ymir Fritz"
    ageymir = 23
    titanymir = "Founding Titan"
class Frieda:
    namefrieda = "Frieda Reiss"
    agedina = 18
    titanfrieda = "Attack Titan, Founding Titan"
class Lara:
    namelara = "Lara Tybur"
    agelara = 29
    titanlara = "War Hammer Titan"
class Zeke:
    namezeke = "Zeke Yaeger"
    agezeke = 15
    titanzeke = "Beast Titan"
class Marcel:
    namemarcel = "Marcel Galliard"
    agegalliard = 12
    titanmarcel = "Jaw Titan"
class Ymir:
    nameymir = "Ymir"
    ageymir = 17
    titanymir = "Jaw Titan"
class Porco:
    nameporco = "Porco Galliard"
    ageporco = 19
    titanporco = "Jaw Titan"
class Falco:
    namefalco = "Falco Grice"
    agefalco = 15
    titanfalco = "Jaw Titan"
class Bertholdt:
    nameber = "Bertholdt Hoover"
    ageber = 17
    titanber = "Colossal Titan"
class Reiner:
    namereiner = "Reiner Braun"
    agereiner = 21
    titanreiner = "Armored Titan"
class Annie:
    nameannie = "Annie Leonhart"
    ageannie = 16
    titanannie = "Female Titan"
class Pieck:
    namepieck = "Pieck Finger"
    agepieck = 23
    titanpieck = "Cart Titan"



inform()