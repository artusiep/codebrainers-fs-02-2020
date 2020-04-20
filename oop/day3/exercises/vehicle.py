# Napisz program który będzie składal się z 3 klas.
# Pierwsza klasa nazwana będzie `Vehicle` i będzie klasą bazową
# dla pozostałych tj. `Bus`, `Truck`.
# Klasa bazowa będzie posiadać prywatne atrybuty takie jak:
# _driving_cost -> reprezentujący składową kosztu wykonania metody drive()
# _per_passenger_cost -> reprezentujacy składową kosztu wykonania metody drive() pomnożoną przez ilośc pasażerów
# _passenger_limit -> limit osób mogących znaleść się w pojeździe
# _passenger_no -> ilość osób mogących znaleść się w pojeździe musi być zawsze większa od jeden
# _fuel_tank -> reprezentujacy obecny poziom paliwa w pojeździe
# Klasa `Vehicle` będzie miała zdefiniowane metody takie jak `drive` -> redukuje ilość dostępnego paliwa o `_driving_cost` plus dodatkowo `_per_passenger_cost` za każdego pasażera, jeżeli w trakcie ilość paliwa spadnie do zera to operacja `drive` się nie udaje i każde kolejne wykonanie operacji drive nie zadziała,
# `check_fuel` -> pokazuje stan paliwa, `find_petrol_station` -> wykonuje operacje drive i jeżeli się uda to tankuje paliwo, `check_passenger` -> sprawdza ilość pasażerów
# Klasa `Bus` będzie miała zdefiniowaną metodę `take_passager` która będzie dodawać losową liczbę osób (z zakresu 0 do 5) do obecnie znajdujących się w pojeździe
# Klasa `Bus` będzie miała zdefiniowaną metodę `unload_passager` która będzie usuwać wszystkich pasażerów
# Klasa `Truck` będzie miała metody `take_cargo`, `unload_cargo` które odpwiednio będą losowały wartości float i przypisywały do pola należącego tylko do obieku `Truck` o nazwie `_cargo_weight`.
# Dla metody `drive` w klasie `Truck` wywołana zostanie metoda z `drive` z klasy bazowej, a następnie wartość paliwa (_fuel_tank) obniży się o `_cargo_weight` * 0,5

# Niekiedy instrukcja dotycząca tego zadania nie jest kompletna w takim momecie należy zapytać się
import random


class Vehicle:
    _driving_cost = None
    _per_passenger_cost = None
    _passenger_limit = None
    _passenger_no = None
    _fuel_tank = None
    _fuel_limit = None

    def drive(self):
        self._fuel_tank -= self._driving_cost
        self._fuel_tank -= self._per_passenger_cost * self._passenger_no
        if self._fuel_tank < 0:
            self._fuel_tank = 0
            raise Exception('Warning! No fuel')
        print("I'm driving")

    def check_fuel(self):
        return self._fuel_tank

    def find_petrol_station(self):
        self.drive()
        self._fuel_tank = self._fuel_limit

    def check_passenger(self):
        return self._passenger_no


class Bus(Vehicle):
    _driving_cost = 30
    _per_passenger_cost = 4
    _passenger_limit = 100
    _passenger_no = 1
    _fuel_tank = 1500
    _fuel_limit = 3000

    def take_passenger(self):
        self._passenger_no += random.randint(0, 5)
        if self._passenger_no > self._passenger_limit:
            self._passenger_no = self._passenger_limit
            raise Exception('Warning! Passenger limit exceeded')

    def unload_passenger(self):
        self._passenger_no = 1


class Truck(Vehicle):
    _driving_cost = 90
    _per_passenger_cost = 40
    _passenger_limit = 3
    _passenger_no = 1
    _fuel_tank = 1500
    _fuel_limit = 3000
    _cargo_weight = 333
    _cargo_limit = 1333

    def take_cargo(self):
        self._cargo_weight += random.random() * 100
        if self._cargo_weight > self._cargo_limit:
            self._cargo_weight = self._cargo_limit
            raise Exception('Warning! Cargo limit exceeded')

    def unload_cargo(self):
        self._cargo_weight -= random.random() * 100
        if self._cargo_weight < 0:
            self._cargo_weight = 0
            raise Exception('Warning! Cargo unloaded')

    def drive(self):
        self._fuel_tank -= self._cargo_weight * 0.05
        super().drive()


bs = Bus()
tr = Truck()
print(bs.check_fuel())
bs.take_passenger()
bs.drive()
print(bs.check_fuel())
bs.take_passenger()
bs.drive()
print(bs.check_fuel())
bs.take_passenger()
bs.drive()
print(bs.check_fuel())
bs.unload_passenger()
print(bs.check_fuel())
