import pyqtgraph as pg
import numpy as np
import sys
from PyQt6 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)  # Create QApplication ***

def main ():
    x = np.random.normal(size=1000)
    y = np.random.normal(size=1000)
    pg.plot(x, y, pen=None, symbol='o')  ## setting pen=None disables line drawing

if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        main()
        app.exec()  # Start QApplication event loop ***