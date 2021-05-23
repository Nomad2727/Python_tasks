# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

def num_translate():
    num_tuple = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    num_tuple_translate = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    input_num = input('Введите число от 0 до 10 на английском языке: ')
    if input_num == num_tuple[0]:
        print(num_tuple_translate[0])
    elif input_num == num_tuple[1]:
        print(num_tuple_translate[1])
    elif input_num == num_tuple[2]:
        print(num_tuple_translate[2])
    elif input_num == num_tuple[3]:
        print(num_tuple_translate[3])
    elif input_num == num_tuple[4]:
        print(num_tuple_translate[4])
    elif input_num == num_tuple[5]:
        print(num_tuple_translate[5])
    elif input_num == num_tuple[6]:
        print(num_tuple_translate[6])
    elif input_num == num_tuple[7]:
        print(num_tuple_translate[7])
    elif input_num == num_tuple[8]:
        print(num_tuple_translate[8])
    elif input_num == num_tuple[9]:
        print(num_tuple_translate[9])
    elif input_num == num_tuple[10]:
        print(num_tuple_translate[10])
    elif input_num == num_tuple[11]:
        print(num_tuple_translate[11])
    else: print('Вы ввели не верное число !')

num_translate()
