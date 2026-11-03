celsius = float(input("Enter the temperature in Celsius: "))

if celsius > 0:
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(fahrenheit, 2), "°F")
elif celsius < 0:
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", round(kelvin, 2), "K")
else:
    print("0°C is the freezing point of water.")
    print("That is 32.0 °F or 273.15 K.")
