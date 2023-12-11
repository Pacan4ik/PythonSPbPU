import doctest


class Bank:
    def __init__(self, account_holder: str, balance: float):
        """
        Создание и подготовка к работе объекта "Банк".

        :param account_holder: Владелец счета
        :param balance: Баланс счета

        Примеры:
        >>> bank_account = Bank("John Doe", 1000.0)  # инициализация экземпляра класса
        """
        if not isinstance(account_holder, str):
            raise TypeError("Имя владельца счета должно быть строкой")
        self.account_holder = account_holder

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс счета должен быть числом")
        if balance < 0:
            raise ValueError("Баланс счета не может быть отрицательным числом")
        self.balance = balance

    def get_balance(self) -> float:
        """
        Получение текущего баланса счета.

        :return: Текущий баланс счета

        Примеры:
        >>> bank_account = Bank("John Doe", 1000.0)
        >>> bank_account.get_balance()
        1000.0
        """
        return self.balance

    def deposit(self, amount: float) -> float:
        """
        Внесение денег на счет.

        :param amount: Сумма для внесения
        :return: Новый баланс счета после внесения денег

        Примеры:
        >>> bank_account = Bank("John Doe", 1000.0)
        >>> bank_account.deposit(500.0)
        1500.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма для внесения должна быть числом")
        if amount < 0:
            raise ValueError("Сумма для внесения не может быть отрицательной")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия
        :return: Новый баланс счета после снятия денег

        :raise ValueError: Если сумма для снятия превышает текущий баланс
        Примеры:
        >>> bank_account = Bank("John Doe", 1000.0)
        >>> bank_account.withdraw(200.0)
        800.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма для снятия должна быть числом")
        if amount < 0:
            raise ValueError("Сумма для снятия не может быть отрицательной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        return self.balance


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("The Great Gatsby", "F. Scott Fitzgerald", 200)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        self.author = author

        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.pages = pages

    def get_book_info(self) -> str:
        """
        Получение информации о книге.

        :return: Строка с информацией о книге

        Примеры:
        >>> book = Book("The Great Gatsby", "F. Scott Fitzgerald", 200)
        >>> book.get_book_info()
        'The Great Gatsby by F. Scott Fitzgerald, 200 pages'
        """
        return f'{self.title} by {self.author}, {self.pages} pages'


class Car:
    def __init__(self, make: str, model: str, year: int, fuel_type: str, distance: float):
        """
        Создание и подготовка к работе объекта "Автомобиль".

        :param make: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param fuel_type: Тип топлива (бензин, дизель, электро и т.д.)
        :param distance: Пробег автомобиля в километрах

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022, "Бензин", 15000.0)  # инициализация экземпляра класса
        """
        if not isinstance(make, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        self.make = make

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        self.model = model

        if not isinstance(year, int) or year < 1886:  # первый год автомобиля
            raise ValueError("Год выпуска автомобиля должен быть положительным целым числом")
        self.year = year

        if not isinstance(fuel_type, str):
            raise TypeError("Тип топлива должен быть строкой")
        self.fuel_type = fuel_type

        if not isinstance(distance, (int, float)) or distance < 0:
            raise ValueError("Пробег автомобиля должен быть положительным числом")
        self.distance = distance

    def get_car_info(self) -> str:
        """
        Получение информации о автомобиле.

        :return: Строка с информацией о автомобиле

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022, "Бензин", 15000)
        >>> car.get_car_info()
        '2022 Toyota Camry, Бензин, 15000 км'
        """
        return f'{self.year} {self.make} {self.model}, {self.fuel_type}, {self.distance} км'


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
