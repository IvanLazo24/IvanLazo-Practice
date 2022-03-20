import unittest
from scr.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEqual(4, result)
    def test_age(self):
        cal = Calculator()
        result = cal.Valid_age(85)
        self.assertEqual(True, result)
    def test_maxim(self):
        cal = Calculator()
        result = cal.Maxim(25.554, 51, 31)
        self.assertEqual(51, result)

    def test_vocal(self):
        cal = Calculator()
        result = cal.isVocal('ade')
        self.assertEqual('Consonante', result)

    def test_Inv(self):
        cal = Calculator()
        result = cal.invertir_cadena('Hola Paolo')
        self.assertEqual('olopaP aloH', result)

    def test_Palind(self):
        cal = Calculator()
        result = cal.Palindromo('ana')
        self.assertEqual(True, result)

    def test_Ope(self):
        cal = Calculator()
        result = cal.Ope([1,2,3,4,5])
        self.assertEqual([8,1,3], result)

    def test_Country(self):
        cal = Calculator()
        result = cal.Pais(['bolivia','peru','argentina','venezuela','estados unidos'])
        self.assertEqual('peru', result)

    def test_binario(self):
        cal = Calculator()
        result = cal.binario('-154548.5')
        self.assertEqual('1010', result)

    def test_long(self):
        cal = Calculator()
        result = cal.long('154548.5')
        self.assertEqual(7, result)