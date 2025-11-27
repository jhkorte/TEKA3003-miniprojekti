from viiteRepository import ViiteRepository

def main():
    repo = ViiteRepository()

    while True:
        print("Tama on kayttoliittymasovellus viitteiden hallintaan bibtex muodossa \nMahdolliset komennot: \
              \nNew: Lisaa uusi viite \nPrint: Tulostaa tallennetut viitteet\n"  \
               "Quit: Tallenna ja päätä ohjelman käyttö \n")
        response = input("Anna komento \n").strip().lower(); print()

        if response == "quit":
            break

        if response == "new":
            repo.viitteenLuontiKysely()
        
        if response == "print":
            repo.tulostaViitteetListasta()
        

if __name__ == "__main__":
    main()