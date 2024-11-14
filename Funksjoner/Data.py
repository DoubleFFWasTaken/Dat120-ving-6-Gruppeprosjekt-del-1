
import csv
import datetime as dt

class Data(): 
    def __init__(self, filnavn):

        self.filnavn     = filnavn

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
        self.RuneTrykkBar= []
        self.RuneTrykkAbs= []

        if self.filnavn  == "Filer/temperatur_trykk_met_samme_rune_time_datasett.csv.txt":
            self.Soladata  ()
        
        if self.filnavn  == "Filer/trykk_og_temperaturlogg_rune_time.csv.txt":
            self.Runedata  ()

        if self.filnavn  == "Filer/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt":
            self.Sirdaldata()


        
    def Soladata(self):
            with open(self.filnavn, "r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=';') 
                for i, row in enumerate(reader):
                        
                        if "Navn" in row[0] or "Data" in row[0]:
                            print(f"skipping line {i}, {row[0]}" )
                            continue

                        time_str  = row[2]
                        base_time = dt.datetime.strptime(time_str, "%d.%m.%Y %H:%M")
                        self.solaTid  .append(base_time)

                        self.solaTemp .append(float(row[3].replace(',', '.'))) 
                        self.solaTrykk.append(float(row[4].replace(',', '.')))
            print(self.solaTrykk[-1])

    def Sirdaldata(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=';') 
                for i, row in enumerate(reader):
                    if "Navn" in row[0] or "Data" in row[0]:
                            print(f"skipping line {i}, {row[0]}" )
                            continue
                    
                    time_str  = row[2]
                    base_time = dt.datetime.strptime(time_str, "%d.%m.%Y %H:%M")
                    
                    if "Sinnes" in row[0]:

                        self.SinnesTid  .append(base_time)

                        self.SinnesTemp .append(float(row[3].replace(',', '.'))) 
                        self.SinnesTrykk.append(float(row[4].replace(',', '.')))


                    if "Sauda" in row[0]:

                        self.SaudaTid  .append(base_time)

                        self.SaudaTemp .append(float(row[3].replace(',', '.')))
                        self.SaudaTrykk.append(float(row[4].replace(',', '.')))



    def Runedata(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';') 
            for i, row in enumerate(reader):
                try:
                    if "Navn" in row[0] or "Data" in row[0]:
                        print(f"skipping line {i}, {row[0]}" )
                        continue
                    time_str = row[0].strip()

                    if 'am' in time_str.lower() or 'pm' in time_str.lower():
                        if time_str.startswith("06/13/2021 00"):
                            time_str = "06/13/2021 12" + time_str[13:]
                        base_time = dt.datetime.strptime(time_str, "%m/%d/%Y %I:%M:%S %p")
                    else:
                        if "Navn" in row[0] or "Data" in row[0]:
                            print(f"skipping line {i}, {row[0]}" )
                            continue                        
                        base_time = dt.datetime.strptime(time_str, "%m.%d.%Y %H:%M")
                    
                    
                    if not self.RuneTid or self.RuneTid[-1] != base_time:
                        self.RuneTid     .append(base_time)
                        self.RuneTemp    .append(float(row[4].replace(',', '.')))
                        self.RuneTrykkAbs.append(float(row[3].replace(',', '.')))
                        self.RuneTrykkBar.append(float(row[2].replace(',', '.')))
                        
                except Exception as e:
                    print(f"Error processing row {i}: {e}")
                    continue


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

    def RunetrykkAbs(self):
        return self.RuneTrykkAbs
    
    def RunetrykkBar(self):
        return self.RuneTrykkBar
    
    def Sinnestrykk(self):
        return self.SinnesTrykk
    
    def Saudatrykk(self):
        return self.SaudaTrykk 

    def SolaTrykk(self):
        return self.solaTrykk
    


