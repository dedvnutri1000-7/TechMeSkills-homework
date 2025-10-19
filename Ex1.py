'''
1. Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
'''
def cyclic_sequence(seq):
    while True:
        for item in seq:
            yield item


count = int(input("Сколько чисел вывести? "))
sequence = [1, 2, 3]
gen = cyclic_sequence(sequence)

for _ in range(count):
    print(next(gen), end=" ")
