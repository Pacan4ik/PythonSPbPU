class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Название должно быть str")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("Автор должно быть str")
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть int.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть > 0.")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть > 0.")
        self._duration = float(value)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    book = Book("book", "<NAME>")
    paper_book = PaperBook("paper book", "<NAME>", 100)
    audiobook = AudioBook("audiobook", "<NAME>", 100)

    print(book)
    print(paper_book)
    print(audiobook)
