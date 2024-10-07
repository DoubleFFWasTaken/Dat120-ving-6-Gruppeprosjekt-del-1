#Class_access_files

import csv


# en class er bare en funksjon med funksjoner inni
class RuneData:
    #self er bare et vanlig variabelnavn, basically det det gjør er å call-e på seg selv forklaring under
    def __init__(self, filnavn): #init betyr initialize, altså "start med:" så hver gang du vil hente noe fra klassen så gjør den følgende operasjoner:
        self.filnavn    = filnavn
        #står egentlig "RuneData skal starte med å fortelle seg selv at den skal bruke variabelen filnavn når enn filnavn blir nevnet senere" 
        self.tid        = []
        self.trykk_bar  = []
        self.trykk_abs  = []
        self.temparatur = []
        self.LesData()  
        #så må du manuelt spør om resten av koden

    def LesData(self):
        # Åpner og leser rune sin fil:
        with open(self.filnavn) as data_rune:
            reader = csv.reader(data_rune, delimiter=';')
            for row in reader:
                self.tid       .append(row[1])
                self.trykk_bar .append(row[2])
                self.trykk_abs .append(row[3])
                self.temparatur.append(row[4])

    #Disse funksjonene returnerer da listene vi ser etter, hvis ikke så bare eksisterer de tomt
    #skal forklare senere hvordan vi får tak i de
    def runeTemp(self):
        return self.temparatur
    
    def runeTid(self):
        return self.tid

    def runeTrykkBar(self):
        return self.trykk_bar

    def runeTrykkAbs(self):
        return self.trykk_abs
    

class SolaData: 
    def __init__(self, filnavn):
        self.filnavn = filnavn
        self.tid     = []
        self.trykk   = []
        self.temp    = []
        self.LesData()  

    def LesData(self):
        with open(self.filnavn) as data_Sola:
            reader = csv.reader(data_Sola, delimiter=';')
            for row in reader:
                #jeg må egentlig lage en loop slik at rune og sola har like lange lister, nå er de 74 og 20222 lange :)
                self.tid  .append(row[2])
                self.temp .append(row[3])
                self.trykk.append(row[4])

    def solaTid(self):
        return self.tid

    def solaTrykk(self):
        return self.trykk

    def solaTrykkAbs(self):
        return self.trykk
    