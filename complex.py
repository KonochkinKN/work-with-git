from dataclasses import dataclass


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


if __name__ == '__main__':
    c = Complex(3.0, -5.0)
    print(c)
