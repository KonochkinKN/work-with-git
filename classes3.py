from functools import total_ordering
from dataclasses import dataclass


def total_ordering_example():
    """
        При перегрузке методов == и
        только одного из (>, <, >=, <=)
        вcе остальные перегружаются автоматически
    """
    @total_ordering
    class Number:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value < other.value

        def __eq__(self, other):
            return self.value == other.value


    print(Number(20) > Number(3))
    # True
    print(Number(1) < Number(5))
    # True
    print(Number(15) >= Number(15))
    # True
    print(Number(10) <= Number(2))
    # False


def data_class_example():
    """
        Автоматически получаем обычный, наследуемый
        и расширяемый класс, с реализованными методами
        __init__, __repr__, __str__ и __eq__.
    """
    @dataclass
    class Publication:
        title: str
        author: str
        year: int
        publisher: str
    

    pub = Publication(title='Мастер и Маргарита', 
                      author='Булгаков М.А.',
                      year=2024, publisher='АСТ')
    print(pub.__dict__)
    print(pub.title)
    
    
def singleton_example():
    """
        Шаблон Singleton (одиночка) предоставляет механизм
        создания одного и только один экземпляра объекта,
        и предоставление к нему глобальную точку доступа.
    """
    class Singleton(object):
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance
    s1 = Singleton()
    print("Object created", id(s1))
    s2 = Singleton()
    print("Object created", id(s2))


if __name__ == "__main__":
    data_class_example()