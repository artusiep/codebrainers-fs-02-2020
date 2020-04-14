# Implementacja obiektowa

class Konto:
    def __init__(self, stan_poczatkowy, imie, naziwsko):
        print("Jestem Konstuktorem")
        self.stan = stan_poczatkowy  # Pole w klasie, Class Field
        self.imie = imie
        self.nazwisko = naziwsko

    def __str__(self):
        return f"""Właściciel {self.imie} {self.nazwisko}
Stan: {self.stan}
"""

    def wplac(self, kwota):
        self.stan += kwota

    def wyplac(self, kwota):
        self.stan -= kwota
        return kwota

    def przelew(self, kwota, konto_docelowe):
        if not isinstance(kwota, int):
            raise Exception("Kwota nie moze być innego typu niz int")
        self.stan -= kwota
        konto_docelowe.stan += kwota


x = Konto(500, 'Artur', 'Siepietowski')
print(x)
y = Konto(404, "Jan", "Kowalski")
print(y)

try:
    x.przelew(600, y)
except Exception:
    print(f"Podana kwota 600 jest niepoprawna")

try:
    x.przelew("100", y)
except Exception:
    print(f"Podana kwota '100' jest niepoprawna")
print(x)
print(y)

# x.wplac(1000)
# print(x.stan, x.imie)
# portfel = x.wyplac(100)
# print(x.stan)
# print(f"Mam w portfelu {portfel}")
