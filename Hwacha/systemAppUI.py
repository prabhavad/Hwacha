import sys
from PyQt4 import QtGui,QtCore

class hwachaForm(QtGui.QDialog):

    def __init__(self, parent=None):
        pass

    def updateUi(self):
        pass

app = QtGui.QApplication(sys.argv)
form = hwachaForm()
form.show()
sys.exit(app.exec_())
