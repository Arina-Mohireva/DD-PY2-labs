import doctest


class Ipoteka:
    def __init__(self, capital: int, cost_aparment: int, salary: int):
        """
        Создание и подготовка к работе объекта "Ипотека"
        :param capital: первоначальный взнос
        :param cost_aparment: цена квартиры
        :param salary: доход
        Примеры:
        >>> ipoteka = Ipoteka(1350000, 9000000, 100000)  # инициализация экземпляра класса
        """
        if not isinstance(capital, int):
            raise TypeError("Ваш первоначальный взнос должен быть целым числом!")
        if capital <= 0.15 * cost_aparment:
            raise ValueError("Ваш первоначальный взнос должен быть больше 15% от стоимости квратиры!")
        self.capital = capital

        if not isinstance(cost_aparment, int):
            raise TypeError("Цена квартиры должна быть целым числом!")
        if cost_aparment < 0:
            raise ValueError("Цена квартиры не может быть отрицательным числом")
        self.cost_aparment = cost_aparment

        if not isinstance(salary, int):
            raise TypeError("Заработная плата должна быть целым числом")
        if salary < 80000:
            raise ValueError("Ваш доход должен быть больше 80 тысяч рублей!")
        self.salary = salary

    def is_take_ipoteka(self) -> bool:
        """
        Функция которая проверяет можно ли взять ипотеку
        :return: Можно ли взять ипотеку
        Примеры:
        >>> ipoteka = Ipoteka(1350000, 9000000, 100000)
        >>> ipoteka.is_take_ipoteka(True)
        """
        ...

    def early_repayment(self, money: int) -> None:
        """
        Функция котороя проверяет сумму долга при досрочном погашении.
        :param money: Сумма досрочного погашения
        :raise ValueError: Если Сумма досрочного погашения превышает остаток долга, то вызываем ошибку
        Примеры:
        >>> ipoteka = Ipoteka(1350000, 9000000, 100000)
        >>> ipoteka.early_repayment()
        """
        if not isinstance(money, int):
            raise TypeError("Сумма досрочного погашения должна быть целым числом")
        if money < 0:
            raise ValueError("Сумма досрочного погашения должна положительным числом")
        self.money = money
        ...

    def full_repayment(self, interest_rate: float) -> None:
        """
        Функция считает сумму выплаечнных процентов, при полном погашении.
        :param interest_rate: процентная ставка
        :raise ValueError: если сумма выплаченных процентов превышает стоимость квартиры, вызываем ошибку .
        :return: Выплаченные проценты
        Примеры:
        >>> ipoteka = Ipoteka(1350000, 9000000, 100000)
        >>> ipoteka.interest_rate(11)
        """
        if not isinstance(interest_rate, int):
            raise TypeError("Процентная ставка должна быть целым числом")
        if interest_rate < 0:
            raise ValueError("Процентная ставка должна положительным числом")
        self.interest_rate = interest_rate
        ...

class Bottle:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бутылка"
        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> glass = Bottle(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть целыи или вещественным числом")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли бутылка пустой
        :return: Является ли бутылка пустой
        Примеры:
        >>> glass = Bottle(500, 0)
        >>> glass.is_empty_glass()
        """
        ...

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку
        Примеры:
        >>> glass = Bottle(500, 0)
        >>> glass.add_water_to_glass(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Количество добавляемой жидкоси должно быть целыи или вещественным числом")
        if water < 0:
            raise ValueError("Количество добавляемой жидкости не может быть отрицательным числом")
        ...

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из бутылки.
        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в бутылке,
        то возвращается ошибка.
        :return: Объем реально извлеченной жидкости
        Примеры:
        >>> glass = Bottle(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        ...

class Bedside:
    def __init__(self, number_boxes: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Тумбочка"
        :param number_boxes: количество ящиков
        :param occupied_volume: Объем тумбочки
        Примеры:
        >>> glass = Bedside(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(number_boxes, (int, float)):
            raise TypeError("Количество ящиков должено быть целым или вещественным числом")
        if number_boxes <= 0:
            raise ValueError("Количество ящиков должено быть положительным числом")
        self.capacity_volume = number_boxes

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем тумбочки должен быть целым или вещественным числом")
        if occupied_volume < 0:
            raise ValueError("Объем тумбочки должен быть положительным числом")
        self.occupied_volume = occupied_volume

    def is_empty_bedside(self) -> bool:
        """
        Функция которая проверяет является ли тумбочка пустой
        :return: Является ли тумбочка пустой
        Примеры:
        >>> bedside = Bedside(500, 0)
        >>> bedside.is_empty_bedside()
        """
        ...

    def add_stuff_to_bedside(self, stuff: int) -> None:
        """
        Добавление вещей в тумбочку.
        :param stuff: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку
        Примеры:
        >>> bedside = Bedside(500, 0)
        >>> bedside.add_stuff_to_bedside(10)
        """
        if not isinstance(stuff, int):
            raise TypeError("Количество добавленных вещей должно быть целым числом")
        if stuff < 0:
            raise ValueError("Количество добавленных вещей должно быть положительным числом")
        ...

    def remove_stuff_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение вещей из тумбочки.
        :param estimate_water: Объем извлекаемых вещей
        :raise ValueError: Если количество извлекаемых вещей превышает колчиство вещей в тумбочке,
        то возвращается ошибка.
        :return: Объем извлеченных вещей
        Примеры:
        >>> bedside = Bedside(50, 50)
        >>> bedside.remove_stuff_from_glass(10)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
