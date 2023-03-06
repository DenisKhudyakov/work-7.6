# Задание 2
summ_salary = 0
for month in range(1, 13):
    salary = int(input('Ввведите зарплату за ' + str(month) + ' месяц'))
    summ_salary += salary
    middle_salaty = summ_salary / 12
print("%.2f" % middle_salaty)
