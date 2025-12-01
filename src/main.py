from viiteRepository import ViiteRepository

def main():
    repo = ViiteRepository()

    while True:
        print("Tama on kayttoliittymasovellus viitteiden hallintaan bibtex muodossa \nMahdolliset komennot: \
              \nNew: Lisaa uusi viite \nPrint: Tulostaa tallennetut viitteet\nLuo: Luo bibtex muotoisen tiedoston ja lisää luodut viitteet sinne  \
               \nQuit: Tallenna ja päätä ohjelman käyttö \nHae: hae viitteitä\n")
        response = input("Anna komento \n").strip().lower(); print()

        if response == "quit":
            repo.tallennaViitteetJsoniin()
            break

        if response == "new":
            repo.viitteenLuontiKysely()
        
        if response == "print":
            repo.tulostaViitteetListasta()
        
        if response == "luo":
            repo.tallennaViitteetTiedostoon()

        if response == "hae":
            repo.Filtteroi()
            

if __name__ == "__main__":
    main()
