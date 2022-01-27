import serial #import the serial port library
import datetime #import the library for getting current time
from time import time #import the library for converting current time to unix time
import csv #import the csv library for writing to the csv file
import sys #import the sys library that is needed by the sys.exit() feature to close the program
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = t  # 100 time points
        self.y = x_vibration  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

    def update_plot_data(self):
            #self.counter+=1
            self.x = self.x[1:]
            self.x.append(t[-1])
            #self.interval = time[-1]+1-self.x[-1]

            self.y = self.y[1:]
            # self.y2 = self.y2[1:]
            # self.y3 = self.y3[1:]
            self.y.append(x_vibration[-1])
            # self.y2.append(y_vibration[self.counter])
            # self.y3.append(z_vibration[self.counter])

            self.data_line.setData(self.x, self.y)
            # self.sensor_2.setData(self.x, self.y2)
            # self.sensor_3.setData(self.x, self.y3)
            


Dataline =[] #create an empty list called "Dataline" to hold a single row of data
#initialize the serial port reader by specifying the parameter of the serial port the data will be coming in from
serialPort = serial.Serial(port = "COM7", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialPort.close() #close the serial port to end other instances that may still be running in the background
serialPort.open() #Open the serial port
readings = 0 #This is a variable to set the number of readings to be taken before the program exits. 
             #This is necessary if the data is to be handled by excel which can't handle csv files with more than 1000000 rows

#The number of readings is altered based on the time needed to take the readings. Each sensor generates approximately 81 readings per second. 

#Create empty lists to hold vibration data
t = [] #time
x_vibration = [] #vibration in the x axis
no_data_point = 0
# y_vibration = [] #vibration in the y axis
# z_vibration = [] #vibration in the z axis

while (readings<2000): 
    if(serialPort.in_waiting>0): #Check if there is any data from the specified serial port
        f = open('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Vibrations.csv', 'a',newline='') #open the csv file that will be written to. 'a' worked, 'w' did not
        writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
        Time = int(time() * 1000) #Get the current date and time
        #UnixTime = time.mktime(Time.timetuple()) * 1000 #convert the current date and time to unixtime. Makes writing to csv less 'clanky'
        #print(UnixTime)
        #Read data out of the buffer until a carriage return/new line is found and save to the variable "Temperature"
        
        raw_data=serialPort.readline()  #Save the data from the serial port to a variable
        data_string = raw_data.decode("utf-8") #Decode the data string. This helps to remove some miscellaneous information
        data_list = data_string.split() #Split the string into a list of individual words. This separates data from different vibration axes
        Dataline.append(Time) #Add the Unixtime to the Dataline list. Time in the unix format keeps the data 'neat' i.e. easier to transfer
        Dataline.extend(data_list) #Add the data_list list to the Dataline List
        if readings<30:
            readings+=1
        else:
            try:
                x_vibration.append (float(Dataline[2]))
                t.append (float(Dataline[0]))
                no_data_point +=1
                if no_data_point>=100:
                    MainWindow.update_plot_data()

                print(Dataline) #Print the dataline. Helps to verify the data that will be added to the csv file
                writer.writerows([Dataline]) #Write the values of Dataline list to the csv file as a list of lists. A simple list will result in each character being separated by a comma
                
            except:
                readings+=1
            # y_vibration.append(Dataline[2])
            # z_vibration.append(Dataline[3])
            
            Dataline=[] #Reinitialize the dataline list in preparation for the next reading
            readings+=1 #Adds one to the counter

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
serialPort.close() #close the serial port

