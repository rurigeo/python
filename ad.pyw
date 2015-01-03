#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, uic


class AddressBook(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)
        
        self.__id = '123'
        uic.loadUi( "ad.ui", self )
        self.openDeviceButton.clicked.connect(self.showid)
        self.getIdButton.clicked.connect(self.getid)
        self.setIdButton.clicked.connect(self.setid)
    
    def showid(self):
        QtGui.QMessageBox.information(self, "Title","Can't connect to dln_srv!")
        self.id.setText('0')
        
    def setid(self):
        self.__id = self.id.getText(self)
        self.id.setText(self._id) 
      
    def getid(self):
        self.id.setText(self.__id) 

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    addressBook = AddressBook()
    addressBook.show()

    sys.exit(app.exec_())
