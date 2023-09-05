# 1
temperature_in_celsius = input('Enter the temperature in Celsius: ')
temperature_in_fahrenheit = int(temperature_in_celsius) * 9 / 5 + 32
temperature_in_kelvin = int(temperature_in_celsius) + 273.15
print('Temperature in Fahrenheit is: ' + str(temperature_in_fahrenheit))
print('Temperature in Kelvin is: ' + str(temperature_in_kelvin))

# 3
number_1 = float(input('Enter the first value: '))
number_2 = float(input('Enter the second value: '))
operator = input('Enter an operator: \n + to add \n - to subtract \n * to multiply \n / to divide \n')
result = None

if operator == '+':
    result = number_1 + number_2
elif operator == '-':
    result = number_1 - number_2
elif operator == '*':
    result = number_1 * number_2
elif operator == '/':
    result = number_1 / number_2

print(f"{number_1} {operator} {number_2} = {round(result, 3)}")
