import re
import test
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class   myui(QMainWindow,test.Ui_MainWindow):

    _signal = pyqtSignal(str)

    def __init__(self,text,parent=None):
        super(myui,self).__init__(parent)
        self.__text = text
        self.__index = 0
        self.setupUi(self)
        self.updateUi()

    def updateUi(self):
        if self.findLineEdit.text():
            enable = True
        else:
            enable = False
        self.findButton.setEnabled(enable)
        self.replaceButton.setEnabled(enable)
        self.replaceAllButton.setEnabled(enable)

    def text(selfs):
        return self.__text

    def makeRegex(self):
        findText = self.findLineEdit.text()
        if self.syntaxComboBox.currentText() == "Literal":
            findText = re.escape(findText)
        flags = re.MULTILINE | re.DOTALL | re.UNICODE
        if not self.caseCheckBox.isChecked():
            flags |= re.IGNORECASE
        if self.wholeCheckBox.isChecked():
            findText = r"\b%s\b" % findText
        return re.compile(findText,flags)

    @pyqtSlot("QString")
    def on_findLineEdit_textEdited(self,text):
        self.__index = 0
        self.updateUi()

    @pyqtSlot()
    def on_findButton_clicked(self):
        regex = self.makeRegex()
        match = regex.search(self.__text,self.__index)
        if match is not None:
            self.__index = match.end()
            self._signal.emit("find at %d"%match.start())
        else:
            self._signal.emit("not found")


    @pyqtSlot()
    def on_replaceButton_clicked(self):
        regex = self.makeRegex()
        self.__text = regex.sub(self.replaceLineEdit.text(),self.__text,1)
        print("%s"%self.__text)
    @pyqtSlot()
    def on_replaceAllButton_clicked(self):
        regex = self.makeRegex()
        self.__text = regex.sub(self.replaceLineEdit.text(),self.__text)
        print("%s" % self.__text)


