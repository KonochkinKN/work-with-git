def functor_example():
    class Functor:
        def __call__(self, *args):
            print('Вызов функтора с аргументами:', *args)
    functor = Functor()
    functor(1, 'q')
    # Вызов функтора с аргументами: 1 q


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
    functor_example()