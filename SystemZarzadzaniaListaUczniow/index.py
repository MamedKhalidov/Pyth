plik = open("uczniowie.txt", "r", encoding="utf-8")
uczniowie = plik.readlines()
plik.close()

for i in range(len(uczniowie)):
    uczniowie[i] = uczniowie[i].strip()

    while True:
        print("1. Wyswietl uczniow")
        print("2. Posortuj uczniow")
        print("3. Usun ucznia")
        print("4. Zakoncz")

        wybor = input("wybierz opcje: ")
        
        if wybor == "1":
            for i in range(len(uczniowie)):
                print(i + 1, uczniowie[i])

        elif wybor == "2":
                uczniowie.sort()
                print("Posortowano liste")

        elif wybor == "3":
            for i in range(len(uczniowie)):
                print(i + 1, uczniowie[i])

            numer = int(input("Podaj numer ucznia: "))

            if numer >= 1 and numer <= len(uczniowie):
                uczniowie.pop(numer - 1)
                print("usunieto ucznia")
            else:
                print("nie ma takiego numeru")

        elif wybor == "4":
            print("koniec programu")
            break
        else:
            print("\nwybierz liczbe od 1 do 4")
            