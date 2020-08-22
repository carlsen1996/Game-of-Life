"""
Denne klassen beskriver cellen. Den har mulighet for å endre statusen til cellen og brukes til å
vise hvordan den skal vises på skjermen.
"""
class Celle:
    def __init__(self):
        self._doed = True
    def settDoed(self): #Denne brukes for å gjøre om fra levende til død
        self._doed = True
    def settLevende(self): #Denne brukes for å gjøre om fra død til levende
        self._doed = False
    def erLevende(self): #Denne brukes til å vise om den er levende
        return not self._doed
    def hentStatusTegn(self): #Her setter den tegn som viser statusen på cellen
        if self._doed == False:
            return("O") #Hvis levende
        else:
            return(".") #Hvis død
