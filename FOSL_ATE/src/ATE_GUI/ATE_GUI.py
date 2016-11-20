#!/usr/bin/python
# calendar.py


#this master branch.
import sys
from PyQt4 import QtGui, QtCore



class Calendar(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'),
        self.showDate)
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        
    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))

'''
app = QtGui.QApplication(sys.argv)
w = Calendar()
w.show()
sys.exit(app.exec_())
'''

global iLoop
iLoop = 0
class ProgressBar(QtGui.QWidget):


    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 1050, 200)
        self.setWindowTitle('ProgressBar')
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 1000, 50)
        self.button = QtGui.QPushButton('Start', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 120)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.onStart)
        self.timer = QtCore.QBasicTimer()
        self.step = 0
    def timerEvent(self, event):
	global iLoop
        if self.step >= 100:
            #self.timer.stop()
            self.step=-1
	    iLoop=iLoop+1
            self.button.setText('%d'%iLoop)
	    print "iLoop:",iLoop

        self.step = self.step +1
        self.pbar.setValue(self.step)


    def onStart(self):
	global iLoop
        if self.timer.isActive():
            #self.timer.stop()
            self.button.setText('%d'%iLoop)
        else:
            self.timer.start(100, self)
            self.button.setText('%d'%iLoop)




app = QtGui.QApplication(sys.argv)
icon = ProgressBar()
icon.show()
sys.exit(app.exec_())







        
