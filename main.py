# Задание № 1
number = {10, -20, 35, 49, 1, 2, 90, 85, -66, 6}
for i in number:
    if i % 2 == 0 and i > 0:
        print('Заемщик с номером:', i, 'не благополучен')
print('')
# Задание № 3
number1 = int(input('Введите число: '))
factorial = 1
for i in range(1, number1+1):
    factorial *= i
print('Факториал числа', number1, 'равен', factorial)
print('')
# Задание № 5
number2 = int(input('Введите первое число: '))
number3 = int(input('Введите второе число: '))
summ_numbers = 0
for i in range(number2, number3 + 1):
    if i % 3 == 0:
        summ_numbers += i
print('среднее арифметическое всех чисел из отрезка = ', summ_numbers / i)
print('')
# Задание № 6
Str = ""
for i in range(10, 100):
    if i == (i // 10)*(i % 10)*3:
        Str += str(i) + ' '
print(Str)


