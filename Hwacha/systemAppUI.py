import sys
from PyQt4 import QtGui,QtCore

class hwachaForm(QtGui.QDialog):

    # Top level window with no parent
    def __init__(self, parent=None):
        # Super to initialize the form
        super(hwachaForm, self).__init__(parent)
        self.browser = QtGui.QTextBrowser()
        self.lineEdit = QtGui.QLineEdit("Message")
        # select all, so that user can overwrite
        self.lineEdit.selectAll()
        layout = QtGui.QVBoxLayout()
        # add widgets to the layout
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        # setLayout() is the layout manager, which gives ownership of the widgets and of itself to the form, and takes ownership of any nested layouts itself.
        self.setLayout(layout)
        # set focus to the start of lineEdit
        self.lineEdit.setFocus()
        # To signal the press of the return
        self.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), self.updateUi)
        self.setWindowTitle("Hwacha")

    def updateUi(self):
        try:
            text = unicode(self.lineEdit.text())
            self.browser.append("<b>%s</b>" % (text))
        except:
            self.browser.append("<font color=red>Error</font>")

app = QtGui.QApplication(sys.argv)
form = hwachaForm()
form.show()
sys.exit(app.exec_())
