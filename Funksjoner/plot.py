from Data import Data
from matplotlib import pyplot as plt
import pandas as pd

rune_instance    = Data("Filer/trykk_og_temperaturlogg_rune_time.csv.txt")
runetemp         = rune_instance.Runetemp        ()  
runetrykkAbs     = rune_instance.RunetrykkAbs    ()
runetrykkBar     = rune_instance.RunetrykkBar    ()
runetid          = rune_instance.Runetid         ()
trykkforskjel    = rune_instance.smoothed_diff

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



hvilken          = int(input("0 graf, 1 histogram, 2 trykkforskjell"))

if hvilken > 2:
    print("solatid", solatid )
    print("runtid", runetid)




if hvilken       == 0:
    plt.plot(runetid  , runetemp        , label = "runetemp")
    plt.plot(sinnestid, sinnestemp      , label = "sinnestemp")
    plt.plot(saudatid , saudatemp       , label = "saudatemp")
    plt.plot(solatid  , solatemparatur  , label = "solatemp")
    plt.grid    ()
    plt.legend  ()
    plt.show    ()

if hvilken == 1: 

    alle_temperaturer = [runetemp, sinnestemp, saudatemp, solatemparatur]
    navn              = ["Rune", "Sinnes", "Sauda", "Sola"]
    fig, axes         = plt.subplots(2, 2, figsize=(14, 10)) 
    fig.suptitle("Temperaturer:", fontsize=16)
    

    for i, temperatures in enumerate(alle_temperaturer):
        row      = i // 2  
        col      = i % 2   
        min_temp = int(min(temperatures))
        max_temp = int(max(temperatures))
        
        axes[row, col].hist         (temperatures, bins=range(min_temp, max_temp + 2), edgecolor='black', color='skyblue')
        axes[row, col].set_title    (navn[i])
        axes[row, col].set_xlabel   ('Temp °C')
        axes[row, col].set_ylabel   ('Frekvens')
        axes[row, col].grid         (axis='y', alpha=0.75)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


if hvilken == 2:
        plt.plot(runetid  , trykkforskjel         , label = "Trykkforskjell")

        plt.title("Trykkforskjell: barometrisk vs absolutt")
        plt.grid    ()
        plt.legend  ()
        plt.show    ()
        

else: 
    print("feil input")
    
