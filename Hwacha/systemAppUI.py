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
        self.clear = "Clear screen"
        self.emptySm = "None"
        self.defaultSmName = "Choose Social Media Name"
        self.requiredSmList = []
        self.key = []

        self.browser = QtGui.QTextBrowser()
        self.lineEdit = QtGui.QLineEdit(self.defaultMessage)
        # Select all, so that user can overwrite
        self.lineEdit.selectAll()
        self.button = QtGui.QPushButton(self.send)
        self.smComboBox = QtGui.QComboBox()
        self.smComboBox.addItem(self.emptySm)
        self.clearButton = QtGui.QPushButton(self.clear)

        #create app object
        appObject = appControl.appController()
        self.smComboBox.addItems(appObject.getAvailableSmList())
        self.lineEdit2 = QtGui.QLineEdit(self.defaultSmName)
        #self.browser2 = QtGui.QTextBrowser()
        

        layout = QtGui.QVBoxLayout()

        # Add widgets to the layout
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.smComboBox)
        #layout.addWidget(self.browser2)
        # lineEdit2 is purposefully removed from layout
        #layout.addWidget(self.lineEdit2)
        layout.addWidget(self.button)
        layout.addWidget(self.clearButton)

        # setLayout() is the layout manager, which gives ownership of the widgets and of itself to the form, and takes ownership of any nested layouts itself.
        self.setLayout(layout)

        # Set focus to the start of lineEdit
        self.lineEdit.setFocus()

        # To signal the press of the return
        self.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), self.updateUi)
        # To signal the click over the button
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.updateUi)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.resetRequiredSmList)
        #self.connect(self.button, QtCore.SIGNAL("clicked()"), self.getKey)
        #self.connect(self.button, QtCore.SIGNAL("clicked()"), self.broadcast)

        self.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.cleanBrowser)

        # To signal index change in comboBox
        self.connect(self.smComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.lineEdit2,QtCore.SLOT("setText(QString)"))
        self.connect(self.smComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateSmBrowser)
        self.connect(self.smComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateSmList)

        self.setWindowTitle("Hwacha")

    def broadcast(self):
        message = unicode(self.lineEdit.text())
        appObject = appControl.appController()
        try:
            retValue = appObject.broadcastMessage(message,self.requiredSmList)
        except:
            retValue = "Failed"

    def resetRequiredSmList(self):
        self.requiredSmList = []

    def updateSmList(self):
        smName = unicode(self.lineEdit2.text())
        if smName not in self.requiredSmList:
            self.requiredSmList.append(smName)

    def cleanBrowser(self):
        self.browser.clear()

    def updateSmBrowser(self):
        #self.browser2.append("<font color=yellow>=)Hwacha=)</font>")
        try:
            smName = unicode(self.lineEdit2.text())
            if smName != self.defaultSmName and smName != self.emptySm:
                if smName not in self.requiredSmList:
                    self.browser.append("<b>%s,</b>" % (smName))
                else:
                    self.browser.append("<font color=Red>Already selected</font>")
            else:
                raise ValueError('Social Media cannot be added')
        except:
            self.browser.append("<font color=red>Choose a social media</font>")
        #self.browser2.append("<font color=yellow>(=Hwacha(=</font>")

    def updateUi(self):
        self.browser.append("<font color=yellow>=)Hwacha=)</font>")
        try:
            text = unicode(self.lineEdit.text())
            smName = unicode(self.lineEdit2.text())

            appObject = appControl.appController()
            retValue = appObject.getMessage(lambda: text)
            retValue2 = appObject.getSmName(lambda: smName)
            if retValue == text: 
                if retValue2 == smName:
                    if retValue2 != self.defaultSmName and retValue2 != self.emptySm: 
                        self.browser.append("<b>%s</b> broadcasted in <font color=blue><b>%s</b></font>" % (text,smName))
                    else:
                        self.browser.append("<font color=red>Social Media not choosen</font>")
                        raise ValueError('Social Media not choosen')
                else:
                    self.browser.append("<font color=red>Message cannot be broadcasted</font>")
                    raise ValueError('Message cannot be broadcasted')
            else:
                self.browser.append("<font color=red>Message cannot be readr</font>")
                raise ValueError('Message cannot be read')
        except:
            self.browser.append("<font color=red>Error</font>")
        self.browser.append("<font color=yellow>(=Hwacha(=</font>")

app = QtGui.QApplication(sys.argv)
form = hwachaForm()
form.show()
sys.exit(app.exec_())
