class BadShelfError(Exception):
    """Класс для обработки ошибок местонахождения товара"""

    def __init__(self, shelf, message):
        self.shelf = shelf
        self.message = message

    def __str__(self):
        return f"BadShelfError: {self.shelf} - {self.message}"


class BadIdError(Exception):
    """Класс для обработки ошибок id товара"""

    def __init__(self, tid, message):
        self.id = tid
        self.message = message

    def __str__(self):
        return f"BadIdError: {self.id} - {self.message}"


class BadProductError(Exception):
    """Класс для обработки ошибок неверно введённого названия товара"""

    def __init__(self, product, message):
        self.product = product
        self.message = message

    def __str__(self):
        return f"BadProductError: {self.product} - {self.message}"


class Product:
    """Класс по товару на складе"""

    def __init__(self, product, shelf):
        self.product = product
        self.shelf = shelf

    def __str__(self):
        return f"Товар: {self.product}, стеллаж: {self.shelf}"


class Warehouse:
    """Класс по списку товаров на складе"""

    auto_id = 1

    def __init__(self):
        self.__storage = {}


    def create(self, product, shelf):
        """Метод по созданию товара"""

        if len(product) < 3:
            raise BadProductError(product, "Название должно быть более 2 символов")
        if shelf < 1 or shelf > 100:
            raise BadShelfError(shelf, "№ стеллажа должен быть от 1 до 100")

        self.__storage.update({Warehouse.auto_id: Product(product, shelf)})
        Warehouse.auto_id += 1

        return True


    def read(self, tid):
        """Метод для поиска товара по id"""

        if tid < 1:
            raise BadIdError(tid, "Номер товара от 1")

        if tid not in self.__storage:
            raise BadIdError(tid, "Такого товара нет")

        return self.__storage.get(tid)


    def read_all(self):
        """Метод для получения всех товаров на складе"""

        res = "Список товаров:\n"
        for k, v in self.__storage.items():
            res += f"id: {k} - {v}\n"
        return res


    def update(self, tid, shelf):
        """Метод по переносу товара на другой стеллаж"""

        if tid < 1:
            raise BadIdError(tid, "Номер товара от 1")
        if tid not in self.__storage:
            raise BadIdError(tid, "Такого товара нет")
        if shelf < 1 or shelf > 100:
            raise BadShelfError(shelf, "№ стеллажа должен быть от 1 до 100")

        res = self.__storage.get(tid)
        product = res.product
        self.__storage.update({tid: Product(product, shelf)})

        return True

    def delete(self, tid):
        """Метод по выдаче(удалению) товара со склада"""

        if tid < 1:
            raise BadIdError(tid, "Номер товара от 1")
        if tid not in self.__storage:
            raise BadIdError(tid, "Такого товара нет")

        self.__storage.pop(tid)

        return True


class App:
    def __init__(self):
        self.__todolist = Warehouse()

    def Run(self):
        """Основной метод для работы co сценариями."""

        condition = input(App.condition_display())
        while condition != "-1":
            try:
                if condition == "1":  # Прием товара на склад
                    product = input("Введите название: ")
                    shelf = int(input("Введите стеллаж: "))
                    self.__todolist.create(product, shelf)
                elif condition == "2":  # Просмотр всего товара на складе
                    print(self.__todolist.read_all())
                elif condition == "3":  # Просмотр товара по id
                    tid = int(input("Введите id: "))
                    print(self.__todolist.read(tid))
                elif condition == "4":  # Перемещение товара на другой стеллаж
                    tid = int(input("Введите id: "))
                    shelf = int(input("Введите стеллаж: "))
                    self.__todolist.update(tid, shelf)
                elif condition == "5":  # Выдача(удаление) товара со склада
                    tid = int(input("Введите id: "))
                    self.__todolist.delete(tid)
                elif condition == "-1":  # Выход из программы
                    print("Пока пока...")

            except BadIdError as e:
                print("Ошибка: ", e)
            except BadShelfError as e:
                print("Ошибка: ", e)
            except BadProductError as e:
                print("Ошибка: ", e)
            except Exception as e:
                print("Неизвестная ошибка! ", e)

            condition = input("Выберите операцию: ")


    @staticmethod
    def condition_display():
        """Отображение меню"""
        return """
        Название товара (не менее 3 символов)
        Стеллаж (от 1 до 100)
        1 - добавление нового товара,
        2 - просмотр товаров на складе,
        3 - просмотр товара по id,
        4 - перемещение товара на другой стеллаж по id,
        5 - выдача товара со склада по id,
        -1 - выход из программы.
        """
