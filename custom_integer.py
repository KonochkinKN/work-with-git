

class CustomInteger(type):
    val: int = 0
    __bits: int = 8
    __sign: bool = True
    
    def __new__(cls, name, superclasses, attributes):
        custom_int = super().__new__(cls, name, superclasses, attributes)
        attrs = name.split('int')
        if attrs[0] == 'u':
            custom_int.__sign = False
        else:
            custom_int.__sign = True
        custom_int.__bits = int(attrs[-1])
        custom_int.__shift = 2**int(attrs[-1])
        custom_int.val = 0
        custom_int.__init__ = cls.__init
        custom_int.__str__ = cls.__str
        custom_int.__add__ = cls.__add
        custom_int.__sub__ = cls.__sub
        return custom_int
    
    def __init(cls, value):
        if not cls.__sign and value < 0:
            n = abs(value) // cls.__shift
            cls.val = value + (n + 1) * cls.__shift
        else:
            cls.val = value + cls.__shift/2
            cls.val %= cls.__shift
            cls.val -= cls.__shift/2
        cls.val = int(cls.val)
        print(f'{value}->{cls.val}')
    
    def __add(cls, other):
        smm = cls.val + other.val
        if cls.__sign:
            smm += cls.__shift/2
            smm %= cls.__shift
            smm -= cls.__shift/2
        else:
            smm %= cls.__shift
        _sum = CustomInteger(cls.__class__.__name__, (int,), {})
        smm = _sum(smm)
        return smm
    
    def __sub(cls, other):
        dif = cls.val - other.val
        if cls.__sign:
            dif += cls.__shift/2
            dif %= cls.__shift
            dif -= cls.__shift/2
        else:
            dif %= cls.__shift
            if dif < 0:
                dif += cls.__shift
        _dif = CustomInteger(cls.__class__.__name__, (int,), {})
        dif = _dif(dif)
        return dif

    def __str(cls):
        return f'{cls.val}'

    def __type(cls):
        if cls.__sign:
            return f'int{cls.__bits}'
        else:
            return f'uint{cls.__bits}'
    
    def __str__(cls):
        return f"<class '{cls.__type()}'>"


def test_uint8():

    class uint8(int, metaclass=CustomInteger):
        pass

    c = uint8(8)
    d = uint8(254)
    e = c + d
    f = c - d
    print(type(e), f'{c} + {d} = {e}')
    print(type(f), f'{c} - {d} = {f}')


def test_int16():
    int16 = CustomInteger('int16', (int,), {})
    c = int16(32767)
    d = int16(16)
    e = c + d
    f = c - d
    print(type(e), f'{c} + {d} = {e}')
    print(type(f), f'{c} - {d} = {f}')


if __name__ == '__main__':
    test_uint8()


