number_1 = 10
number_2 = 11
# Коли ми порівнювали цифри по значенням, типу чи вони рівні, то іс порівнює чи це один і той самий об'єкт

# is & is not
print(number_1 is number_2)

number_3 = 10
number_4 = 10
# те про що вже говорили - якщо присвоїти двом змінним одне і те ж значення, то це буде один і той самий обєкт в області памяті з однаковими айдішками

print(id(number_3)) # виводимо айдішки. вони будуть однакові
print(id(number_4))

print(number_3 is number_4)
print(number_3 is not number_4)

list_1 = [1, 2]
list_2 = [1, 2]

print(id(list_1)) # виводимо айдішки. вони будуть однакові
print(id(list_2))

print(list_1 is list_2)
print(list_1 is not list_2) # чомусь повертає тру, а в попередньому фолс. але лісти однакові. але їм чомусь заасайнились різні айдішки

print(True is 1)
# хоч обоє є тру, нам поверне фолс, так як це різні типи даних і відповідно різні обєкти
print(True == 1) # буде тру, так як значення в них однакове

my_war = []
if bool(my_war) is not False:
    print('my_war is not empty') # тут потрібно вписати бул так як іс та іс нот порівнюють лище однакові типи даних. так як фолс - булевий, то і май вар треба перевести в булевий.
    # і тоді умова, що якщо не фолс, тобто не пусте, тобто якщо там щось є, то виведи це речення. В даному випадку не виведе
