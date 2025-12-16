import os
import json
from pathlib import Path
import requests
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError
from dotenv import load_dotenv
from viite import Viite

load_dotenv()
DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")

class ViiteRepository:
    def __init__(self, data_file_name="viitteet.json"):
        self.data_file_name = data_file_name
        self.dropbox_path = f"/{data_file_name}"
        self.dbx = None

        # Nämä kolme muuttujaa tarvitaan Dropboxia varten
        # Tiedot haetaan ympäristömuuttujasta, sitä ei laiteta gittiin
        app_key = os.getenv("DROPBOX_APP_KEY")
        app_secret = os.getenv("DROPBOX_APP_SECRET")
        refresh_token = os.getenv("DROPBOX_REFRESH_TOKEN")

        if app_key and app_secret and refresh_token:
            try:
                self.dbx = dropbox.Dropbox(
                    app_key=app_key,
                    app_secret=app_secret,
                    oauth2_refresh_token=refresh_token
                )
                self.lataaDropboxista()
            except Exception as e:
                print(f"Virhe Dropbox-yhteydessä: {e}")
                print("Käytetään paikallista tiedostoa.")
        else:
            print("Käytetään paikallista tallennusta.")

        self.viitteet = self.lataaViitteetTiedostosta()

    # Luo viitteen käyttäjän antamien tietojen perusteella
    # Käyttäjälle tulostetaan viitteen tyypit, joista käyttäjä valitsee haluamansa tyypin
    # Valitun tyypin mukaan loudaan oikeanlainen viite
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

    # Määritelee ja luo konferenssipuheen julkaisun tai kokoelman viitteen
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
        return uusi_viite

    # Määritelee ja luo artikkelin viitteen
    def luoViiteArticle(self):
        key = input("Anna viitteen avain\n"); print()
        author = input("Anna authorit\n"); print()
        title = input("Anna title\n"); print()
        journal = input("Anna journal\n"); print()
        year = input("Anna year\n"); print()
        volume = input("Anna volume\n"); print()
        pages = input("Anna pages\n"); print()
        uusi_viite = Viite("article", key,author,year,title,None,journal,volume,pages)
        print("Luotu:")
        print(uusi_viite); print()
        self.viitteet.append(uusi_viite)
        return uusi_viite


    # Määritelee ja luo kirjan viitteen
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


    # Tulostaa viitteet, jos niitä on
    def tulostaViitteetListasta(self):
        if len(self.viitteet) < 1:
            print("Ei tallennettuja viitteitä"); print()
            return

        print("Tulostetaan tallennetut viitteet"); print()
        for viite in self.viitteet:
            print(viite)

    # Tallentaa viitteet bib-tiedostoon
    def tallennaViitteetTiedostoon(self):
        with open("references.bib", "w") as f:
            for viite in self.viitteet:
                f.write(str(viite))
                f.write("\n")

    # Tallentaa viitteet Json-tiedostoon
    def tallennaViitteetJsoniin(self):
        try:
            viite_dictionary = [viite.toDictionary() for viite in self.viitteet]

            with open(self.data_file_name, "w", encoding="utf-8") as f:
                json.dump(viite_dictionary, f, indent=4)

            print(f"\nViitteet tallennettu tiedostoon: {self.data_file_name}.")
        except Exception as e:
            print(f"\nTallennus epäonnistui: {e}")

    # Lataa viitteet json-tiedostosta
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

     # Määrittelee hakuun käyvät tagit ja hakee viitteen, käyttäjän syöttämän tagin (tyypin) ja  hakusanan perusteella
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
            tyyppi = input("Anna haku tyyppi esim. author\n").strip().lower(); print()
        hakusana = input("Anna hakusana\n").strip().lower(); print()

        print("Löydetyt viitteet:\n")
        for viite in self.viitteet:
            attribute_value = getattr(viite, tyyppi).strip().lower()
            if hakusana in attribute_value:
                print(str(viite))
                print("--------------------------------------------------------------------")


    #DOI API -rajapinta: https://www.doi.org/doi-handbook/HTML/doi-rest-api.html

    # Tallentaa uuden viitteen doi -osoitteen perusteella
    # Käyttäjältä kysytään doi jonka jälkeen viitteen tiedot haetaan
    def tallennaViiteDoi(self):
        doi = input("Anna doi \n").strip().lower()
        url = f"https://api.crossref.org/works/{doi}"

        response = requests.get(url)
        data = response.json()
        viiteData = data.get("message", {})

        if "type" in viiteData:
            viiteData["entryType"] = viiteData.pop("type")

        if "issued" in viiteData and "date-parts" in viiteData["issued"]:
            viiteData["year"] = viiteData["issued"]["date-parts"][0][0]

        authors_list = viiteData.get("author", [])
        if authors_list:
            viiteData["author"] = " and ".join(
                f"{author.get('family', '')}, {author.get('given', '')}".strip(", ")
                for author in authors_list
            )

        if viiteData.get("author") and viiteData.get("year"):
            first_author = viiteData["author"].split(" and ")[0].split(",")[0]
            viiteData["key"] = f"{first_author}{viiteData['year']}"

        uusiViite = Viite.fromDictionary(viiteData)
        print(str(uusiViite))
        return uusiViite

    # Lataa Dropboxiin tallennetut viitteet
    def lataaDropboxista(self):
        if not self.dbx:
            return
        try:
            self.dbx.files_download_to_file(self.data_file_name, self.dropbox_path)
            print("Lataus Dropboxista onnistui.")
            return True
        except ApiError as e:
            if e.error.is_path() and e.error.get_path().is_not_found():
                print("Tiedostoa ei löytynyt Dropboxista. Käytetään paikallista.\n")
                return False
            else:
                print(f"Virhe ladattaessa Dropboxista: {e}\n")
                return False

    # Tallentaa viitteet Dropboxiin
    def tallennaDropboxiin(self):
        print(f"Tallennetaan {self.data_file_name} Dropboxiin.")
        try:
            with open(self.data_file_name, "rb") as f:
                self.dbx.files_upload(
                    f.read(),
                    self.dropbox_path,
                    mode=WriteMode('overwrite')
                )
            print("Tallennus Dropboxiin onnistui.\n")
            return True
        except Exception as e:
            print(f"Virhe tallennettaessa Dropboxiin: {e}\n")
            return False
