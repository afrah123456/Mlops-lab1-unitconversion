# MLOps LAB1 - Unit Converter

## Project Description
A Python-based unit converter that converts between different units of measurement including:
- **Temperature**: Celsius, Fahrenheit, Kelvin
- **Distance**: Miles, Kilometers, Feet, Meters
- **Weight**: Pounds, Kilograms
- **Volume**: Gallons, Liters

## My Modifications
Instead of a basic calculator, I created a comprehensive unit converter with:
- 12+ conversion functions covering temperature, distance, weight, and volume
- Comprehensive test coverage with both pytest and unittest
- Automated testing with GitHub Actions for continuous integration

## GitHub Actions
This project uses automated testing with GitHub Actions:
- **Pytest workflow**: Runs on every push and pull request
- **Unittest workflow**: Provides additional test coverage

Both workflows automatically run all tests and report results.

## Example Usage
- from src.unit_converter import celsius_to_fahrenheit, miles_to_kilometers
- Convert temperature
- temp_f = celsius_to_fahrenheit(25)  # Returns 77.0°F
- Convert distance
- distance_km = miles_to_kilometers(10)  # Returns 16.0934 km
- Convert weight
- weight_kg = pounds_to_kilograms(150)  # Returns 68.04 kg

## Features
- Temperature conversions (C ↔ F ↔ K)
- Distance conversions (Miles ↔ Km, Feet ↔ Meters)
- Weight conversions (Pounds ↔ Kilograms)
- Volume conversions (Gallons ↔ Liters)
- Comprehensive test coverage
- Automated CI/CD with GitHub Actions

## Author
Afrah Fathima

## Course
MLOps (IE-7374) - Lab1 (github lab)

