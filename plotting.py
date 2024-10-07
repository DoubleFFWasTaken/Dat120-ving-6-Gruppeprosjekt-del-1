#plotting
from matplotlib import pyplot as plt
from access_files import * #importerer alle funksjoner


# lager variabler vi kan bruke
SolaTemparatur = sola_temp()
RuneTemparatur = rune_temp()
RuneTid        = rune_tid()




#Hvilken psykopat velger å kalle vilen for temperatur_trykk_met_samme_rune_time_datasett.csv.txt
#JEG HAR LETT SÅ LENGE ETTER EN FEIL SÅ FINNER JEG UT AT DET EN EN .TXT FIL MED NAVNET .CSV HVORFOR FAEN


"""
plt.plot(SolaTemparatur,SolaTemparatur, label="sola temp")
plt.plot(RuneTemparatur,RuneTemparatur, label="sola temp")


plt.legend()
plt.grid()
plt.show()"""

print(len(SolaTemparatur), len(RuneTemparatur), len(RuneTid))
