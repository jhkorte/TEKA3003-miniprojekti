class Viite:
    def __init__(self, entryType=None, key=None, author=None, year=None, 
                 title=None, booktitle=None, journal=None, volume=None, 
                 pages=None, publisher=None):
        self.entryType = entryType
        self.key = key
        self.author = author
        self.year = year
        self.title = title
        self.booktitle = booktitle
        self.journal = journal
        self.volume = volume
        self.pages = pages
        self.publisher = publisher


    def __str__(self):
        
        output = f"@{self.entryType}{{{self.key},\n"
        
        if self.author:
            output += f"    author = {{{self.author}}},\n"
            
        if self.title:
            output += f"    title = {{{self.title}}},\n"
            
        if self.year:
            output += f"    year = {{{self.year}}},\n"
            
        if self.booktitle:
            output += f"    booktitle = {{{self.booktitle}}},\n"
            
        if self.journal:
            output += f"    journal = {{{self.journal}}},\n"
            
        if self.volume:
            output += f"    volume = {{{self.volume}}},\n"
            
        if self.pages:
            output += f"    pages = {{{self.pages}}},\n"
            
        if self.publisher:
            output += f"    publisher = {{{self.publisher}}},\n"

        output += "}"
        
        return output
        

        
    def toDictionary(self):
        return self.__dict__


    @classmethod
    def fromDictionary(cls, data):
        return cls(**data)