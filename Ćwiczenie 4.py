def cena_biletu(wiek, cena_podstawowa = 30):
    if wiek < 12:
        return 15
    elif wiek < 18:
        return 20:
    else:
        return cena_podstawowa

wiek = int(input("Podaj wiek: "))
print("Cena biletu: ", cena_biletu(wiek))