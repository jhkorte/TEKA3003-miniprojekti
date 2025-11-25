def main():
    while True:
        print("Tama on kayttoliittymasovellus viitteiden hallintaan bibtex muodossa \nMahdolliset komennot: \n New: Lisaa uusi viite \n")
        response = input("laita quit \n")
        print(response + "\n")
        if response == "quit":
            break


if __name__ == "__main__":
    main()