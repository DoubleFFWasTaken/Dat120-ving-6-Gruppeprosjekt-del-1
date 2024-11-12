from Data import Data
from matplotlib import pyplot as plt

rune_instance    = Data("Filer/trykk_og_temperaturlogg_rune_time.csv.txt")
runetemp         = rune_instance.Runetemp        ()  
runetrykk        = rune_instance.Runetrykk       ()
runetid          = rune_instance.Runetid         ()


sirdal_instance  = Data("Filer/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv.txt")
sinnestemp       = sirdal_instance.Sinnestemp    ()
sinnestrykk      = sirdal_instance.Sinnestrykk   ()
sinnestid        = sirdal_instance.Sinnestid     ()  

saudatemp        = sirdal_instance.Saudatemp     ()
saudatrykk       = sirdal_instance.Saudatrykk    ()
saudatid         = sirdal_instance.Saudatid      ()


sola_instance    = Data("Filer/temperatur_trykk_met_samme_rune_time_datasett.csv.txt")
solatemparatur   = sola_instance.Solatemp        ()
solatrykk        = sola_instance.SolaTrykk       ()
solatid          = sola_instance.Solatid         ()



plt.plot(runetid  , runetemp        , label = "runetemp")
plt.plot(sinnestid, sinnestemp      , label = "sinnestemp")
plt.plot(saudatid , saudatemp       , label = "saudatemp")
plt.plot(solatid  , solatemparatur  , label = "solatemp")
plt.grid    ()
plt.legend  ()
plt.show    ()


#print(runetid)
print(len(runetid))
print(runetid[-1])

