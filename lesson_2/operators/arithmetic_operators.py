number_1 = 10
number_2 = 5

print(number_1 + number_2) # Якщо хоча б одне значення флотове, на виході - флот
print(number_1 - number_2)
print(number_1 * number_2)
print(number_1 / number_2) # При діленні на виході завжди флот

number_3 = 10
number_4 = 6
print(number_3 % number_4) # Модульне ділення. Поверне залишок від ділення. 10 на 6 можна розділити 1 раз і залишиться 0,4. То виведе ось це 4.
# Для чого модульне ділення може використовуватись. В нас є список з цілими значеннями
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# І з цього списку нам потрібно вивести лише парні
print(1 % 2)
print(2 % 2) # Ми по черзі виводимо залишок на кожне число і якщо виводиться нуль, то це парне число
# Погуглити про це бо якась хрінь

print(number_3 // number_4) # Ціле числове. Як з модульним діленням, але навпаки. Поверне ціле число. Тобто 1.
print(number_1 ** number_2) # Піднесення в степінь
print(pow(10, 5)) # Є така вбудована функція, яка робить те ж саме




