# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample


def new_list(size):
    list_num = sample(range(size * 3), size)
    print(list_num)
    return [list_num[i] for i in range(1, len(list_num)) if list_num[i] > list_num[i-1]]

num = int(input('Введите размер: '))
if num > 1:
    print(new_list(num))
else:
    print('Ошибка')
