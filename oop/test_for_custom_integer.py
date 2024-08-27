import unittest
from custom_integer import CustomInteger


class Tester(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_uint8(self):
        class uint8(int, metaclass=CustomInteger):
            pass

        c = uint8(8)
        d = uint8(254)
        e = c + d
        f = c - d
        self.assertEqual(str(type(e)), str(type(c)))
        self.assertEqual(str(type(f)), str(type(c)))
        self.assertEqual(e, uint8(6))
        self.assertEqual(f, uint8(10))

    def test_int16(self):
        int16 = CustomInteger('int16', (int,), {})
        c = int16(32767)
        d = int16(16)
        e = c + d
        f = c - d
        self.assertEqual(str(type(e)), str(type(c)))
        self.assertEqual(str(type(f)), str(type(c)))
        self.assertEqual(e, int16(-32753))
        self.assertEqual(f, int16(32751))


if __name__ == "__main__":
    unittest.main()
