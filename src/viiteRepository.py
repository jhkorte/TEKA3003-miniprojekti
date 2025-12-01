from viite import Viite
from pathlib import Path
import json

class ViiteRepository:
    def __init__(self, data_file_name="viitteet.json"):
        self.data_file_name = data_file_name
        self.viitteet = self.lataaViitteetTiedostosta()


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
        return uusi_viite



    def tulostaViitteetListasta(self):
        if len(self.viitteet) < 1:
            print("Ei tallennettuja viitteitä"); print()
            return

        print("Tulostetaan tallennetut viitteet"); print()
        for viite in self.viitteet:
            print(viite)


    def tallennaViitteetTiedostoon(self):
        with open("references.bib", "w") as f:
            for viite in self.viitteet:
                f.write(str(viite))
                f.write("\n")


    def tallennaViitteetJsoniin(self):
        try:
            viite_dictionary = [viite.toDictionary() for viite in self.viitteet]

            with open(self.data_file_name, "w", encoding="utf-8") as f:
                json.dump(viite_dictionary, f, indent=4)

            print(f"\nViitteet tallennettu tiedostoon: {self.data_file_name}.")
        except Exception as e:
            print(f"\nTallennus epäonnistui: {e}")


    def lataaViitteetTiedostosta(self):
        data_file = Path(self.data_file_name)

        if not data_file.exists():
            return []

        try:
            with open(data_file, "r", encoding="utf-8") as f:
                viite_dictionary = json.load(f)

                viitteet = [Viite.fromDictionary(d) for d in viite_dictionary]
                print(f"Ladattu {len(viitteet)} viitettä tiedostosta {self.data_file_name}.\n")
                return viitteet

        except Exception as e:
            print(f"Lataus epäonnistui: {e}")
            return []


    def Filtteroi(self):
        tyypit = [
                "entryType", 
                "key", 
                "author", 
                "year", 
                "title", 
                "booktitle", 
                "journal", 
                "volume", 
                "pages", 
                "publisher"
                ]
        tyyppi = ""
        while tyyppi not in tyypit:
            tyyppi = input("Anna haku tyyppi esim. author\n"); print()
        hakusana = input("Anna hakusana\n"); print()

        print("Löydetyt viitteet:\n")
        for viite in self.viitteet:
            attribute_value = getattr(viite, tyyppi)
            if hakusana in attribute_value:
                print(str(viite))
                print("--------------------------------------------------------------------")


