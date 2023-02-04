class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        self.info = f"Книга {self.__name}. Автор {self.__author}."
        return self.info

    def __repr__(self):
        self.programm_info = f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"
        return self.programm_info

    def errorMsg(self, er):  # функция для вывода сообщения об ошибке, если знаечние поля заполнено не првивльно
        print(f'Вы ввели не верное значение для {er}')

    def checkNumber(self, num: str) -> bool:  # функция для проверки является ли введенная строчка пользователем числом
        if num.isdigit():  # возвращает True, если все символы в строке являются цифрами
            return True
        else:
            num = num.replace('.', '', 1)  # заменяем точку в вещественном числе на "пустоту", единица  замену только
            # первой точки, если в строке больше точек
            if num.isdigit():
                return True
        return False


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: str):
        super().__init__(name, author)
        if self.checkNumber(pages):
            self.pages = int(pages)
        else:
            self.errorMsg('pages')

    def __str__(self):
        super().__str__()
        info = f'{self.info} Кол-во страниц: {self.pages}'
        return info

    def __repr__(self):
        super().__repr__()
        info = f'{self.programm_info[:-1]}, pages= {self.pages}'
        return info


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: str):
        super().__init__(name, author)
        if self.checkNumber(duration):
            self.duration = float(duration)
        else:
            self.errorMsg('duration')

    def __str__(self):
        super().__str__()
        info = f'{self.info} Продолжительность: {self.duration}'
        return info

    def __repr__(self):
        super().__repr__()
        info = f'{self.programm_info[:-1]}, duration= {self.duration})'
        return info

