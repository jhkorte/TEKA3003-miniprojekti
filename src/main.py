"""
main moduuli viitteiden hallintaan.
"""
from viiteRepository import ViiteRepository
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    """
    main funktio viitteiden hallintaan.
    """
    
    repo = ViiteRepository()
    
    commands = """Mahdolliset komennot:
  New:     Lisää uusi viite
  Print:   Tulosta tallennetut viitteet
  Hae:     Hae viitteitä
  Luo:     Luo .bib-tiedosto
  Doi:     Lisää viite DOI-tunnisteella
  Dropbox: Tallenna tietokanta verkkoon
  Help:    Tulostaa komennot
  Quit:    Tallenna ja lopeta
    """
    print("Tämä on käyttöliittymäsovellus viitteiden hallintaan bibtex muodossa")
    print(commands)

    while True:
        
        response = input("Anna komento \n").strip().lower(); print()

        if response == "quit":
            repo.tallennaViitteetJsoniin()
            repo.tallennaDropboxiin()
            break

        if response == "doi":
            uusiViite = repo.tallennaViiteDoi()
            repo.viitteet.append(uusiViite)
            repo.tallennaViitteetJsoniin()

        if response == "new":
            repo.viitteenLuontiKysely()
            

        if response == "print":
            repo.tulostaViitteetListasta()

        if response == "luo":
            repo.tallennaViitteetTiedostoon()

        if response == "hae":
            repo.Filtteroi()

        if response =="dropbox":
            repo.tallennaDropboxiin()

        if response == "help":
            print(commands)


if __name__ == "__main__":
    main()
