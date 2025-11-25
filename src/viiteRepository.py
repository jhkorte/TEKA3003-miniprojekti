from viite import Viite

class ViiteRepository:
    def luoViite(self):
        entryType = input("Anna entry type\n")

        uusi_viite = Viite(entryType)
        uusi_viite.viiteToString()
        