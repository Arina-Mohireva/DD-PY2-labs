BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("параметр 'id' элемента 'Книга' должно быть целым числом!")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("параметр 'name' элемента 'Книга' должно являться строкой!")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("параметр 'pages' элемента 'Книга' должно быть целым числом!")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if len(self.books) <= 0:
            id_books = 1
        else:
            id_books = len(self.books) + 1
        return id_books

    def get_index_by_book_id(self, index_book=None):
        list = []
        for i in range(len(self.books)):
            list.append(self.books[i].id_)
        for index, current_id in enumerate(list):
            if current_id == index_book:
                index_book = index
        if index_book is None:
            raise ValueError("Книги с запрашиваемым id не существует")
        return index_book



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
