class TrainCar:
    def __init__(self, id, comfort_level):
        self.id = id
        self.comfort_level = comfort_level

    def get_id(self):
        return self.id

    def get_comfort_level(self):
        return self.comfort_level

    def get_passenger_count(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")

    def get_luggage_count(self):
        raise NotImplementedError("Метод должен быть реализован в подклассе")


class PassengerCar(TrainCar):
    def __init__(self, id, comfort_level, passenger_count, luggage_count):
        super().__init__(id, comfort_level)
        self.passenger_count = passenger_count
        self.luggage_count = luggage_count

    def get_passenger_count(self):
        return self.passenger_count

    def get_luggage_count(self):
        return self.luggage_count


class LuggageCar(TrainCar):
    def __init__(self, id, comfort_level, luggage_count):
        super().__init__(id, comfort_level)
        self.luggage_count = luggage_count

    def get_passenger_count(self):
        return 0  # В багажных вагонах пассажиров нет

    def get_luggage_count(self):
        return self.luggage_count


class Train:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    # Подсчет общего количества пассажиров
    def get_total_passengers(self):
        return sum(car.get_passenger_count() for car in self.cars)

    # Подсчет общего количества багажа
    def get_total_luggage(self):
        return sum(car.get_luggage_count() for car in self.cars)

    # Сортировка вагонов по уровню комфорта
    def sort_by_comfort_level(self):
        self.cars.sort(key=lambda car: car.get_comfort_level())

    # Поиск вагонов по диапазону количества пассажиров
    def find_cars_by_passenger_range(self, min_passengers, max_passengers):
        return [car for car in self.cars if min_passengers <= car.get_passenger_count() <= max_passengers]

    # Печать информации о поезде
    def print_train_info(self):
        for car in self.cars:
            print(f"Вагон ID: {car.get_id()}, Уровень комфорта: {car.get_comfort_level()}, "
                  f"Пассажиров: {car.get_passenger_count()}, Багаж: {car.get_luggage_count()}")


def main():
    train = Train()

    # Инициализация вагонов поезда
    train.add_car(PassengerCar(1, 3, 50, 100))
    train.add_car(PassengerCar(2, 2, 40, 80))
    train.add_car(LuggageCar(3, 1, 500))

    while True:
        print("\nМеню:")
        print("1. Посмотреть информацию о поезде")
        print("2. Подсчитать общее количество пассажиров")
        print("3. Подсчитать общее количество багажа")
        print("4. Отсортировать вагоны по уровню комфорта")
        print("5. Найти вагоны по количеству пассажиров")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            train.print_train_info()

        elif choice == "2":
            print(f"Общее количество пассажиров: {train.get_total_passengers()}")

        elif choice == "3":
            print(f"Общее количество багажа: {train.get_total_luggage()}")

        elif choice == "4":
            train.sort_by_comfort_level()
            print("Вагоны отсортированы по уровню комфорта.")

        elif choice == "5":
            min_passengers = int(input("Минимальное количество пассажиров: "))
            max_passengers = int(input("Максимальное количество пассажиров: "))
            cars = train.find_cars_by_passenger_range(min_passengers, max_passengers)
            if cars:
                print("Вагоны, удовлетворяющие условиям:")
                for car in cars:
                    print(f"Вагон ID: {car.get_id()}, Пассажиров: {car.get_passenger_count()}")
            else:
                print("Нет вагонов, удовлетворяющих заданным параметрам.")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
