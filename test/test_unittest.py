"""
Unittest tests for unit converter
"""
import unittest
import sys

sys.path.append('src')
from unit_converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    miles_to_kilometers, kilometers_to_miles,
    pounds_to_kilograms, kilograms_to_pounds
)


class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)


class TestDistanceConversion(unittest.TestCase):

    def test_miles_to_kilometers(self):
        result = miles_to_kilometers(1)
        self.assertAlmostEqual(result, 1.61, places=2)

    def test_kilometers_to_miles(self):
        result = kilometers_to_miles(1)
        self.assertAlmostEqual(result, 0.62, places=2)


class TestWeightConversion(unittest.TestCase):

    def test_pounds_to_kilograms(self):
        result = pounds_to_kilograms(1)
        self.assertAlmostEqual(result, 0.45, places=2)

    def test_kilograms_to_pounds(self):
        result = kilograms_to_pounds(1)
        self.assertAlmostEqual(result, 2.20, places=2)


if __name__ == '__main__':
    unittest.main()