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


def TrykkForskjell(solatid, solatrykk, runetid, runetrykkAbs):
    maksForskjelltrykk = float('-inf')
    makstrykkforskjelltid = 0
    minForskjelltrykk = float('inf')
    mintrykkforskjelltid = 0
    for i in range(len(solatid)):
        for j in range(len(runetid)):
            if solatid[i] == runetid[j]:
                differanse = abs(solatrykk[i] - runetrykkAbs[j])
                if differanse > maksForskjelltrykk:
                    maksForskjelltrykk = differanse
                    makstrykkforskjelltid = solatid[i]
                if differanse < minForskjelltrykk:
                    minForskjelltrykk = differanse
                    mintrykkforskjelltid = solatid[i]
    return maksForskjelltrykk, minForskjelltrykk, makstrykkforskjelltid, mintrykkforskjelltid

maksForskjelltrykk_resultat, minForskjelltrykk_resultat, makstrykkforskjelltid_resultat, minstrykkforskjelltid_resultat = TrykkForskjell(
    solatid, solatrykk, runetid, runetrykkAbs
)

print(f"Den største trykkforskjellen var {maksForskjelltrykk_resultat} ved {maksForskjelltrykk_resultat}.")
print(f"Den minste trykkforskjellen var ved {minForskjelltrykk_resultat} ved {minstrykkforskjelltid_resultat}.")


def TempForskjell():
    maksForskjelltemp = float('-inf')
    minForskjelltemp = float('inf')
    for i in range(len(solatid)):
        for j in range(len(runetid)):
            if solatid[i] == runetid[j]:
                differanse = abs(solatemparatur[i] - runetemp[j])
                if differanse > maksForskjelltemp:
                    maksForskjelltemp = differanse
                if differanse < minForskjelltemp:
                    minForskjelltemp = differanse


        
def GjennomsnittTempogTrykk(solatemparatur, runetemp, solatrykk, runetrykkAbs):
    TotalSolatemp = sum(solatemparatur)
    TotalRunetemp = sum(runetemp)
    TotalSolatrykk = sum(solatrykk)
    TotalRunetrykk = sum(runetrykkAbs)
    
    antallSolaTemp = len(solatemparatur)
    antallRuneTemp = len(runetemp)
    antallSolaTrykk = len(solatrykk)
    antallRuneTrykk = len(runetrykkAbs)
    
    gjennomsnittSolaTemp = TotalSolatemp / antallSolaTemp if antallSolaTemp > 0 else 0
    gjennomsnittRuneTemp = TotalRunetemp / antallRuneTemp if antallRuneTemp > 0 else 0
    gjennomsnittSolatrykk = TotalSolatrykk / antallSolaTrykk if antallSolaTrykk > 0 else 0
    gjennomsnittRunetrykk = TotalRunetrykk / antallRuneTrykk if antallRuneTrykk > 0 else 0

    gjenforskjellTemp = abs(gjennomsnittSolaTemp - gjennomsnittRuneTemp) / 2
    gjenforskjellTrykk = abs(gjennomsnittSolatrykk - gjennomsnittRunetrykk) / 2

    return gjenforskjellTemp, gjenforskjellTrykk

gjenforskjellTemp_resultat, gjenforskjellTrykk_resultat = GjennomsnittTempogTrykk(solatemparatur, runetemp, solatrykk, runetrykkAbs)

print("Den gjennomsnittlige temperaturforskjellen er:", gjenforskjellTemp_resultat)
print("Den gjennomsnitttlige trykkforskjellen er:", gjenforskjellTrykk_resultat)