# тернарний оператор теж іф елс але для визначення змінної. наприклад нам треба призначити якусь змінну в залежності від умов

even_number = True if 4 % 2 == 0 else False # кщо вираз іф правдивий (тру), нам присвоюється те що зліва в іншому випадку те що справа
print(even_number)

is_nice = True
state = 'nice' if is_nice else 'not nice'
print(state)

age = 23
is_can_by_beer = True if age >= 21 else False
if is_can_by_beer:
    print('I can by beer')



