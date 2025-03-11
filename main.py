import sys
from pyexpat.errors import messages

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

import osoby
from layout import Ui_Dialog
from osoba import Osoba
from osoby import Osoby


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.zapiszButton.clicked.connect(self.zapisz)
        self.osoby = Osoby()
        self.osoby.wczytaj("dane.txt")
        lista = ["(nowy)"]
        lista.extend([f'{o.imie}, {o.nazwisko}' for o in self.osoby.osoby])

        self.ui.comboBox.addItems(lista)
        self.show()

    def zapisz(self):
        imie = self.ui.imie.text()
        nazwisko = self.ui.nazwisko.text()
        dob = self.ui.dob.date().toPyDate()
        pesel = self.ui.pesel.text()
        miejscowosc = self.ui.miejscowosc.text()
        ulica = self.ui.ulica.text()
        kod = self.ui.kod.text()
        numer_domu = self.ui.numerDomu.text()

        try:
            self.osoby.osoby.append(Osoba(imie, nazwisko, dob, pesel, miejscowosc, ulica, kod, numer_domu))
            lista = ["(nowy)"]
            lista.extend([f'{o.imie}, {o.nazwisko}' for o in self.osoby.osoby])
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(lista)

            self.czysc_pola()

        except ValueError as e:
            message = QMessageBox()
            message.setText(e.__str__())
            message.exec()

    def czysc_pola(self):
        self.ui.imie.clear()
        self.ui.nazwisko.clear()
        self.ui.dob.setDate(QDate.currentDate())
        self.ui.pesel.clear()
        self.ui.miejscowosc.clear()
        self.ui.ulica.clear()
        self.ui.kod.clear()
        self.ui.numerDomu.clear()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    app.exec()
    ex.osoby.zapisz("dane.txt")
    sys.exit()