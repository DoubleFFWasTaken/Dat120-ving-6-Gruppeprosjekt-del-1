import csv
import datetime as dt

class Data(): 
    def __init__(self, filnavn=None):

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
        
        self.maksForskjelltrykk = float('-inf')
        self.minForskjelltrykk = float('inf')
        self.maksForskjelltemp = float('-inf')
        self.minForskjelltemp = float('inf')
        self.gjenforskjellTemp = 0
        self.gjenforskjellTrykk = 0

        self.TrykkForskjell()
        self.TempForskjell()
        self.GjennomsnittTempogTrykk()

        self.LesData()
  

    def LesData(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';') 

#sjekker hvilken fil vi er i og formaterer data korrekt

            for i, row in enumerate(reader): 

                if "Data er gyldig" in row[0]:
                    print(f"Skipping non-data row {i}: {row}")
                    continue

                if "navn" in row[0]:
                    print(f"Skipping non-data row {i}: {row}")
                    continue


                if "Sinnes" in row:
                    time_str = row[2]
                    base_time = dt.datetime.strptime(time_str, "%d.%m.%Y %H:%M")

                    self.SinnesTid.append(base_time)

                    self.SinnesTemp.append(float(row[3].replace(',', '.'))) 
                    self.SinnesTrykk.append(float(row[4].replace(',', '.')))


                if "Sauda" in row:
                    time_str = row[2]
                    base_time = dt.datetime.strptime(time_str, "%d.%m.%Y %H:%M")

                    self.SaudaTid.append(base_time)

                    self.SaudaTemp.append(float(row[3].replace(',', '.')))
                    self.SaudaTrykk.append(float(row[4].replace(',', '.')))



                if "Sola" in row:                
                    time_str = row[2]
                    base_time = dt.datetime.strptime(time_str, "%d.%m.%Y %H:%M")

                    self.solaTid.append(base_time)

                    self.solaTemp.append(float(row[3].replace(',', '.'))) 
                    self.solaTrykk.append(float(row[4].replace(',', '.')))


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
''' 
    def TrykkForskjell(self):
        try: 
            for i in range(len(self.solaTid)):
                for j in range(len(self.RuneTid)):
                    if self.solaTid[i] == self.RuneTid[j]:
                        differanse = abs(self.solaTrykk[i] - self.RuneTrykk[j])
                        if differanse > self.maksForskjelltrykk:
                            self.maksForskjelltrykk = differanse
                        if differanse < self.minForskjelltrykk:
                            self.minForskjelltrykk = differanse
        except IndexError as e:
            print("IndexError:", e)
    
    def TempForskjell(self):
        try: 
            for i in range(len(self.solaTid)):
                for j in range(len(self.RuneTid)):
                    if self.solaTid[i] == self.RuneTid[j]:
                        differanse = abs(self.solaTemp[i] - self.RuneTemp[j])
                        if differanse > self.maksForskjelltemp:
                            self.maksForskjelltemp = differanse
                        if differanse < self.minForskjelltemp:
                            self.minForskjelltemp = differanse
        except IndexError as e:
            print("IndexError:", e)

    def GjennomsnittTempogTrykk(self):
        TotalSolatemp = sum(self.solaTemp)
        TotalRunetemp = sum(self.RuneTemp)
        TotalSolatrykk = sum(self.solaTrykk)
        TotalRunetrykk = sum(self.RuneTrykk)
        
        antallSolaTemp = len(self.solaTemp)
        antallRuneTemp = len(self.RuneTemp)
        antallSolaTrykk = len(self.solaTrykk)
        antallRuneTrykk = len(self.RuneTrykk)
        
        gjennomsnittSolaTemp = TotalSolatemp / antallSolaTemp if antallSolaTemp > 0 else 0
        gjennomsnittRuneTemp = TotalRunetemp / antallRuneTemp if antallRuneTemp > 0 else 0
        gjennomsnittSolatrykk = TotalSolatrykk / antallSolaTrykk if antallSolaTrykk > 0 else 0
        gjennomsnittRunetrykk = TotalRunetrykk / antallRuneTrykk if antallRuneTrykk > 0 else 0

        self.gjenforskjellTemp = abs(gjennomsnittSolaTemp - gjennomsnittRuneTemp) / 2
        self.gjenforskjellTrykk = abs(gjennomsnittSolatrykk - gjennomsnittRunetrykk) / 2

'''
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

'''
    def MaksForskjelltrykk(self):
        return self.maksForskjelltrykk
    
    def MinForskjelltrykk(self):
        return self.minForskjelltrykk

    def MaksForskjelltemp(self):
        return self.maksForskjelltemp
    
    def MinForskjelltemp(self):
        return self.minForskjelltemp

    def GjenforskjellTemp(self):
        return self.gjenforskjellTemp
    
    def GjenforskjellTrykk(self):
        return self.gjenforskjellTrykk
'''
