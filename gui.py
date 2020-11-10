from PyQt5 import QtCore, QtGui, QtWidgets
import chemistry as ch
import misc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 10, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.proceed)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 50, 51, 17))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 61, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setEnabled(False)
        self.listView.setGeometry(QtCore.QRect(10, 70, 331, 111))
        self.listView.setWordWrap(True)
        self.listView.setObjectName("listView")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 349, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chémia"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.radioButton.setText(_translate("MainWindow", "Prvok"))
        self.radioButton_2.setText(_translate("MainWindow", "Vzorec"))

    def proceed(self):
        vlastnost, informacie = self.lineEdit.text(), []
        if self.radioButton.isChecked():
            if misc.cisla() in vlastnost:
                if '.' in vlastnost:
                    vlastnost = float(vlastnost)
                else:
                    vlastnost = int(vlastnost)
                    
            if ch.informacie_o_prvku(vlastnost) is not None:
                    informacie = ch.informacie_o_prvku(vlastnost)
                    informacie = ch.informacie_o_prvku(vlastnost)
            elif ch.informacie_o_prvku(vlastnost) is None:
                    exit()

            self.listView.addItem(f'Slovenský názov: {informacie[2]}')
            self.listView.addItem(f'Latinský názov: {informacie[1]}')
            self.listView.addItem(f'Značka: {informacie[0]}')
            self.listView.addItem(f'Protónové číslo: {informacie[3]}')
            self.listView.addItem(f'Atómová hmostnosť: {informacie[4]}')


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
