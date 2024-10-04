from datetime import datetime

class Car:
    def __init__(self, id, brand, model, year, color, price, reg_number, tuning=False):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.reg_number = reg_number
        self.tuning = tuning
    
    # Геттеры
    def get_id(self):
        return self.id

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_reg_number(self):
        return self.reg_number

    def get_tuning(self):
        return self.tuning
    
    # Сеттеры
    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def set_reg_number(self, reg_number):
        self.reg_number = reg_number

    def set_tuning(self, tuning):
        self.tuning = tuning

    # Переопределение метода для строкового представления объекта
    def __str__(self):
        return f"Car(id={self.id}, brand={self.brand}, model={self.model}, year={self.year}, color={self.color}, price={self.price}, reg_number={self.reg_number}, tuning={self.tuning})"

    # Переопределение метода для хеширования объекта
    def __hash__(self):
        return hash((self.id, self.brand, self.model, self.year, self.reg_number))


class CarManager:
    def __init__(self, cars=None):
        self.cars = cars if cars else []

    def add_car(self, car):
        self.cars.append(car)

    # Метод для получения списка автомобилей по марке
    def get_by_brand(self, brand):
        return [car for car in self.cars if car.get_brand() == brand]

    # Метод для получения списка автомобилей по модели и возрасту эксплуатации
    def get_by_model_and_years(self, model, years):
        current_year = datetime.now().year
        return [car for car in self.cars if car.get_model() == model and (current_year - car.get_year()) > years]

    # Метод для получения списка автомобилей по году выпуска и цене
    def get_by_year_and_price(self, year, min_price):
        return [car for car in self.cars if car.get_year() == year and car.get_price() > min_price]


car1 = Car(1, "Toyota", "Corolla", 2015, "Black", 8000, "A123BC")
car2 = Car(2, "Toyota", "Camry", 2010, "White", 12000, "B456DE")
car3 = Car(3, "Honda", "Civic", 2018, "Red", 15000, "C789FG")
car4 = Car(4, "Ford", "Focus", 2016, "Blue", 9000, "D012HI")
manager = CarManager([car1, car2, car3, car4])

print("Автомобили марки Toyota:")
for car in manager.get_by_brand("Toyota"):
    print(car)

print("\nАвтомобили модели, эксплуатируемые больше 5 лет:")
for car in manager.get_by_model_and_years("Civic", 5):
    print(car)

print("\nАвтомобили 2016 года выпуска с ценой больше 8000:")
for car in manager.get_by_year_and_price(2016, 8000):
    print(car)
