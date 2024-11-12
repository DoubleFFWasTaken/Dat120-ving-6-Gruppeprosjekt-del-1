def Runedata(self):
        with open(self.filnavn, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';') 
            for i, row in enumerate(reader):
                try:
                    time_str = row[0]
                    
                    try:
                        seconds_offset = int(row[1])  
                    except ValueError:
                        print(f"Skipping row {i} due to invalid seconds: {row[1]}")
                        continue

                    if 'am' in time_str.lower() or 'pm' in time_str.lower():
                        base_time = dt.datetime.strptime(time_str, "%m/%d/%Y %H:%M:%S %p")

                    if 'am' not in time_str.lower() and 'pm' not in time_str.lower():
                        base_time = dt.datetime.strptime(time_str, "%m.%d.%Y %H:%M")
                    
                    #time_obj = base_time + dt.timedelta(seconds=seconds_offset)
                    self.RuneTid.append(base_time)


                    self.RuneTemp.append(float(row[4].replace(',', '.'))) 
                    self.RuneTrykk.append(float(row[3].replace(',', '.')))

                        
                except Exception as e:
                    print(f"Error processing row {i}: {e}")