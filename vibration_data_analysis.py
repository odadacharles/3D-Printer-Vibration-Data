import pyqtgraph as pg
import numpy as np
import sys
import csv
from PyQt6 import QtWidgets, QtCore
from pyqtgraph.Qt import QtGui

app = QtWidgets.QApplication(sys.argv)  # Create QApplication ***
w = QtWidgets.QWidget()

def main ():
    csv_file = open ('C:/Users/Charlie.O/Documents/Python Projects/3D Printer Vibration Data/Sensor_1.csv')
    csvreader = csv.reader(csv_file)


    time = []
    x_vibration = []
    y_vibration = []
    z_vibration = []

    next(csvreader)
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

    graph1 = pg.plot(time, x_vibration, pen='r', symbol='o')  ## setting pen=None disables line drawing
    graph1.plot(time, y_vibration, pen='b', symbol='o')
    graph1.plot(time, z_vibration, pen='g', symbol='o')


if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        main()
        app.exec()  # Start QApplication event loop ***