import doctest
from typing import Union, List


# TODO Написать 3 класса с документацией и аннотацией типов
class Champaign:
    """
    Документация на класс.
    Класс описывает модель шампанского.
    """
    def __init__(self, brand_name: str, capacity_volume: Union[int, float], alcohol_proof: Union[int, float]):
        """ Инициализация экземпляра класса, который описывает модель шампанского.

        :param brand_name: Марка шампанского
        :param capacity_volume: Объем бутылки
        :param alcohol_proof: Крепость напитка

        Примеры:
        >>> champaign = Champaign("Абрау Дюрсо", 0.75, 13)  # инициализация экземпляра класса
        """
        if not isinstance(brand_name, str):
            raise TypeError
        if len(brand_name) <= 0:
            raise ValueError
        self.brand_name = brand_name

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(alcohol_proof, (int, float)):
            raise TypeError
        if alcohol_proof < 0:
            raise ValueError
        self.alcohol_proof = alcohol_proof

    def is_open_bottle(self) -> bool:
        """
        Функция, которая проверяет, является ли бутылка открытой

        :return: Является ли бутылка открытой

        Примеры:
        >>> champaign = Champaign("Абрау Дюрсо", 0.75, 13)
        >>> champaign.is_open_bottle()
        """
        ...

    def is_drink(self) -> bool:
        """
        Функция, которая проверяет, является ли бутылка выпитой

        :return: Является ли бутылка выпитой

        Примеры:
        >>> champaign = Champaign("Абрау Дюрсо", 0.75, 13)
        >>> champaign.is_drink()
        """
        ...


class Mandarin:
    """
    Документация на класс.
    Класс описывает модель мандарина.
    """
    def __init__(self, seeds_number: int, mandarin_diameter: Union[int, float]):
        """ Инициализация экземпляра класса, который описывает модель мандарина.

        :param seeds_number: Количество семечек в мандарине
        :param mandarin_diameter: Диаметр плода мандарина

        Примеры:
        >>> mandarin = Mandarin(7, 5)  # инициализация экземпляра класса
        """
        if not isinstance(seeds_number, int):
            raise TypeError
        if seeds_number < 0:
            raise ValueError
        self.seeds_number = seeds_number

        if not isinstance(mandarin_diameter, (int, float)):
            raise TypeError
        if mandarin_diameter <= 0:
            raise ValueError
        self.mandarin_diameter = mandarin_diameter

    def remove_seeds(self, count: int) -> None:
        """
        Функция, которая проверяет, сколько семян удалено из мандарина

        Примеры:
        >>> mandarin = Mandarin(7, 5)
        >>> mandarin.remove_seeds(7)
        """
        ...

    def eat(self) -> bool:
        """
        Функция, которая проверяет, съеден ли мандарин

        :return: Съеден ли мандарин

        Примеры:
        >>> mandarin = Mandarin(0, 5)
        >>> mandarin.eat()
        """
        ...


class ChristmasTree:
    """
    Документация на класс.
    Класс описывает модель мандарина.
    """
    def __init__(self, tree_height: Union[int, float], tree_diameter: Union[int, float]):
        """ Инициализация экземпляра класса, который описывает модель ёлки.

        :param tree_height: Высота ёлки
        :param tree_diameter: Диаметр ёлки в самой широкой части

        Примеры:
        >>> christmasTree = ChristmasTree(200, 100)  # инициализация экземпляра класса
        """
        if not isinstance(tree_height, (int, float)):
            raise TypeError
        if tree_height <= 0:
            raise ValueError
        self.tree_height = tree_height

        if not isinstance(tree_diameter, (int, float)):
            raise TypeError
        if tree_diameter <= 0:
            raise ValueError
        self.tree_diameter = tree_diameter

    def decorate(self, mandarins: List[Mandarin]) -> None:
        """
        Функция, которая добавляет мандарины на ёлку

        Примеры:
        >>> christmasTree = ChristmasTree(7, 5)
        >>> mandarin = Mandarin(0, 5)
        >>> christmasTree.decorate([mandarin])
        """
        ...

    def cat_attack(self) -> bool:
        """
        Функция, которая проверяет, упала ли ёлка от атаки котиком

        :return: Упала ли ёлка от атаки котиком

        Примеры:
        >>> christmasTree = ChristmasTree(7, 5)
        >>> christmasTree.cat_attack()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
