from unittest import result


def multiplicar(num1, num2):
    return num1 * num2

resultado = multiplicar(2,4)
print(resultado)

import unittest
class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(2,4),8)
        self.assertEqual(multiplicar(2,4),9)

if __name__ == '__main__':
    unittest.main()

#python3 unitest.py