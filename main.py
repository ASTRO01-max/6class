from modul import Car, Electronic, Truck, Super, Sales

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
