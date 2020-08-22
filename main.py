"""
Dette her skal brukes til å kjøre programmet.
"""
from spillbrett import Spillbrett

def main():
    x = "f" #Denne gjør så vi kan starte en whileløkke så programmet kan starte
    dimensjonA = int(input("Oppgi dimensjon x: ")) #Definerer hvor stort brettet skal bli
    dimensjonB = int(input("Oppgi dimensjon y: "))
    a = Spillbrett(dimensjonA, dimensjonB) #Åpner spillbrettet og gjør det klart
    while x != "q": #Løkken som gjør at vi kan kjøre det over flere generasjoner
        a.tegnBrett() #Den starter med å hente informasjon ut fra spillbrett for å vise frem og fortsetter med å hente ut fra oppdatering etterhvert som spillet fortsetter
        a.oppdatering() #Brukes til å finne ut hva som skal skje i neste generasjon
        x = input("Trykk enter for å fortsette eller q for å avslutte: ") #Spør om vi skal fortsette eller avslutte spillet

main()
