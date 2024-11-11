
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

        self.LesData()  

    def LesData(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';') 

#sjekker hvilke fil vi er i og formaterer data korrekt
            for i, row in enumerate(reader): 
                try:
                    if "Sinnes" in row:
                        return 0
                        #sinnes data

                    if "Sauda" in row:
                        return 0
                        #bytt med sauda data

                    if "Sola" in row:
                        return 0
                        #sola data

                    #kan egentlig bytte alle if med dette:
                    if self.filnavn == "Filer/trykk_og_temperaturlogg_rune_time.csv.txt":
                    
                        if "am" not in row:
                            time_str = row[0]
                            base_time = dt.datetime.strptime(time_str,"%m.%d.%Y %H:%M")
                            self.RuneTid.append(base_time)
                            self.RuneTemp.append(row[4])
                        
                        if "am" in row:
                            time_str = row[0]
                            base_time = dt.datetime.strptime(time_str,"%m/%d/%Y %I:%M:%S %p")
                            self.RuneTemp.append(row[4])
                        else: 
                            print(f"feil i linje {i}, {row[0]}")   
                        

                except Exception as e:
                    print(f"Error processing row {i}: {e}")



#endre disse til å passe listene fra tidligere


    def Data_1(self):
        return self.liste
