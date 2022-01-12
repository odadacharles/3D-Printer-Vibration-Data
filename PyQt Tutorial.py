from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
import time

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,31,29,32,35,45]
        temperature_2 = [28,32,33,30,41,43,39,34,29,34]

        # plot data: x, y values

        self.graphWidget.setBackground((100,50,255,25))
        pen = pg.mkPen(color=(255, 0, 0), width=1, style=QtCore.Qt.SolidLine)
        self.graphWidget.setTitle("PYQT Tutorial", color="b", size="30pt")
        self.graphWidget.setLabel('left','Temp(C)')
        self.graphWidget.setLabel('bottom','Hour(H)')
        self.graphWidget.addLegend() #Has to be added before the 'plot' method below
        #self.graphWidget.plot(hour, temperature, name = "Sensor 1",  pen = pen, symbol='+', symbolSize=30, symbolBrush=('b'))
        self.plot(hour,temperature_1,'Sensor 1','r')
        self.plot(hour,temperature_2,'Sensor 1','b')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setXRange(5,20, padding=0)
        self.graphWidget.setYRange(30,40, padding=0)


    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x,y, name=plotname, pen=pen, symbol='o', symbolSize=5, symbolBrush=(color))
    
       
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()