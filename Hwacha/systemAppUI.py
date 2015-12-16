import sys
from appControl import appControl
from PyQt4 import QtGui,QtCore

class hwachaForm(QtGui.QDialog):

    # Top level window with no parent
    def __init__(self, parent=None):

        # Super to initialize the form
        super(hwachaForm, self).__init__(parent)

        # Some data abstractions
        self.defaultMessage = "Message"
        self.send = "Send"
        self.emptySm = "None"
        self.defaultSmName = "Choose Social Media Name"

        self.browser = QtGui.QTextBrowser()
        self.lineEdit = QtGui.QLineEdit(self.defaultMessage)
        # Select all, so that user can overwrite
        self.lineEdit.selectAll()
        self.button = QtGui.QPushButton(self.send)
        self.smComboBox = QtGui.QComboBox()
        self.smComboBox.addItem(self.emptySm)

        #create app object
        appObject = appControl.appController()
        self.smComboBox.addItems(appObject.getAvailableSmList())
        self.lineEdit2 = QtGui.QLineEdit(self.defaultSmName)

        layout = QtGui.QVBoxLayout()

        # Add widgets to the layout
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.smComboBox)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.button)

        # setLayout() is the layout manager, which gives ownership of the widgets and of itself to the form, and takes ownership of any nested layouts itself.
        self.setLayout(layout)

        # Set focus to the start of lineEdit
        self.lineEdit.setFocus()

        # To signal the press of the return
        self.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), self.updateUi)
        # To signal the click over the button
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.updateUi)
        # To signal index change in comboBox
        self.connect(self.smComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.lineEdit2,QtCore.SLOT("setText(QString)"))

        self.setWindowTitle("Hwacha")

    def updateUi(self):
        try:
            text = unicode(self.lineEdit.text())
            smName = unicode(self.lineEdit2.text())
            appObject = appControl.appController()

            retValue = appObject.getMessage(lambda: text)
            retValue2 = appObject.getSmName(lambda: smName)
            if retValue == text: 
                if retValue2 == smName:
                    self.browser.append("<b>%s</b> broadcasted in <font color=blue><b>%s</b></font>" % (text,smName))
                else:
                    raise ValueError('Message cannot be broadcasted')
            else:
                raise ValueError('Message cannot be read')

        except:
            self.browser.append("<font color=red>Error</font>")

app = QtGui.QApplication(sys.argv)
form = hwachaForm()
form.show()
sys.exit(app.exec_())
