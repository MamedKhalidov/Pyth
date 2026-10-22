nazwa_pliku = "dane.txt"

while True:
    print("1 Odczyt danych")
    print("2 Dopisywanie danych")
    print("3 Nadpisywanie pliku")
    print("4 Czyszczenie pliku")
    print("5 Wyszukiwanie tekstu")
    print("6 Numerowanie linii")
    print("7 Zakończenie programu")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        try:
            with open(nazwa_pliku, "r", encoding="utf-8") as plik:
                print(plik.read())
        except FileNotFoundError:
            print("Plik nie istnieje.")

    elif wybor == "2":
        tekst = input("Podaj tekst: ")
        with open(nazwa_pliku, "a", encoding="utf-8") as plik:
            plik.write(tekst)

    elif wybor == "3":
        tekst = input("Podaj nowy tekst: ")
        with open(nazwa_pliku, "w", encoding="utf-8") as plik:
            plik.write(tekst)

    elif wybor == "4":
        open(nazwa_pliku, "w").close()
        print("Plik wyczyszczony.")

    elif wybor == "5":
        tekst = input("Czego szukasz? ")
        try:
            with open(nazwa_pliku, "r", encoding="utf-8") as plik:
                liczba = plik.read().count(tekst)
            print("Liczba wystąpień:", liczba)
        except FileNotFoundError:
            print("Plik nie istnieje.")

    elif wybor == "6":
        try:
            plik = open(nazwa_pliku, "r", encoding="utf-8")
                for linia in plik:
        print(linia, end="")
    plik.close()

except FileNotFoundError:
    print("Plik nie istnieje.")
    elif wybor == "7":
        print("Koniec programu.")
        break

    else:
        print("Błędna opcja.")