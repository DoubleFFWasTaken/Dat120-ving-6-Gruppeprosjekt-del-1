import csv


#class SolaInfo:    
def sola_temp():
    temp    = []
    tid     = []    
    with open('temperatur_trykk_met_samme_rune_time_datasett.csv.txt') as data_sola:

        reader = csv.reader(data_sola, delimiter=';')
        for row in reader:
            temp.append(row[3])
        return temp
    data_sola.close()


#class RuneInfo:
def rune_temp():
    temp    = []
    with open('trykk_og_temperaturlogg_rune_time.csv.txt') as data_rune:

        reader = csv.reader(data_rune, delimiter=';')
        for row in reader:
            temp.append(row[4])
        return temp
    data_rune.close()

def rune_tid():
    tid     = []    
    with open('trykk_og_temperaturlogg_rune_time.csv.txt') as data_rune:

        reader = csv.reader(data_rune, delimiter=';')
        for row in reader:
            tid.append(row[1])
        return tid

    data_rune.close()

def rune_trykk_bar():
    temp     = []    
    with open('trykk_og_temperaturlogg_rune_time.csv.txt') as data_rune:

        reader = csv.reader(data_rune, delimiter=';')
        for row in reader:
            temp.append(row[2])
        return temp

    data_rune.close()

def rune_trykk_abs():
    temp     = []    
    with open('trykk_og_temperaturlogg_rune_time.csv.txt') as data_rune:

        reader = csv.reader(data_rune, delimiter=';')
        for row in reader:
            temp.append(row[3])
        return temp

    data_rune.close()    