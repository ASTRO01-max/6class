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
    def __init__(self, bank_name, account_num, payment, cash=1200):
        self.bank_name = bank_name
        self.cash = cash
        self.__account_num = account_num
        self.payment = payment

    def pay(self, product):
        if self.cash < product:
            return "xisobingizda yetarlicha pul yo'q!"
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

class Security:
    def __init__(self, p_id, password=1234, login="user", admin="admin"):
        self.password = password
        self.login = login
        self.admin = admin
        self.__p_id = id()
        self.attempts = []
        self.is_authenticated = False

    def security(self, ent_pass, ent_log, ent_admin):
        if ent_pass == self.password and ent_log == self.login and ent_admin == self.admin:
            print(f"Barcha xafsizlik ma'lumotlari to'g'ri"
                  f"Foydalanuvchining ID raqami: {self.__p_id}")
            self.attempts.clear()
            
        else:
            self.attempts.append(1)

        if len(self.attempts) >= 5:
            print(f"urunishlar soni 5tadan oshib ketti siz bloklandingiz! {len(self.attempts)}")

    def change_password(self, old_password, new_password):
        if not self.is_authenticated:
            print(f"Parolni o'zgartirish uchun avval tizimga kiring!")

        if len(self.attempts) >= 5:
            print(f"Siz bloklangansiz! Parolni o'zgartira olmaysiz.")

        if old_password == self.password:
            self.password = new_password
            print(f"Parol muvaffaqiyatli o'zgartirildi!")
            print(f"Yangi parol IDsi: {self.__p_id}")
            self.attempts.clear()

        else:
            self.attempts.append(1)
            print(f"Eski parol noto'g'ri! Urinishlar soni: {len(self.attempts)}/5")         

class Insurance:
    def __init__(self, company, policy_number, coverage_amount, expiration_date):
        self.company = company
        self.policy_number = policy_number
        self.coverage_amount = coverage_amount
        self.expiration_date = expiration_date

    def info(self):
        return (f"Sug'urta kompaniyasi: {self.company}\n"
                f"Sug'urta polisi raqami: {self.policy_number}\n"
                f"Sug'urta qamrovi: {self.coverage_amount} USD\n"
                f"Muddati tugash sanasi: {self.expiration_date}")

    def extend_policy(self, additional_years):
        return f"Sug'urta muddati {additional_years} yilga uzaytirildi."

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



