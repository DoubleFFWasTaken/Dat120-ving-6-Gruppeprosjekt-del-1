#plotting
from matplotlib import pyplot as plt
import csv
from access_files import sola_temp

#Hvilken psykopat velger å kalle vilen for temperatur_trykk_met_samme_rune_time_datasett.csv.txt
#JEG HAR LETT SÅ LENGE ETTER EN FEIL SÅ FINNER JEG UT AT DET EN EN .TXT FIL MED NAVNET .CSV HVORFOR FAEN



plt.plot(sola_temp, tid, label="sola temp")
#plt.plot(other)

plt.legend()
plt.grid()
