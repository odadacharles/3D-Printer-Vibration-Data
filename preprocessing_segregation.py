import csv

def main ():
    csv_file = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Vibrations.csv')
    csvreader = csv.reader(csv_file)
    header = next(csvreader)                     #Assign the first item in trading pairs the header variable

    for row in csvreader:
        if "S1" in row[1]:
            f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_1.csv', 'a',newline='') #open the csv file that will be written to. 'a' worked, 'w' did not
            writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
            new_row = []
            new_row.append(row[0])
            new_row.extend(row[1])
            writer.writerows([new_row])
        elif "S2" in row[1]:
            f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_2.csv', 'a',newline='') #open the csv file that will be written to. 'a' worked, 'w' did not
            writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
            new_row = []
            new_row.append(row[0])
            new_row.extend(row[1])
            writer.writerows([new_row])

#Run the function above if the condition below is met
if __name__ == "__main__":
    main()