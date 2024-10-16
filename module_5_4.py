class House:
    houses_history = []  # Атрибут класса для хранения названий созданных объектов

    def __new__(cls, *args):
        # Создание нового объекта
        instance = super(House, cls).__new__(cls)

        if args:
            house_name = args[0]
            cls.houses_history.append(house_name)  # Добавляем название дома в историю
            instance.name = house_name
        return instance

    def __init__(self, *args):
        self.floors = args[1]  # Количество этажей

    def __del__(self):
        # Вызов метода при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"


home1 = House("ЖК Эльбрус", 10)
home2 = House("ЖК Альбатрос", 16)
home3 = House("ЖК Парус", 23)

# Проверяем значение атрибута houses_history
print("История созданных домов:", House.houses_history)

del home1

# Проверяем значение атрибута houses_history после удаления
print("История после удаления:", House.houses_history)

# Удаляем следующие дома для проверки
del home2
del home3
