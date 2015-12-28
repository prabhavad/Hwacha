# System app UI

import sys
from appControl import appControl
from PyQt4 import QtGui,QtCore

class hwachaForm(QtGui.QDialog):

    # Top level window with no parent
    def __init__(self, parent=None):

        # --------- Super to initialize the form ---------------
        super(hwachaForm, self).__init__(parent)

        # --------- Some data abstractions ----------------
        self.defaultMessage = "Message"
        self.send = "Send"
        self.clear = "Clear screen"
        self.add = "Add"
        self.remove = "Remove"
        self.emptySm = "None"
        self.defaultSmName = "Choose Social Media Name"
        self.requiredSmList = []
        self.key = []
        self.displayAddSm = "Add Social Media Name"

        # ----------- Add GUI elements --------------------
        self.browser = QtGui.QTextBrowser()
        self.lineEdit = QtGui.QLineEdit(self.defaultMessage)
        # Select all, so that user can overwrite
        self.lineEdit.selectAll()
        self.button = QtGui.QPushButton(self.send)
        self.smComboBox = QtGui.QComboBox()
        self.smComboBox.addItem(self.emptySm)
        self.smComboBox2 = QtGui.QComboBox()
        self.smComboBox2.addItem(self.emptySm)
        self.clearButton = QtGui.QPushButton(self.clear)
        #create app object
        appObject = appControl.appController()
        self.smComboBox.addItems(appObject.getAvailableSmList())
        self.smComboBox2.addItems(appObject.getAvailableSmList())
        self.lineEdit2 = QtGui.QLineEdit(self.defaultSmName)
        self.lineEdit3 = QtGui.QLineEdit(self.displayAddSm)
        # self.lineEdit3.selectAll() // Not working
        self.addButton = QtGui.QPushButton(self.add)
        self.removeButton = QtGui.QPushButton(self.remove)
        self.lineEdit4 = QtGui.QLineEdit(self.emptySm)

        # -------- Add layout --------------------------
        layout = QtGui.QVBoxLayout()


        # ---------- Add widgets to the layout --------------
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.smComboBox)
        # lineEdit2 is purposefully removed from layout, if need to see uncomment
        #layout.addWidget(self.lineEdit2)
        layout.addWidget(self.button)
        layout.addWidget(self.clearButton)
        layout.addWidget(self.lineEdit3)
        layout.addWidget(self.addButton)
        layout.addWidget(self.smComboBox2)
        # lineEdit4 is purposefully removed from layout, if need to see uncomment
        #layout.addWidget(self.lineEdit4)        
        layout.addWidget(self.removeButton)

        # setLayout() is the layout manager, which gives ownership of the widgets and of itself to the form, and takes ownership of any nested layouts itself.
        self.setLayout(layout)
        # Set focus to the start of lineEdit
        self.lineEdit.setFocus()

        
        # ------------- Add signals for the buttons on an action ------------------

        # To signal the press of the return
        self.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), self.updateUi)

        # To signal the click over the button
        #self.connect(self.button, QtCore.SIGNAL("clicked()"), self.updateUi)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.resetRequiredSmList)
        # The underlying is commented, this may come into use in future.
        #self.connect(self.button, QtCore.SIGNAL("clicked()"), self.getKey)

        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.verifyBroadcast)


        # clear the screen
        self.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.cleanBrowser)

        # Add action to 'Add' button
        self.connect(self.addButton, QtCore.SIGNAL("clicked()"), self.addSm)

         
        # Add action to 'Remove' button
        self.connect(self.removeButton, QtCore.SIGNAL("clicked()"), self.rmSm)


        # To signal index change in comboBox
        self.connect(self.smComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.lineEdit2,QtCore.SLOT("setText(QString)"))
        self.connect(self.smComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateSmBrowser)
        self.connect(self.smComboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateSmList)

        # To signal index change in comboBox2
        self.connect(self.smComboBox2, QtCore.SIGNAL("currentIndexChanged(QString)"), self.lineEdit4,QtCore.SLOT("setText(QString)"))

        # set window title
        self.setWindowTitle("Hwacha")


    def addSm(self):
        smName = unicode(self.lineEdit3.text())
        appObject = appControl.appController()
        self.browser.append("<font color=green>Hwacha :/socialMedia/$</font>")
        try: 
            smList = appObject.getAvailableSmList()
            if smName in smList:
                self.browser.append("<font color=blue><b>%s</b></font> is already in Social Media List" % (smName))
            else:
                addStatus = appObject.addSm([smName])
                self.smComboBox.addItem(smName)
                self.smComboBox2.addItem(smName)
                self.browser.append("<font color=blue><b>%s</b></font> successfully added to Social Media List" % (smName))
                
        except:
           self.browser.append("<font color=red><b>%s</b> cannot be added to Social Media List</font>" % (smName))

    def rmSm(self):
        smName = unicode(self.lineEdit4.text())
        appObject = appControl.appController()
        self.browser.append("<font color=green>Hwacha :/socialMedia/$</font>")
        try:
            rmStatus = appObject.removeSm([smName])
            self.smComboBox.clear()
            self.smComboBox.addItem(self.emptySm)
            self.smComboBox.addItems(appObject.getAvailableSmList())
            self.smComboBox2.clear()
            self.smComboBox2.addItem(self.emptySm)
            self.smComboBox2.addItems(appObject.getAvailableSmList())
            self.browser.append("<font color=blue><b>%s</b></font> successfully removed from Social Media List" % (smName))
        except Exception as a:
            print a
            self.browser.append("<font color=red><b>%s</b> cannot be removed from Social Media List</font>" % (smName))            

    def verifyBroadcast(self):
        updateUiStatus = self.updateUi()
        if updateUiStatus == True:
            broadcastStatus = self.broadcast()


    # Broadcast method
    def broadcast(self):
        """ Broadcast the input message in various social medias specified by the user"""
        self.browser.append("<font color=green>Hwacha :/broadcast/$</font>")
        message = unicode(self.lineEdit.text())
        smName = unicode(self.lineEdit2.text())
        appObject = appControl.appController()
        try:
            retValue = appObject.broadcastMessage(message,self.requiredSmList)
            self.browser.append("<b>%s</b> broadcasted in <font color=blue><b>%s</b></font>" % (message,smName))
        except Exception as a:
            print a
            retValue = "Failed"
            self.browser.append("<font color=Red>Sending failed</font>")
        return retValue


    def resetRequiredSmList(self):
        """ Reset the Social Media list into empty list """
        self.requiredSmList = []

    def updateSmList(self):
        """ Update the social media list.
        Add the user specified social media into the social media list """
        smName = unicode(self.lineEdit2.text())
        if smName not in self.requiredSmList:
            self.requiredSmList.append(smName)

    def cleanBrowser(self):
        """ Clear the browser screen """
        self.browser.clear()

    def updateSmBrowser(self):
        """ Update the browser screen on the user input on social media """
        #self.browser2.append("<font color=yellow>=)Hwacha=)</font>")
        try:
            smName = unicode(self.lineEdit2.text())
            if smName != self.defaultSmName and smName != self.emptySm:
                if smName not in self.requiredSmList:
                    self.browser.append("<b>%s selected.</b>" % (smName))
                else:
                    self.browser.append("<font color=Red>Already selected</font>")
            else:
                raise ValueError('Social Media cannot be added')
        except:
            self.browser.append("<font color=red>Choose a social media</font>")
        #self.browser2.append("<font color=yellow>(=Hwacha(=</font>")

    def updateUi(self):
        """ Update the browser screen based on the user input and report appropriate errors """
        try:
            text = unicode(self.lineEdit.text())
            smName = unicode(self.lineEdit2.text())

            appObject = appControl.appController()
            retValue = appObject.getMessage(lambda: text)
            retValue2 = appObject.getSmName(lambda: smName)
            if retValue == text: 
                if retValue2 == smName:
                    if retValue2 == self.defaultSmName or retValue2 == self.emptySm: 
                       # self.browser.append("<b>%s</b> broadcasted in <font color=blue><b>%s</b></font>" % (text,smName))
                    #else:
                        self.browser.append("<font color=green>Hwacha :/$</font>")
                        self.browser.append("<font color=red>Social Media not choosen</font>")
                        raise ValueError('Social Media not choosen')
                else:
                    self.browser.append("<font color=green>Hwacha :/$</font>")
                    self.browser.append("<font color=red>Message cannot be broadcasted</font>")
                    raise ValueError('Message cannot be broadcasted')
            else:
                self.browser.append("<font color=green>Hwacha :/$</font>")
                self.browser.append("<font color=red>Message cannot be read</font>")
                raise ValueError('Message cannot be read')
        except:
            self.browser.append("<font color=blue>Try again!</font>")
            return  False
        #self.browser.append("<font color=yellow>(=Hwacha(=</font>")
        return  True

if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    form = hwachaForm()
    form.show()
    sys.exit(app.exec_())
