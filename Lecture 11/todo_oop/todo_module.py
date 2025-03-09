class BadPriorityError(Exception):
    """Класс для обработки ошибок приоритета задачи."""

    def __init__(self, priority, message):
        self.priority = priority
        self.message = message

    def __str__(self):
        return f"BadPriorityError: {self.priority} - {self.message}"


class BadIdError(Exception):
    """Класс для обработки ошибок индекса задачи."""

    def __init__(self, tid, message):
        self.id = tid
        self.message = message

    def __str__(self):
        return f"BadIdError: {self.id} - {self.message}"


class BadNameError(Exception):
    """Класс для обработки ошибок неверно введённого имени задачи."""

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return f"BadNameError: {self.name} - {self.message}"


class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"Задача: {self.name}, приоритет: {self.priority}"


class TodoList:
    """Класс по списку задач"""
    auto_id = 1

    def __init__(self):
        self.__storage = {}


    def create(self, name, priority):
        """Метод по созданию задачи."""
        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов")
        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100")
        self.__storage.update({TodoList.auto_id: Task(name, priority)})
        TodoList.auto_id += 1

        return True


    def read(self, tid):
        """Метод по чтению задачи по их id."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1")

        if tid not in self.__storage:
            raise BadIdError(tid, "Номер задачи НЕ содержится")

        return self.__storage.get(tid)

    def read_all(self):
        """Метод для чтения всех задач."""
        res = "Список задач:\n"
        for k, v in self.__storage.items():
            res += f"id: {k} - {v}\n"
        return res

    def update(self, tid, name, priority):
        """Метод по обновлению задачи"""

        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1")

        if tid not in self.__storage:
            raise BadIdError(tid, "Номер задачи НЕ содержится")

        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов")

        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100")

        self.__storage.update({tid: Task(name, priority)})

        return True

    def delete(self, tid):
        """Метод по удалению задачи по id."""

        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1")

        if tid not in self.__storage:
            raise BadIdError(tid, "Номер задачи НЕ содержится")

        self.__storage.pop(tid)

        return True


class App:
    def __init__(self):
        self.__todolist = TodoList()

    def Run(self):
        """Основной метод для работы co сценариями."""

        condition = input(App.condition_display())
        while condition != "-1":
            try:
                if condition == "1":  # Создание задачи
                    name = input("Введите имя: ")
                    priority = int(input("Введите приоритет: "))
                    self.__todolist.create(name, priority)
                elif condition == "2":  # Просмотр всех задач
                    print(self.__todolist.read_all())
                elif condition == "3":  # Просмотр задачи
                    tid = int(input("Введите индекс: "))
                    print(self.__todolist.read(tid))
                elif condition == "4":  # Обновление задачи
                    tid = int(input("Введите индекс: "))
                    name = input("Введите имя: ")
                    priority = int(input("Введите приоритет: "))
                    self.__todolist.update(tid, name, priority)
                elif condition == "5":  # Удаление задачи
                    tid = int(input("Введите индекс: "))
                    self.__todolist.delete(tid)
                elif condition == "-1":  # Выход
                    print("Пока пока...")

            except BadIdError as e:
                print("Ошибка: ", e)
            except BadPriorityError as e:
                print("Ошибка: ", e)
            except BadNameError as e:
                print("Ошибка: ", e)
            except Exception as e:
                print("Неизвестная ошибка! ", e)

            condition = input("Выберите операцию: ")


    @staticmethod
    def condition_display():
        """Отображение меню"""
        return """
        Номер задачи(от 1)
        Имя задачи(не менее 7 символов)
        Приоритет(от 1 до 100)
        1 - добавление новой задачи,
        2 - просмотр списка задач,
        3 - просмотр задачи по id,
        4 - обновление задачи по id,
        5 - удаление задачи по id,
        -1 - выход из программы.
        """
