from abc import ABC, abstractmethod
from uuid import uuid4 as id

class Vehicle(ABC):
    def __init__(self, brand, model, year, price, km=0):
        self._km = km
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def warranty(self):
        pass

    def get_km(self):
        return f"{self._km} km yurgan"

class Car(Vehicle):
    def __init__(self, brand, model, year, price, warranty, km=0):
        super().__init__(brand, model, year, price, km)
        self.__warranty = warranty

    def info(self):
        return f"Mashina nomi: {self.brand}, Modeli: {self.model}, Yili: {self.year}, Narxi: {self.price}"

    def warranty(self):
        return f"Kafolat muddati: {self.__warranty} yil"

class Electronic(Vehicle):
    def __init__(self, brand, model, year, price, electricity, battery, km=0):
        super().__init__(brand, model, year, price, km)
        self.electricity = electricity
        self.__battery = battery

    def info(self):
        return (f"Mashina nomi: {self.brand}, Modeli: {self.model}, Yili: {self.year}, Narxi: {self.price}, "
                f"Mashina turi: {self.electricity}, Batareya quvvati: {self.__battery} kWh")

    def warranty(self):
        return "Elektr avtomobillari uchun kafolat shartlari belgilanmagan."

class Truck(Car):
    def __init__(self, brand, model, year, price, warranty, capacity, km=0):
        super().__init__(brand, model, year, price, warranty, km)
        self.capacity = capacity

    def info(self):
        return super().info() + f", Yuk ko'tarish hajmi: {self.capacity} tonna"

    def warranty(self):
        return "Yuk mashinalari uchun kafolat shartlari belgilanmagan."

class Super(Vehicle):  
    def __init__(self, brand, model, year, price, warranty, power, km=0):
        super().__init__(brand, model, year, price, km)
        self.__power = power
        self.__warranty = warranty

    def info(self):
        return (f"Mashina nomi: {self.brand}, Modeli: {self.model}, Yili: {self.year}, Narxi: {self.price}, "
                f"Ot kuchi: {self.__power} HP")

    def warranty(self):
        return f"Kafolat muddati: {self.__warranty} yil"

class Sales:
    def __init__(self):
        self.__id = id()
        self.sold_cars = [] 

    def add(self, car, price):
        car_id = self.__id
        self.sold_cars.append({"Mashina": car, "Narxi": price, "id" : car_id})
        return f"{car} xaridlar ro'yhatiga qo'shildi, idsi{car_id}"

    def total_price(self):
        summa = 0
        for i in self.sold_cars:
            summa += i["Narxi"]
        return f"Umumiy narx: {summa} USD"
    
    def show_sold_cars(self):
        if not self.sold_cars:
            print("Hali hech qanday mashina yo'q.")
        else:
            print("Olingan mashinalar:")
            for car in self.sold_cars:
                print(car.info())

