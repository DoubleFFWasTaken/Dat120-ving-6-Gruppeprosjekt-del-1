
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
                            return 0
                        
                        if "am" in row:
                            return 0
                        

                except Exception as e:
                    print(f"Error processing row {i}: {e}")

            """
        
            time_str = f"{row[2]}.{row[1]}.{row[0]}"
            base_time = dt.datetime.strptime(time_str, "%d.%m.%Y")
            self.datetime.append(base_time)
               
            """

#endre disse til å passe listene fra tidligere, pass på at datoene og listene skal være like, vurderer å bruke arrays eller dictionaries

    def år_max(self):
        if not hasattr(self, 'årlig_maks'):
            self.yearly_avg()
        return self.årlig_maks

    def år_min(self):
        if not hasattr(self, 'årlig_min'):
            self.yearly_avg()
        return self.årlig_min

    def år_gj(self):
        if not hasattr(self, 'årlig_gj'):
            self.yearly_avg()
        return self.årlig_gj

    def Data_år(self):
        return self.år

    def Data_1(self):
        return self.måned

    def Data_2(self):
        return self.dag

    def Data_3(self):
        return self.rad3

    def Maksimum(self):
        return self.solflekker

    def Minimum(self):
        return self.solflekker

    def Data_6(self):
        return self.rad6

    def Data_7(self):
        return self.rad7
    
    def Gjennomsnitt(self):
        return self.gj

    def absTime(self):
        return self.datetime
    
