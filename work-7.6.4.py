# Задание № 4
student_count = int(input('Введите количетсов учеников в классе: '))
excellent = 0
well = 0
satisfactory = 0
for i in range(1, student_count + 1):
    estimation = int(input('Введите оценку '))
    if estimation == 5:
        excellent += 1
    elif estimation == 4:
        well += 1
    elif estimation == 3:
        satisfactory += 1
    else:
        print('Ошибочный ввод данных')
        continue
print('В классе количество отличников:', excellent, 'количество ударников:', well, 'количество троечников:', satisfactory)

