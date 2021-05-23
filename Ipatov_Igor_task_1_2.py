# Task 2
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a. Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» # будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.

cube_list = []
for numbers in range(1, 1001, 2):
    cube_list.append(numbers ** 3)
final_sum = 0
for numbers in cube_list:
    check_sum = 0
    for check_num in str(numbers):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += numbers
print(final_sum)
