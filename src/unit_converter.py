"""
Unit Converter - MLOps LAB1
Converts between different units of measurement
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def miles_to_kilometers(miles):
    """Convert miles to kilometers"""
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    """Convert kilometers to miles"""
    return kilometers / 1.60934

def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms"""
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    """Convert kilograms to pounds"""
    return kilograms / 0.453592

def feet_to_meters(feet):
    """Convert feet to meters"""
    return feet * 0.3048

def meters_to_feet(meters):
    """Convert meters to feet"""
    return meters / 0.3048

def gallons_to_liters(gallons):
    """Convert US gallons to liters"""
    return gallons * 3.78541

def liters_to_gallons(liters):
    """Convert liters to US gallons"""
    return liters / 3.78541