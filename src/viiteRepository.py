from .viite import Viite
from pathlib import Path


class ViiteRepository:
    def __init__(self):
        self.viitteet = []

    def viitteenLuontiKysely(self):
        print("Valitse viitteen tyyppi: inproceedings, article, book")
        print("Palaa takaisin komennolla: peruuta")
        while True:
            komento = input().strip().lower()
            print()
            if komento in ["inproceedings", "article", "book", "peruuta"]:
                break
            print("Väärä komento, valitse tyyppi: inproceedings, article, book")
            print("Palaa takaisin komennolla: peruuta")

        if komento == "inproceedings":
            self.luoViiteInproceedings()

        if komento == "article":
            self.luoViiteArticle()

        if komento == "book":
            self.luoViiteBook()

        if komento == "peruuta":
            return


    def luoViiteInproceedings(self):
        key = input("Anna viitteen avain\n"); print()
        author = input("Anna authorit\n"); print()
        title = input("Anna title\n"); print()
        year = input("Anna year\n"); print()
        booktitle = input("Anna booktitle\n"); print()
        uusi_viite = Viite("Inproceedings", key,author,year,title,booktitle)
        print("Luotu:")
        print(uusi_viite); print()
        self.viitteet.append(uusi_viite)
        self.tallennaViitteetTiedostoon(uusi_viite)


    def luoViiteArticle(self):
        key = input("Anna viitteen avain\n"); print()
        author = input("Anna authorit\n"); print()
        title = input("Anna title\n"); print()
        journal = input("Anna journal\n"); print()
        year = input("Anna year\n"); print()
        volume = input("Anna volume\n"); print()
        pages = input("Anna pages\n"); print()
        uusi_viite = Viite("article", key,author,year,title,None,journal,volume,pages)
        print("Luotu:"); 
        print(uusi_viite); print()
        self.viitteet.append(uusi_viite)
        self.tallennaViitteetTiedostoon(uusi_viite)



    def luoViiteBook(self):
        key = input("Anna viitteen avain\n"); print()
        author = input("Anna author\n"); print()
        title = input("Anna title\n"); print()
        year = input("Anna year\n"); print()
        publisher = input("Anna publisher\n"); print()
        uusi_viite = Viite("book", key,author,year,title,None,None,None,None,publisher)
        print("Luotu:")
        print(uusi_viite); print()
        self.viitteet.append(uusi_viite)
        self.tallennaViitteetTiedostoon(uusi_viite)


    def tulostaViitteetListasta(self):
        if len(self.viitteet) < 1:
            print("Ei tallennettuja viitteitä"); print()
            return
        
        print("Tulostetaan tallennetut viitteet"); print()
        for viite in self.viitteet:
            print(viite)

    def tallennaViitteetTiedostoon(self, reference):
        with open("references.txt", "a") as f:
            f.write(reference.__str__())
            f.write("\n")
            f.write("\n")

