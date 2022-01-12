#Import the relevant libraries
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
from random import randint
import csv

#Import the csv file with sensor data and read the data into a variable called 'csvreader'
csv_file = open ('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_1.csv') 
csvreader = csv.reader(csv_file)

#create lists for each column of data in the csv file
time = []
x_vibration = []
y_vibration = []
z_vibration = []

next(csvreader) #Move to the second row in the data file
#For each row in the csv file, append each value to the corresponding list starting from first to last. Convert values to floats
for row in csvreader:
    #print(row)
    x = float(row[0])
    y1 = float(row[2])
    y2 = float(row[3])
    y3 = float(row[4])
    time.append(x)
    x_vibration.append(y1)
    y_vibration.append(y2)
    z_vibration.append(y3)
    # x = np.random.normal(size=1000)
    # y = np.random.normal(size=1000)

#Declare a class called 'MainWindow'
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        #Initialize data, counter and interval between data cycles. In this case, the interval is calculated by subtracting time values
        self.counter = 2
        self.interval = time[-1]-time[-2]
        self.x = time[0:self.counter]
        self.y1 = x_vibration[0:self.counter]
        self.y2 = y_vibration[0:self.counter]
        self.y3 = z_vibration[0:self.counter]

        #Set the background color
        self.graphWidget.setBackground('w')

        #Pick a pen color
        pen1 = pg.mkPen(color=(255,0,0))
        pen2 = pg.mkPen(color=(0,255,0))
        pen3 = pg.mkPen(color=(0,0,255))
        self.sensor_1 = self.graphWidget.plot(self.x, self.y1, pen=pen1, symbol='o')
        self.sensor_2 = self.graphWidget.plot(self.x, self.y2, pen=pen2, symbol='o')
        self.sensor_3 = self.graphWidget.plot(self.x, self.y3, pen=pen3, symbol='o')

        #Set time to update data
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    #Create a method to update the data after a certain period of time
    def update_plot_data(self):
        self.counter+=1
        self.x = self.x[1:]
        self.x.append(time[self.counter])
        self.interval = time[-1]+1-self.x[-1]

        self.y1 = self.y1[1:]
        self.y2 = self.y2[1:]
        self.y3 = self.y3[1:]
        self.y1.append(x_vibration[self.counter])
        self.y2.append(y_vibration[self.counter])
        self.y3.append(z_vibration[self.counter])

        self.sensor_1.setData(self.x, self.y1)
        self.sensor_2.setData(self.x, self.y2)
        self.sensor_3.setData(self.x, self.y3)


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())