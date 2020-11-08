import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from functools import partial

from dda import DrawDDA
from Bresenham import DrawBre
from midpoint_circle import Drawcircle
from midpoint_ellipse import Drawellipse
import mainGUI

def drawdda(ui):
    x0 = int(ui.DDA_start_x.text())
    y0 = int(ui.DDA_start_y.text())
    x1 = int(ui.DDA_end_x.text())
    y1 = int(ui.DDA_end_y.text())
    DrawDDA(x0, y0, x1, y1)

def drawbre(ui):
    x0 = int(ui.B_start_x.text())
    y0 = int(ui.B_start_y.text())
    x1 = int(ui.B_end_x.text())
    y1 = int(ui.B_end_y.text())
    DrawBre(x0, y0, x1, y1)
    
def drawcircle(ui):
    x = int(ui.circle_x.text())
    y = int(ui.circle_y.text())
    r = int(ui.circle_r.text())
    Drawcircle(x, y, r)
    
def drawellipse(ui):
    x = int(ui.ellipse_x.text())
    y = int(ui.ellipse_y.text())
    long = int(ui.ellipse_long.text())
    short = int(ui.ellipse_short.text())
    Drawellipse(x, y, long, short)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainGUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.DDA_go.clicked.connect(partial(drawdda, ui))
    ui.B_go.clicked.connect(partial(drawbre, ui))
    ui.circle_go.clicked.connect(partial(drawcircle, ui))
    ui.ellipse_go.clicked.connect(partial(drawellipse, ui))
    sys.exit(app.exec_())