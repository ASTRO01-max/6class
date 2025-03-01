from modul import Car, Electronic, Truck, Super, Sales
import json

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
