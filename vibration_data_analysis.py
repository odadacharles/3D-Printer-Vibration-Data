import endaq
import csv

csv_file = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Vibrations.csv') #Open the csv file where the bulk sensor data is stored
csvreader = csv.reader(csv_file) #Read through the bulk csv file and store its contents in a variable called 'csvreader'

data = {}
x_axis = 
y_axis