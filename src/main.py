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

    # Tallennetaan ViiteRepositoryn viite muuttujaan
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
       
        # Kysytään komento käyttäjältä
        response = input("Anna komento \n").strip().lower(); print()

        # Tallennetaan ja poistutaan ohjelmasta
        if response == "quit":
            repo.tallennaViitteetJsoniin()
            repo.tallennaDropboxiin()
            break

        # Luo uuden DOI viitten
        if response == "doi":
            uusiViite = repo.tallennaViiteDoi()
            repo.viitteet.append(uusiViite)
            repo.tallennaViitteetJsoniin()

        # Luo uuden viitten
        if response == "new":
            repo.viitteenLuontiKysely()
            
        # Tulostaa viitteet
        if response == "print":
            repo.tulostaViitteetListasta()

        # Luo bibtex tiedoston ja liisää viitteet sinne
        if response == "luo":
            repo.tallennaViitteetTiedostoon()

        # Hae viite hakusanan perusteella
        if response == "hae":
            repo.Filtteroi()

        # Tallentaa viitteen tiedostoon ja lähettää sen dropboxiin
        if response =="dropbox":
            repo.tallennaDropboxiin()

        # Tulostaa käyttöohjeet käyttäjälle
        if response == "help":
            print(commands)


if __name__ == "__main__":
    main()
