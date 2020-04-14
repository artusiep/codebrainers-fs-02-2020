konto1 = {
    'stan': 0,
    'imie': 'Artur',
    'nazwisko': 'Siepietowski',
    'numer': 12334514
}


# Pierwsza implementacja (zwracanie wartości)
def wplac(kwota, stan):
    return stan + kwota


konto1['stan'] = wplac(1000, konto1['stan'])
print(konto1['stan'])


def wyplac(kwota, stan):
    return stan - kwota


konto1['stan'] = wyplac(50, konto1['stan'])
print(konto1['stan'])


# def zmien_naziwsko(nowe):
#     return nowe
#
#
# konto1['nazwisko'] = zmien_naziwsko("BlaBla")
#
# print(konto1)

# Druga Implementacja (przekazanie słownika)

def wplac2(kwota, konto):
    konto['stan'] = konto['stan'] + kwota


wplac2(10000, konto1)
print(konto1)


def wyplac2(kwota, konto):
    konto['stan'] = konto['stan'] - kwota


wyplac2(500, konto1)
print(konto1)
