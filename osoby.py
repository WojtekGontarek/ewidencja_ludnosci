import datetime

from osoba import Osoba


class Osoby:
    def __init__(self):
        self.osoby = []

    def zapisz(self, sciezka):
        with open(sciezka, 'w') as file:
            for osoba in self.osoby:
                file.write(osoba.__str__()+"\n")

    def wczytaj(self, sciezka):
        with open(sciezka, 'r') as file:
            dane = file.read()

        osoby_str = dane.split("\n")
        self.osoby = []
        for osoba in osoby_str:
            if osoba == "":
                break
            dane_osoby = osoba.split(";")
            dob = dane_osoby[2].split("-")
            dob = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))
            self.osoby.append(Osoba(dane_osoby[0], dane_osoby[1], dob, dane_osoby[3], dane_osoby[4], dane_osoby[5], dane_osoby[6], dane_osoby[7]))