# Задание № 7
cards = int(input('Введите число карточек '))
sum_cards = 0
sum_number = 0
for i in range(1, cards+1):
    sum_cards += i
for j in  range(1, cards):
    number_card = int(input('Введите номер карточки '))
    sum_number += number_card
print('Потерянная карта: ', sum_cards - sum_number)




