# Task1
# Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
#  <d> дн <h> час <m> мин <s> сек.

# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

duration = int(input('Введите продолжительность времени в секундах: '))
days = duration // 86400
hours = (duration - days * 86400) // 3600
minutes = (duration - (days * 86400) - hours * 3600) // 60
sec = duration - days * 86400 - hours * 3600 - minutes * 60
print('Дней: ', days, ';', 'Часов: ', hours, ';', 'Минут: ', minutes, ';', 'Секунд: ', sec, ';')
