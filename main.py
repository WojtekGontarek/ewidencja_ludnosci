import sys
from pyexpat.errors import messages

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
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
        lista = ["(nowy)"]
        lista.extend(self.osoby.osoby)
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
            lista.extend(self.osoby.osoby)
            self.czysc_pola()
        except ValueError as e:
            message = QMessageBox()
            message.setText(str(e))
            message.exec()

    def czysc_pola(self):
        self.ui.imie.clear()
        self.ui.nazwisko.clear()
        self.ui.dob.clear()
        self.ui.pesel.clear()
        self.ui.miejscowosc.clear()
        self.ui.ulica.clear()
        self.ui.kod.clear()
        self.ui.numerDomu.clear()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())