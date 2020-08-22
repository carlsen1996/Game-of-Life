"""
Her skal vi bruke en del metoder for å skrive ut hvordan brettet skal skrives ut og hva som
skal gjøres før brettet oppdateres til neste generasjon.
"""
from random import randint
from celle import Celle

class Spillbrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._hovedListe = []
        self._celleOrdbok = {}
        self._generasjon = 0 #Holder styr på hvilken generasjon vi befinner oss i
        for i in range(self._rader): #Her lager vi en nøstet liste for å lage et rutenett
            kolonneListe = []
            for j in range(self._kolonner):
                kolonneListe.append(Celle())
            self._hovedListe.append(kolonneListe)
        self.generer()
        self.celleOrdbokF()




    def tegnBrett(self): #Denne brukes til å skrive ut alt vi ser på skjermen
        print("\n" * 30) #Printer ut 30 nye linjer for estetikken
        for rad in self._hovedListe:
            for celle in rad:
                print(celle.hentStatusTegn(), end="") #Gjør så vi ser om cellen er død eller levende
            print()
        print("Nåværende generasjon:", self._generasjon, "Antall levende celler:", self.finnAntallLevende()) #skriver ut info


    def oppdatering(self): #Denne finner det vi trenger å vite til neste oppdatering
        listeSettDoed = []
        listeSettLevende = []
        for celle in self._celleOrdbok.keys(): #denne løkken legger celler som skal død og celler som skal gjennoplives inn i hver sin liste
            if not celle.erLevende() and self.finnAntallLevendeNabo(celle) == 3:
                listeSettLevende.append(celle)
            elif celle.erLevende() and self.finnAntallLevendeNabo(celle) not in range(2,4):
                listeSettDoed.append(celle)
        for celle in listeSettDoed: #Dreper cellene i listen
            celle.settDoed()
        for celle in listeSettLevende: #Gjennopliver cellene i listen
            celle.settLevende()
        self._generasjon += 1 #Legger til en så vi kan vite hvilken generasjon vi er i

    def celleOrdbokF(self): #Lagrer naboene til cellene inn i en ordbok så vi vet hvor mange den har og hvor de er
        for r in range(self._rader):
            for k in range(self._kolonner):
                self._celleOrdbok[self._hovedListe[r][k]] = self.finnNabo(r, k)

    def finnAntallLevendeNabo(self, celle): #Finner ut hvor mange av naboene til cellen som er levende
        levende = 0
        for e in self._celleOrdbok[celle]: #Legger til en for hver levende nabo
            if e.erLevende():
                levende += 1
        return levende

    def finnAntallLevende(self): #Finner ut hvor mange levende celler det er på brettet
        levende = 0
        for rad in self._hovedListe:
            for celle in rad:
                if celle.erLevende(): #Sjekker gjennom alle cellene i listen over dem mot funksjonen som sjekker om de er levende
                    levende += 1
        return levende

    def generer(self): #Denne genererer så det er tilfeldig hvor de levende cellene oppstår når man starter brettet
        for rad in self._hovedListe:
            for celle in rad:
                if randint(0, 2) == 0: #det skal være 1/3 sjanse for at cellene starter som levende på starten
                    celle.settLevende()


    def finnNabo(self, x, y): #Denne her skal finne ut hvor naboene er
        naboer = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x or j != y:
                    if i >= 0 and j >= 0 and i < self._rader and j < self._kolonner: #gjør så vi ikke legger inn hovedcellen i listen over naboer
                        naboer.append(self._hovedListe[i][j]) #Legger hver nabo inne i en liste
        return naboer
