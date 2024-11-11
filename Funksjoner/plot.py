from Data import Data

rune_instance = Data("Filer/temperatur_trykk_met_samme_rune_time_datasett.csv.txt")
runetid = rune_instance.Runetemp()  # Call Runetemp() to retrieve data
print((runetid), "a")

sinnes = Data("Filer/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt")
sinnestid = sinnes.Sinnestid()  # Call Sinnestid() to retrieve data
print((sinnestid), "a")
