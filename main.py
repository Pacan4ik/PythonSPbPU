class Document:
    """
    Базовый класс документа.

    Attributes:
        _title (str): Название документа.
        _size (int): Размер документа в байтах.
    """

    def __init__(self, title: str, size: int):
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(size, int):
            raise TypeError("Размер должен быть целым числом")
        self._title = title
        self._size = size

    @property
    def title(self) -> str:
        """
        Возвращает название документа.

        Returns:
            str: Название документа.
        """
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        """
        Устанавливает новое название документа.

        Args:
            new_title (str): Новое название документа.
        """
        self._title = new_title

    @property
    def size(self) -> int:
        """
        Возвращает размер документа в байтах.

        Returns:
            int: Размер документа в байтах.
        """
        return self._size

    def __str__(self) -> str:
        return f"Документ: {self.title}. Размер: {self.size}"

    def __repr__(self) -> str:
        return f"Document(title='{self.title}', size='{self.size}')"

    def generate_preview(self) -> str:
        """
        Генерирует предварительный просмотр документа.

        Returns:
            str: Предварительный просмотр содержания документа в виде первых нескольких строчек содержания
        """
        pass

    def delete_document(self) -> bool:
        """
        Метод для удаления документа.

        Returns:
            bool: Успешность удаления документа
        """
        pass


class Report(Document):
    """
    Дочерний класс, наследующий от базового класса Document.

    Attributes:
        _author (str): Автор отчета.
        _recipient (str): Получатель отчета.
    """

    def __init__(self, title: str, size: int, author: str, recipient: str):
        super().__init__(title, size)
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(recipient, str):
            raise TypeError("Получатель должен быть строкой")
        self._author = author
        self._recipient = recipient

    @property
    def author(self) -> str:
        """
        Возвращает автора отчета.

        Returns:
            str: Автор отчета.
        """
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """
        Устанавливает нового автора отчета.

        Args:
            new_author (str): Новый автор отчета.
        """
        self._author = new_author

    @property
    def recipient(self) -> str:
        """
        Возвращает получателя отчета.

        Returns:
            str: Получатель отчета.
        """
        return self._recipient

    @recipient.setter
    def recipient(self, new_recipient: str) -> None:
        """
        Устанавливает нового получателя отчета.

        Args:
            new_recipient (str): Новый получатель отчета.
        """
        self._recipient = new_recipient

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title='{self.title}', content='{self.size}', author='{self.author}', " \
               f"recipient='{self.recipient}')"

    def generate_preview(self) -> str:
        """
        Перегруженный метод для генерации предварительного просмотра отчета.

        Returns:
            str: Предварительный просмотр содержания отчета с указанием автора и получателя.
        """
        pass

    def send_report(self) -> bool:
        """
        Метод для отправки отчета.

        Returns:
            bool: Успешность отправки отчета
        """
        pass


if __name__ == "__main__":
    document = Document("Документ", 200)
    document.title = "ДОКУМЕНТ"
    document.generate_preview()

    print(document.__str__())
    print(document.__repr__())

    print("\n\n")

    report = Report("Отчет", 300, "Отправитель", "Получатель")
    # override
    report.generate_preview()

    report.send_report()
    # inherit
    report.delete_document()

    print(report.__str__())
    print(report.__repr__())

