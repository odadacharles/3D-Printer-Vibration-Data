import csv

def main ():
    csv_file = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Vibrations.csv') #Open the csv file where the bulk sensor data is stored
    csvreader = csv.reader(csv_file) #Read through the bulk csv file and store its contents in a variable called 'csvreader'

    f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_1.csv', 'a',newline='', encoding = 'utf-8') #open the csv file that will be written to. 'a' worked, 'w' did not
    writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
    writer.writerow([" Time ","Sensor", "X-Axis", "Y-Axis", "Z-Axis"]) #Write the header of the csv file

    f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_2.csv', 'a',newline='', encoding = 'utf-8') #open the csv file that will be written to. 'a' worked, 'w' did not
    writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
    writer.writerow([" Time ","Sensor", "X-Axis", "Y-Axis", "Z-Axis"]) #Write the header of the csv file

    f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_3.csv', 'a',newline='', encoding = 'utf-8') #open the csv file that will be written to. 'a' worked, 'w' did not
    writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
    writer.writerow([" Time ","Sensor", "X-Axis", "Y-Axis", "Z-Axis"]) #Write the header of the csv file


    #The sensor data is labelled to distinguish inputs from the three sensors. The loop below will go through each row of data and separate the data from the different sensors and store
    #each sensor's data in its respective csv file.
    for row in csvreader:
        if "S1" in row[1]: 
            f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_1.csv', 'a',newline='', encoding = 'utf-8') #open the csv file that will be written to. 'a' worked, 'w' did not
            writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
            writer.writerows([row])
        elif "S2" in row[1]:
            f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_2.csv', 'a',newline='', encoding = 'utf-8') #open the csv file that will be written to. 'a' worked, 'w' did not
            writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
            writer.writerows([row])
        elif "S3" in row[1]:
            f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_3.csv', 'a',newline='', encoding = 'utf-8') #open the csv file that will be written to. 'a' worked, 'w' did not
            writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
            writer.writerows([row])
        else:
            pass

#Run the function above if the condition below is met
if __name__ == "__main__":
    main()