
import csv
import datetime as dt

class Data(): 
    def __init__(self, filnavn):

        self.filnavn  = filnavn

        self.solaTemp    = []
        self.solaTid     = []
    
        self.SaudaTemp   = []
        self.SaudaTid    = []
    
        self.SinnesTemp  = []
        self.SinnesTid   = []
    
        self.RuneTemp    = []
        self.RuneTid     = []
        self.RuneTrykk   = []

        self.LesData()  

    def LesData(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';') 

#sjekker hvilke fil vi er i og formaterer data korrekt
            for i, row in enumerate(reader): 
                
                if "Sinnes" in row:
                    return 0
                    #sinnes data

                if "Sauda" in row:
                    return 0
                    #bytt med sauda data

                if "Sola" in row:
                    return 0
                    #sola data

                if self.filnavn == "Filer/trykk_og_temperaturlogg_rune_time.csv.txt":
                    try:
                        time_str = row[0]
                        
                        try:
                            seconds_offset = int(row[1])  
                        except ValueError:
                            print(f"Skipping row {i} due to invalid seconds: {row[1]}")
                            continue

                        if 'am' in time_str.lower() or 'pm' in time_str.lower():
                            base_time = dt.datetime.strptime(time_str, "%m/%d/%Y %H:%M:%S %p")
                        else:
                            base_time = dt.datetime.strptime(time_str, "%m.%d.%Y %H:%M")
                        
                        time_obj = base_time + dt.timedelta(seconds=seconds_offset)
                        self.RuneTid.append(time_obj)

                        trykk_value = row[4].replace(',', '.') if row[4] else None
                        temp_value = row[3].replace(',', '.') if row[3] else None

                        if temp_value:
                            self.RuneTemp.append(float(temp_value)) 
                        else:
                            self.RuneTemp.append(None)

                        if trykk_value:
                            self.RuneTrykk.append(float(trykk_value))
                        else:
                            self.RuneTrykk.append(None)
                            
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
