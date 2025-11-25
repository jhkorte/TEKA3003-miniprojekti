from viite import Viite

class ViiteRepository:
    def luoViite(self):
        uusi_viite = Viite()
        
        entryType = input("Anna entry type\n")
        uusi_viite.entryType = entryType

        key = input("Anna viitteen avain\n")
        uusi_viite.key = key
        
        author = input("Anna authorit\n")
        uusi_viite.author = author
        
        year = input("Anna vuosi\n")
        uusi_viite.year = year

        title = input("Anna julkaisuvuosi\n")
        uusi_viite.title = title

        booktitle = input("Anna booktitle\n")
        uusi_viite.booktitle = booktitle

        journal = input("Anna journal\n")
        uusi_viite.journal = journal

        volume = input("Anna volume\n")
        uusi_viite.volume = volume

        pages = input("Anna pages\n")
        uusi_viite.pages = pages

        publisher = input("Anna publisher\n")
        uusi_viite.publisher = publisher

        uusi_viite.viiteToString()
        