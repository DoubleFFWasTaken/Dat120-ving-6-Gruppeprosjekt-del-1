
import csv
import datetime as dt

class Data(): 
    def __init__(self, filnavn):
        #BYTT DISSE MED REELLE VARIABELNAVN
        self.filnavn  = filnavn
        self.år       = []
        self.måned    = []
        self.dag      = []
        self.rad3     = []
        self.solflekker = []
        self.gj       = []
        self.rad6     = []
        self.rad7     = []
        self.datetime = []
        self.målinger = []
        self.LesData()  

    def LesData(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';') 

            for i, row in enumerate(reader): 
                
                self.år     .append(row[0].strip()) 
                self.måned  .append(row[1].strip())                
                self.dag    .append(row[2].strip())
                
                self.solflekker.append(float(row[4].strip()))
                self.målinger  .append(i)


                try:
                    time_str = f"{row[2]}.{row[1]}.{row[0]}"
                    base_time = dt.datetime.strptime(time_str, "%d.%m.%Y")
                    self.datetime.append(base_time)
                except Exception as e:
                    print(e, "line:", i)                    

    def yearly_avg(self):
        
        årlig_max = {}
        årlig_min = {}
        årlig_gj  = {}

        
        for i, date in enumerate(self.datetime):
            
            years = (date.year)
            verdi = self.solflekker[i]

            
            if years not in årlig_max:
                årlig_max[years] = []
                årlig_min[years] = []
                årlig_gj [years] = []

            
            årlig_max[years].append(verdi)
            årlig_min[years].append(verdi)
            årlig_gj [years].append(verdi)

            #dict        = {år : verdi}
        self.årlig_maks  = {key: max(values) for key, values in årlig_max.items()}
        self.årlig_min   = {key: min(values) for key, values in årlig_min.items()}
        self.årlig_gj    = {key: sum(values) / len(values) for key, values in årlig_gj.items()}
    # dictionary årlig_max er definert av å ta max-verdien fra verdier fra måneden key(0->n), i listen med alle max-verdier


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
    
