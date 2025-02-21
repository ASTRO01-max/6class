from abc import ABC, abstractmethod
from uuid import uuid4 as id
import json

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
    
    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "km": self._km
        }

class Car(Vehicle):
    def __init__(self, brand, model, year, price, warranty, km=0):
        super().__init__(brand, model, year, price, km)
        self._warranty = warranty  

    def info(self):
        return f"Mashina nomi: {self.brand}, Modeli: {self.model}, Yili: {self.year}, Narxi: {self.price}"

    def warranty(self):
        return f"Kafolat muddati: {self._warranty} yil"

class Electronic(Vehicle):
    def __init__(self, brand, model, year, price, electricity, battery, km=0):
        super().__init__(brand, model, year, price, km)
        self.electricity = electricity
        self._battery = battery  

    def info(self):
        return (f"Mashina nomi: {self.brand}, Modeli: {self.model}, Yili: {self.year}, Narxi: {self.price}, "
                f"Mashina turi: {self.electricity}, Batareya quvvati: {self._battery} kWh")

    def warranty(self):
        return "Elektr avtomobillari uchun kafolat shartlari belgilanmagan."

class Truck(Vehicle):
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
        self._power = power  
        self._warranty = warranty  

    def info(self):
        return (f"Mashina nomi: {self.brand}, Modeli: {self.model}, Yili: {self.year}, Narxi: {self.price}, "
                f"Ot kuchi: {self._power} HP")

    def warranty(self):
        return f"Kafolat muddati: {self._warranty} yil"
    
class Parking:
    def __init__(self, residence, num):
        self.residence = residence
        self.num = num
        self.__r_id = id()
        self.lst = []

    def parking(self):
        if self.num in self.lst:
            return "Bu joy band!"
        else:
            self.lst.append(self.num)
            return (f"Turar joy nomi: {self.residence}, "
                    f"turar joy raqami: {self.num}, "
                    f"turar joy id raqami: {self.__r_id}")

class Payment:
    def __init__(self, bank_name, account_num, payment, my_card, cash=1200):
        self.bank_name = bank_name
        self.cash = cash
        self.__account_num = account_num
        self.payment = payment
        self.__my_card = my_card

    def pay(self, product):
        if self.cash < product:
            return "xisobingizda yetarlicha pul yo'q!"
        
        elif self.cash > product:
            return f"hisobingiz: {self.__my_card}"
        else:
            return f"Bank nomi: {self.bank_name}, hisob raqami: {self.__account_num}, to'lov miqdori: {self.payment}"

class Servis:
    def __init__(self, contract, insurance=10, contract_term=10):
        self.contract = contract
        self.insurance = insurance
        self.contract_term = contract_term
        self.__contract_id = id()

    def info(self):
        return (f"Shartnoma ID raqami: {self.__contract_id}\n"
                f"Sizning shartnomangiz muddati: {self.contract_term} yil\n"
                f"Sug'urta muddati: {self.insurance} yil")
    
class Customer:
    def __init__(self, name, fam, call_num, address):
        self.name = name
        self.fam = fam
        self.call_num = call_num
        self.address = address

    def info(self):
        return (f"Mijoz ismi: {self.name} {self.fam}\n"
                f"Telefon raqami: {self.call_num}\n"
                f"Manzil: {self.address}")

     
class Sales:
    def __init__(self):
        self.sold_cars = [] 

    def add(self, car, price):
        car_id = str(id())  
        self.sold_cars.append({"Mashina": car, "Narxi": price, "id": car_id})
        return f"{car.info()} xaridlar ro'yhatiga qo'shildi, ID: {car_id}"
    
    def remove(self, carr):
        for i in self.sold_cars:
            if i["Mashina"] == carr:
                self.sold_cars.remove(i)
                return f"{carr.info()}, savatdan olib tashlandi!!!"
        return f"{carr.info()} savatda topilmadi"

    def show_sold_cars(self):
        if not self.sold_cars:
            print("Hali hech qanday mashina yo'q.")
        else:
            print("Olingan mashinalar:")
            for car in self.sold_cars:
                print(car["Mashina"].info())  

    def total_price(self):
        summa = sum(car["Narxi"] for car in self.sold_cars)
        return f"Umumiy narx: {summa} USD"


car1 = Car("Toyota", "Camry", 2022, 30000, 5)
car2 = Electronic("Tesla", "Model S", 2023, 80000, "Elektr", 100)
car3 = Truck("Volvo", "FH16", 2021, 120000, 3, 30)
car4 = Super("Ferrari", "F8", 2023, 250000, 3, 710)

sales = Sales()

print(sales.add(car1, car1.price))
print(sales.add(car2, car2.price))
print(sales.add(car3, car3.price))
print(sales.add(car4, car4.price))

print(sales.remove(car3))  

print("________________________________________")
print(sales.total_price())
sales.show_sold_cars()

path = "orders.json"

def read():
    with open(path, "r") as file:
        data = json.load(file)
    return data

def write(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

menu = ("1 - saqlash\n"
        "2 - o'qish\n"
        "3 - chiqib ketish\n")

while True:
    print("\n", menu)
    choice = input("Enter num: ").strip()

    if choice == "1":
        users = read()
        users += [car.to_dict() for car in [car1, car2, car4]]  
        write(users)
        print("Data saved.")

    elif choice == "2":
        users = read()
        if not users:
            print("Ma'lumotlar mavjud emas.")
        else:
            for user in users:
                print(user)
    
    elif choice == "3":
        print("Dastur yakunlandi.")
        break


