
import csv
import datetime as dt

class Data(): 
    def __init__(self, filnavn):

        self.filnavn  = filnavn

        self.solaTemp    = []
        self.solaTid     = []
        self.solaTrykk   = []
    
        self.SaudaTemp   = []
        self.SaudaTid    = []
        self.SaudaTrykk  = []
    
        self.SinnesTemp  = []
        self.SinnesTid   = []
        self.SinnesTrykk = []    

        self.RuneTemp    = []
        self.RuneTid     = []
        self.RuneTrykk   = []

        if self.filnavn == "Filer/temperatur_trykk_met_samme_rune_time_datasett.csv.txt":
            self.Soladata()
        
        if self.filnavn == "Filer/trykk_og_temperaturlogg_rune_time.csv.txt":
            self.Runedata()

        if self.filnavn == "Filer/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt":
            self.Sirdaldata()
  

    def Soladata(self):
            with open(self.filnavn, "r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=';') 
                for i, row in enumerate(reader):
                        
                        if "Navn" in row[0] or "Data" in row[0]:
                            print(f"skipping line {i}, {row[0]}" )
                            continue

                        time_str = row[2]
                        base_time = dt.datetime.strptime(time_str, "%d.%m.%Y %H:%M")
                        self.solaTid.append(base_time)

                        self.solaTemp.append(float(row[3].replace(',', '.'))) 
                        self.solaTrykk.append(float(row[4].replace(',', '.')))
            print(self.solaTrykk[-1])

    def Sirdaldata(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=';') 
                for i, row in enumerate(reader):
                    if "Navn" in row[0] or "Data" in row[0]:
                            print(f"skipping line {i}, {row[0]}" )
                            continue
                    
                    time_str = row[2]
                    base_time = dt.datetime.strptime(time_str, "%d.%m.%Y %H:%M")
                    #Navn;Stasjon;Tid(norsk normaltid);Lufttemperatur;Lufttrykk i havnivå
                    if "Sinnes" in row[0]:

                        self.SinnesTid.append(base_time)

                        self.SinnesTemp.append(float(row[3].replace(',', '.'))) 
                        self.SinnesTrykk.append(float(row[4].replace(',', '.')))


                    if "Sauda" in row[0]:

                        self.SaudaTid.append(base_time)

                        self.SaudaTemp.append(float(row[3].replace(',', '.')))
                        self.SaudaTrykk.append(float(row[4].replace(',', '.')))



    def Runedata(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';') 
            for i, row in enumerate(reader):
                try:
                    time_str = row[0]
                    
                    try:
                        seconds_offset = int(row[1])  
                    except ValueError:
                        print(f"Skipping row {i} due to invalid seconds: {row[1]}")
                        continue

                    if 'am' in time_str.lower() or 'pm' in time_str.lower():
                        base_time = dt.datetime.strptime(time_str, "%m/%d/%Y %H:%M:%S %p")

                    if 'am' not in time_str.lower() and 'pm' not in time_str.lower():
                        base_time = dt.datetime.strptime(time_str, "%m.%d.%Y %H:%M")
                    

                    self.RuneTid.append(base_time)

                    self.RuneTemp.append(float(row[4].replace(',', '.'))) 
                    self.RuneTrykk.append(float(row[3].replace(',', '.')))
                        
                except Exception as e:
                    print(f"Error processing row {i}: {e}")
        



    def Solatemp(self):
        return self.solaTemp

    def Solatid(self):    
        return self.solaTid
        
    def Saudatemp(self):    
        return self.SaudaTemp

    def Saudatid(self):    
        return self.SaudaTid

    def Sinnestemp(self):    
        return self.SinnesTemp
    
    def Sinnestid(self):    
        return self.SinnesTid    

    def Runetemp(self):    
        return self.RuneTemp

    def Runetid(self): 
        return self.RuneTid  

    def Runetrykk(self):
        return self.RuneTrykk
    
    def Sinnestrykk(self):
        return self.SinnesTrykk
    
    def Saudatrykk(self):
        return self.SaudaTrykk 

    def SolaTrykk(self):
        return self.solaTrykk
    


