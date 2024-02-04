class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
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


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
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


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
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


if __name__ == "__main__":
    paper = PaperBook('Paper_name', 'Paper_author', 10)
    audio = AudioBook('Audio_name', 'Audio_author', 10.5)
    print(paper)
    print(audio)

    print(repr(paper))
    print(repr(audio))

    try:
        paper = PaperBook('Paper_name', 'Paper_author', -1)
    except ValueError:
        print("Paper wrong value")

    try:
        audio = AudioBook('Audio_name', 'Audio_author', -1.)
    except ValueError:
        print("Audio wrong value")

    try:
        paper = PaperBook('Paper_name', 'Paper_author', 'kek')
    except TypeError:
        print("Paper wrong type")

    try:
        audio = AudioBook('Audio_name', 'Audio_author', 'kek')
    except TypeError:
        print("Audio wrong value")

    try:
        audio.name = 'lmfao'
    except AttributeError:
        print("Wrong set")

    try:
        paper.author = 'lmfao'
    except AttributeError:
        print("Wrong set")
