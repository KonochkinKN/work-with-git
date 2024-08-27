

class CustomInteger(type):
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
        custom_int.__eq__ = cls.__eq
        custom_int.__repr__ = cls.__repr
        return custom_int
    
    def __init(cls, value):
        if not cls.__sign and value < 0:
            n = abs(value) // cls.__shift
            cls.val = value + (n + 1) * cls.__shift
        elif not cls.__sign:
            cls.val = value % cls.__shift
        else:
            cls.val = value + cls.__shift/2
            cls.val %= cls.__shift
            cls.val -= cls.__shift/2
        cls.val = int(cls.val)
    
    def __add(cls, other):
        smm = cls.val + other.val
        _sum = CustomInteger(cls.__class__.__name__, (int,), {})
        smm = _sum(smm)
        return smm
    
    def __sub(cls, other):
        dif = cls.val - other.val
        _dif = CustomInteger(cls.__class__.__name__, (int,), {})
        dif = _dif(dif)
        return dif

    def __str(cls):
        return f'{cls.val}'

    def __eq(cls, other):
        return cls.val == other.val

    def __repr(cls):
        if cls.__sign:
            return f'int{cls.__bits}'
        else:
            return f'uint{cls.__bits}'
    
    def __str__(cls):
        return f"<class '{cls.__repr()}'>"


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


def metaclass_example():
    meta = type('MyMeta', (), {})
    meta.attr1 = 5
    meta.attr2 = 7
    print(meta.__dict__)
    # print(type(meta))

    m = meta()
    print(m.attr1)
    print(m.__dict__)
    print(type(m))


if __name__ == '__main__':
    metaclass_example()


