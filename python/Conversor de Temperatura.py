def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Digite a temperatura: "))
scale = input("Digite a escala (C para Celsius, F para Fahrenheit): ")

if scale.upper() == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C é igual a {converted_temperature}°F.")
elif scale.upper() == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F é igual a {converted_temperature}°C.")
else:
    print("Escala inválida. Use C ou F.")
