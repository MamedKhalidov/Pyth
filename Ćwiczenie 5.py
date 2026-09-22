def produkt(nazwa: str, cena: float, sztuki: int):
    wartosc = cena * sztuki
    return wartosc
    
nazwa = input("Podaj nazwe produktu: ")
cena = float(input("Podaj cene: "))
sztuki = int(input("Podaj liczbe sztuki: "))

wynik = produkt(nazwa=nazwa, cena=cena, sztuki=sztuki)

print("Produkt: ", nazwa)
print("Wartosc: ", wynik)
