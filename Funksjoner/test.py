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
        
        self.maksForskjell = float('-inf')
        self.minForskjell = float('inf')
        self.gjennomsnittforskjellTemp = 0
        self.gjennomsnittforskjellTrykk = 0
        
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
    
    def TempogTrykkForskjell(self):
        try: 
            for i in range(self.solaTid):
                for j in range(self.RuneTid):
                    if self.solaTid[i] == self.RuneTid[j]:
                        differanse = abs(self.solaTrykk[i] - self.RuneTrykk[j])
                        if differanse > self.maksForskjell:
                            self.maksForskjell = differanse
                        if differanse < self.minForskjell:
                            self.minForskjell = differanse
        except IndexError as e:
            print("IndexError:", e)
    
    def GjennomsnittTempogTrykk(self):
    
        gjennomsnittSolaTemp = 0
        gjennomsnittRuneTemp = 0
        gjennomsnittSolatrykk = 0
        gjennomsnittRunetrykk = 0
        
        TotalSolatemp = 0
        TotalRunetemp = 0
        TotalSolatrykk = 0
        TotalRunetrykk = 0
        
        antallSolaTemp = 0
        antallRuneTemp = 0
        antallSolaTrykk = 0
        antallRuneTrykk = 0
        
        for n in self.solaTemp():
            TotalSolatemp += self.solaTemp[n]
            antallSolaTemp += 1
            for n in self.solaTrykk():
                TotalSolatrykk += self.solaTrykk[n]
                antallSolaTrykk += 1
                
        gjennomsnittSolaTemp = TotalSolatemp / antallSolaTemp
        gjennomsnittSolatrykk = TotalSolatrykk / antallSolaTrykk
                
        for n in self.RuneTemp:
            TotalRunetemp += self.RuneTemp()
            antallRuneTemp += 1
            for n in self.RuneTrykk():
                TotalRunetrykk += self.RuneTrykk
                antallRuneTrykk += 1
        
        gjennomsnittRuneTemp = TotalRunetemp / antallRuneTemp
        gjennomsnittRunetrykk = TotalRunetrykk / antallRuneTrykk
        
        self.gjennomsnittforskjellTemp = abs(gjennomsnittSolaTemp - gjennomsnittRuneTemp) / 2
        self.gjennomsnittforskjellTrykk = abs(gjennomsnittSolatrykk - gjennomsnittRunetrykk) / 2

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

    def GjennomsnittTempogTrykk(self):
        return self.maksForskjell
    
    def GjennomsnittTempogTrykk(self):
        return self.minForskjell
    
    def GjennomsnittTempogTrykk(self):
        return self.gjennomsnittforskjellTemp
    
    def GjennomsnittTempogTrykk(self):
        return self.gjennomsnittforskjellTrykk

print(Data.maksForskjell)
print(Data.minForskjell)
print(Data.gjennomsnittforskjellTemp)
print(Data.gjennomsnittforskjellTrykk)
