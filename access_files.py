#access files
import csv
    
def sola_temp():
    temp    = []
    tid     = []    
    with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt') as data_sola:

        reader = csv.reader(data_sola, delimiter=';')
        for row in reader:
            temp.append(row[3])
            #tid.append (row[2])
        return temp
        #fiks tidformatering også 

    data_sola.close()