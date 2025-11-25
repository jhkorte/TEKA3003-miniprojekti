from viiteRepository import ViiteRepository

def main():
    repo = ViiteRepository()

    while True:
        print("Tama on kayttoliittymasovellus viitteiden hallintaan bibtex muodossa \nMahdolliset komennot: \n New: Lisaa uusi viite \n Quit: Tallenna ja päätä ohjelman käyttö \n")
        response = input("Anna komento \n").strip().lower()  
        print(response + "\n")
        if response == "quit":
            break

        if response == "New":
            repo.luoViite()

if __name__ == "__main__":
    main()