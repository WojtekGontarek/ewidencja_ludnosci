from datetime import date


class Adres:
    def __init__(self, miejscowosc:str, ulica:str, kod:str, numer_domu:str):
        self.ulica = ulica
        self.miejscowosc = miejscowosc
        self.kod = kod
        self.numer_domu = numer_domu

    def __str__(self) -> str:
        return f"{self.miejscowosc};{self.ulica};{self.kod};{self.numer_domu}"

class Osoba:
    def __init__(self, imie:str, nazwisko:str, dob:date, pesel:str, miejscowosc:str, ulica:str, kod:str, numer_domu:str):
        self.adres = Adres(miejscowosc, ulica, kod, numer_domu)
        self.imie = imie
        self.nazwisko = nazwisko
        self.dob = dob
        self.waliduj_pesel(pesel)
        self.pesel = pesel


    def __str__(self) -> str:
        return f"{self.imie};{self.nazwisko};{self.dob};{self.pesel};{self.adres}"

    def walifuj_cyfre_kontrolna(self):
        wagi = [1,3,7,9,1,3,7,9,1,3]
        suma = 0
        for i in range(len(self.pesel)):
            suma += wagi[i]*self.pesel[i]
        return suma//10==self.pesel[-1]


    def waliduj_pesel(self, pesel):
        # TODO walidacja peselu: dlugosc, sklad, cyfra kontrolna, data urodzenia
        cyfra_stulecia = 0 if self.dob.year<=1999 else 20
        if len(pesel) != 11 \
                or not pesel.isnumeric()\
                or pesel[:2] != str(self.dob.year)[2:4]\
                or pesel[2:4] != str(self.dob.month+cyfra_stulecia)\
                or str(int(pesel[4:6])) != str(self.dob.day):
            raise ValueError("Bledny PESEL")
        else:
            return "sdf"


