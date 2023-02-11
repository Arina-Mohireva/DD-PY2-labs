cars = {  # создаем словарь
    'BMW': {    # марка машины
        'X5': {    # модель машины
            'xDrive30d M Sport Pro': dict(engine='дизель 3.0 л.', transmission='АКПП', force=6.8, car_body='crossower'),
        },    # модификация машины
        '4': {    # модель машины
            '420i xDrive': dict(engine='бензин 2.0 л.', transmission='АКПП', force=7.5, car_body='Купе'),
        }
    },
    'KAMAZ': {    # марка машины
            '5490': {   # модель машины
                '99010-87': dict(engine='дизель 12.0 л', transmission='МКПП', volume=400, count_fuel_tank=2),
                '014-87': dict(engine='дизель 12.0 л', transmission='МКПП', volume=400, count_fuel_tank=1)
            }    # модификация машины
        }
    }


class Car:
    """ Базовый класс книги. """
    def __init__(self, name: str, model: str, complictation: str):
        self.name = name
        self.model = model
        self.complictation = complictation
        self.setСonfig(complictation)

    def __str__(self) -> str:  # создаем функцию, которая возвращает информацию о машине для пользователя
        self.info = f"""Марка: {self.name}
Модель: {self.model}
Комплектация: {self.complictation}"""
        return self.info

    def __repr__(self) -> str:  # создаем функцию, которая возвращает информацию для разработчика
        self.info = f'{self.__class__.__name__}(name = {self.name!r}, model = {self.model!r}, complictation = ' \
                    f'{self.complictation!r}'
        return self.info + ')'

    def setСonfig(self, comlictation: str):  # создаем функцию, которая создает переменную для изменения
        self.config = cars.get(self.name).get(self.model).get(comlictation)

    def getСonfig(self) -> dict:  # создаем функцию, которая возвращает словарь с параметрами модификации
        return self.config


class CarB(Car):
    """ Дочерний класс Легковые автомобили (категория b) """
    def __init__(self, name: str, model: str, complictation: str):
        super().__init__(name, model, complictation)

    def setСonfig(self, comlictation: str):  # расширяем конструктор базового класса
        if comlictation == 'custom':  # условие, если пользователь хочет изменить комплектацию
            for i in self.config:
                print(f'{i}: {self.config.get(i)}')
            print('!!!Добавить - add, удалить - del, остановить процедуру - exit')
            while True:
                command = input('команда: ')  # создаем добавление комманды для выбора комлектации
                if command == 'add':  # добавляем модификацию и ее параметр
                    add_config = input('Введите модификацию и его параметр через пробел: ').split()
                    self.config.update({add_config[0]: add_config[1]})
                elif command == 'del':   # удаляем лишнюю модификацию и ее параметр
                    del_config = input('Введите модификацию для удаления: ')
                    self.config.pop(del_config, None)
                elif command == 'exit':   # выходим когда завершили добавление параметров модификации, чтобы увидеть
                    # конечный результат
                    break
                else:
                    print('Вы ввели не правильную команду')

        else:  # оставляем исходные параметры модификации
            super().setСonfig(comlictation)



class CarC(Car):
    """ Дочерний класс Грузовые автомобили (категория с) """
    def __init__(self, name: str, model: str, complictation: str):  # наследуем магчисекий метод str
        super().__init__(name, model, complictation)


x = CarB('BMW', 'X5', 'xDrive30d M Sport Pro')
print(x, end='\n\n')
print(repr(x), end='\n\n')
x.setСonfig('custom')
print(x.getСonfig())

