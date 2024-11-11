#plot 
from Data import Data

Data_instance = Data("Filer/trykk_og_temperaturlogg_rune_time.csv.txt")

Data_instance.RuneTemp()


print(len(Data_instance.RuneTemp()))
