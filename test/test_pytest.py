"""
Pytest tests for unit converter
"""
import sys
sys.path.append('src')
from unit_converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    miles_to_kilometers, kilometers_to_miles,
    pounds_to_kilograms, kilograms_to_pounds,
    feet_to_meters, meters_to_feet,
    gallons_to_liters, liters_to_gallons
)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert round(celsius_to_fahrenheit(37), 1) == 98.6

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(-273.15) == 0

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(373.15) == 100

def test_miles_to_kilometers():
    result = miles_to_kilometers(1)
    assert round(result, 2) == 1.61

def test_kilometers_to_miles():
    result = kilometers_to_miles(1)
    assert round(result, 2) == 0.62

def test_pounds_to_kilograms():
    result = pounds_to_kilograms(1)
    assert round(result, 2) == 0.45

def test_kilograms_to_pounds():
    result = kilograms_to_pounds(1)
    assert round(result, 2) == 2.20

def test_feet_to_meters():
    result = feet_to_meters(1)
    assert round(result, 2) == 0.30

def test_meters_to_feet():
    result = meters_to_feet(1)
    assert round(result, 2) == 3.28

def test_gallons_to_liters():
    result = gallons_to_liters(1)
    assert round(result, 2) == 3.79

def test_liters_to_gallons():
    result = liters_to_gallons(1)
    assert round(result, 2) == 0.26