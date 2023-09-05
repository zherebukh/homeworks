number = 10

# if elif else це оператори бренчування, тобто розгалуження коду. За допомогою цієї конструкції ми будемо оперувати виразами.
# Наш вираз має бути тру або фолс

if number < 10:
    print('number is lower than 10')
elif number > 10:
    print('number is upper than 10')
else:
    print('number is 10')
# елс в нас завжди без умови. еліфів може бути велика кількість.
# мінімальне - це іф, якщо розгалуження, то використовуємо елів

number_1 = 10
number_2 = 2

if (number_1 * number_2) < 10:
    print('number is lower than 10')
elif (number_1 + number_2) == 10:
    print('number is upper than 10')
elif number_1 == 10:
    print('True')
else:
    print('False')
# тут ми взяли в душки щоби дія виконалась перша (як в математиці)
# якщо умови в двох розгалуженнях - тру, то виконається лише перша умова.
# Якщо потрібно щоб виконались усі, то все зробити іфом але це вже будуть окремі конструкції не повязані між собою

if (number_1 * number_2) > 10:
    print('if true')
elif (number_1 + number_2) == 10:
    print('number is upper than 10')
elif number_1 == 10:
    print('True')
else:
    print('False')

# вбудова функція інпут. коли користувач в нього щось втайпає, воно присвоюється в змінну
secret_number = 8
your_number = (input('Guess number! Enter your variant: ')) # Тут нам в консолі виведе цей текст і туди можна буде щось ввести. Інпут означає стрінгове значення.
# Якщо користувач вводитиме щось інше окрім інтів - функція взагалі не відпрацює. Ми присвоюємо змінній те що ввели з консолі

if int(your_number) < secret_number:
    print('This number should be bigger')
elif int(your_number) > secret_number:
    print('This number should be less')
elif int(your_number) == secret_number:
    print('Hurrey! You are right!')

# Так як користувач буде вводити туди числа, то цю змінну ми перевели в інтову

