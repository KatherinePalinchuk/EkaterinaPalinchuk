import doctest


class Book:
    """
    Документация на класс.
    Базовый класс описывает модель книги.
    """
    def __init__(self, name: str, author: str):
        """ Инициализация экземпляра класса, который описывает модель книги.
        :param name: Название книги
        :param author: ФИО автора
        Примеры:
        >>> book = Book("Обломов", "И. А. Гончаров")  # инициализация экземпляра базового класса
        """
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def change_name(self, new_name: str):
        """
        Функция, которая позволяет принудительно переименовать книгу
        Примеры:
        >>> book = Book("Обломов", "И. А. Гончаров")
        >>> book.change_name("Горе от ума")
        """
        self._name = new_name

    def check_size(self, num) -> bool:
        ...


class PaperBook(Book):
    """
    Документация на класс.
    Дочерний класс описывает модель бумажной книги.
    """
    def __init__(self, name: str, author: str, pages: int):
        """ Инициализация экземпляра класса, который описывает модель бумажной книги.
        :param name: Название книги
        :param author: ФИО автора
        :param pages: Кол-во страниц
        Примеры:
        >>> book = PaperBook("Обломов", "И. А. Гончаров", 251)  # инициализация экземпляра дочернего класса
        """
        if self.pages_is_valid(pages):
            self.pages = pages
        super().__init__(name, author)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @staticmethod
    def pages_is_valid(pages):
        if not isinstance(pages, int):
            raise TypeError
        if not pages >= 0:
            raise ValueError
        return True

    def check_size(self, num: int) -> bool:
        """
        Функция, которая проверяет, что номер страницы существует в книге
        :return: Выводит, существует номер или нет
        Примеры:
        >>> book = PaperBook("Обломов", "И. А. Гончаров", 251)
        >>> book.check_size(200)
        True
        >>> book.check_size(300)
        False
        """
        return self.pages >= num > 0


class AudioBook(Book):
    """
    Документация на класс.
    Дочерний класс описывает модель аудиокниги.
    """
    def __init__(self, name: str, author: str, duration: float):
        """ Инициализация экземпляра класса, который описывает модель аудиокниги.
        :param name: Название книги
        :param author: ФИО автора
        :param duration: Кол-во минут аудиозаписи
        Примеры:
        >>> book = AudioBook("Обломов", "И. А. Гончаров", 189.)  # инициализация экземпляра дочернего класса
        """
        if self.duration_is_valid(duration):
            self.duration = duration
        super().__init__(name, author)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

    @staticmethod
    def duration_is_valid(duration):
        if not isinstance(duration, float):
            raise TypeError
        if not duration >= 0:
            raise ValueError
        return True

    def check_size(self, num: float) -> bool:
        """
        Функция, которая проверяет, что таймкод записи существует в аудиокниге
        :return: Выводит, существует таймкод или нет
        Примеры:
        >>> book = AudioBook("Обломов", "И. А. Гончаров", 189.)
        >>> book.check_size(100.)
        True
        >>> book.check_size(200.)
        False
        """
        return self.duration >= num > 0


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
