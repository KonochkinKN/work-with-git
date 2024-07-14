from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class Complex:
    real: float
    imag: float

    def __str__(self):
        if self.imag >= 0:
            sign = '+'
        else:
            sign = '-'
        return f'{self.real} {sign} {abs(self.imag)}i'

    def __abs__(self):
        """
        Перегрузка функции abs() - взятие по модулю
        :return: Модуль данного комплексного числа
        """
        return (self.real**2 + self.imag**2)**0.5

    def __add__(self, other):
        """
        Перегрузка оператора "+" (сумма двух комплексных чисел)
        :param other: Второе число
        :return: Сумма
        """
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __sub__(self, other):
        """
        Перегрузка оператора "-" (разность двух комплексных чисел)
        :param other: Второе число
        :return: Разность
        """
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        """
        Перегрузка оператора "*" (произведение двух комплексных чисел)
        :param other: Второе число
        :return: произведение
        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def plot(self, _fig):
        _fig.plot(self.real, self.imag, 'ro')
        _fig.grid(True)
        _fig.text(self.real + 0.1, self.imag, f'({self.real}, {self.imag})')
        _fig.plot([0, self.real], [0, self.imag], 'r-', linewidth=2)


if __name__ == '__main__':
    c1 = Complex(5.0, -3.0)
    c2 = Complex(0, 1)
    c3 = c1 * c2
    # Оформление
    fig, ax = plt.subplots()
    plt.xlabel('Re')
    plt.ylabel('Im')
    ax.axvline(0, -6, 6, linewidth=2, color='k')
    ax.axhline(0, -6, 6, linewidth=2, color='k')
    # Построение
    c1.plot(ax)
    c2.plot(ax)
    c3.plot(ax)
    plt.axis('square')
    plt.show()
