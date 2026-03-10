celsios = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsios * 9/5) + 32
kelvin = celsios + 273.15

print("======Resultado======")

print(f"A temperatura em Celsius é {celsios:.2f}°C.")
print(f"A temperatura em Fahrenheit é {fahrenheit:.2f}°F.")
print(f"A temperatura em Kelvin é {kelvin:.2f}K.")