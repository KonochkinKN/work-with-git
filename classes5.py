import matplotlib.pyplot as plt


def functor_example():
    class Functor:
        def __call__(self, *args):
            print('Вызов функтора с аргументами:', *args)
    functor = Functor()
    functor(1, 'q')
    # Вызов функтора с аргументами: 1 q


def another_functor_example():
    class Functor:
        def __init__(self, title):
            fig, self.ax = plt.subplots()
            self.ax.set_title(title)

        def __call__(self, *args):
            for arg in args:
                if type(arg[0]) is tuple:
                    x = [a[0] for a in arg]
                    y = [a[1] for a in arg]
                    self.ax.plot(x, y, '-o')
                else:
                    x = list(range(len(arg)))
                    self.ax.plot(x, arg, '--s')
            plt.grid(True)
            plt.axis('square')
            plt.show()

    fun = Functor('Некоторые прямые')
    x1 = [x-5 for x in range(11)]
    y1 = [x*2 for x in x1]
    points1 = list(zip(x1, y1))
    x2 = [x-5 for x in range(11)]
    y2 = [1-x for x in x2]
    points2 = list(zip(x2, y2))
    points3 = x1[:]
    fun(points1, points2, points3)


def class_decorator_example():
    class Validation:
        def __init__(self, lower, upper):
            self._lower = lower
            self._upper = upper

        def __call__(self, arg):
            def wrapper(a):
                res = arg(a)
                if not self._lower < res < self._upper:
                    raise ValueError(
                        'Validation failed'
                    )
                return f'answer: {res}'
            return wrapper

    @Validation(0, 10)
    def square(a):
        return a**2


    print(square(2))
    # answer: 4
    print(square(4))
    # ValueError: Validation failed


if __name__ == "__main__":
    another_functor_example()