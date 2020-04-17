import numpy as np
import random
import timeit

while True:
    enter = input('Input selection: random - 1, manually - 2 : ')
    method = input('Sorting method: Bubble - 1, selection - 2, insertion - 3 : ')
    sort = input('Ascending - 1, descending - 2 : ')
    # спросили ввод, способ и вид сортировки

    def bubble_up(k):  # пузырьковая сортировка на возростание
        # вводим два глобальных счетчика для подсчета
        global count_bubble
        global swap_bubble
        count_bubble = 0
        swap_bubble = 0   # количество обмена
        for i in range(1,n):
            for j in range(n-1, i-1, -1):
                count_bubble += 1
                if (A[j-1]>A[j]):
                    swap_bubble += 1
                    A[j], A[j-1] = A[j-1], A[j]
        print(A)

    def bubble_down(k):  # на спадание
        global count_bubble
        global swap_bubble
        count_bubble = 0
        swap_bubble = 0  # количество обмена
        for i in range(1, n):
            for j in range(n-1, i-1, -1):
                count_bubble += 1
                if (A[j-1]<A[j]):
                    swap_bubble += 1
                    A[j], A[j-1] = A[j-1], A[j]
        print(A)

    def selection_up(k):  # сортировка выбора на возростание
        global count_selection
        global swap_selection
        count_selection = 0
        swap_selection = 0   # количество обмена
        for i in range(n-1):  # алгоритм
            min = i
            for j in range(i+1, n):
                count_selection += 1
                if A[j]<A[min]:
                    swap_selection += 1
                    min = j
            A[i], A[min] = A[min], A[i]
        print(A)

    def selection_down(k):  # сортировка выбора на убывание
        global count_selection
        global swap_selection
        count_selection = 0
        swap_selection = 0  # количество обмена
        for i in range(n-1):
            min = i
            for j in range(i+1, n):
                count_selection += 1
                if A[j]>A[min]:
                    swap_selection += 1
                    min = j
            A[i], A[min] = A[min], A[i]
        print(A)

    def insertion_up(k):      # ф-я сортировки вставки на возростание
        global count_insertion
        global swap_insertion
        count_insertion = 0
        swap_insertion = 0   # количество обмена
        for i in range(1, n):  # алгоритм
            j = i - 1
            key = A[i]
            while j >= 0 and A[j] > key:
                swap_insertion += 1
                count_insertion += 2
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
        print(A)

    def insertion_down(k):  # ф-я сортировки вставки на убывание
        global count_insertion
        global swap_insertion
        count_insertion = 0
        swap_insertion = 0   # количество обмена
        for i in range(1, n):
            j = i - 1
            key = A[i]
            while j >= 0 and A[j] < key:
                swap_insertion += 1
                count_insertion += 2
                A[j + 1] = A[j]
                j -= 1
            A[j+1] = key
        print(A)


    if enter == '1': # способ ввода рандом
        A = np.zeros(100000, dtype=int)  # масив на 100000 рандомных чисел
        for i in range(100000):
            A[i] = random.randint(0, 10)
        print(A)
        n = len(A)
        k = 100000
    elif enter == '2':  # если способ ввода пользователем, просим ввести до 30 чисел
        x = int(input('Enter the number of digits: '))
        while x > 30:
            x = int(input('Enter the number of digits to the 30: '))
        A = np.zeros(x, dtype=int)
        for i in range(x):
            A[i] = int(input('Enter the number  '))
        print(A)
        n = len(A)
        k = x
    else:
        print('Enter 1 or 2: ')

# сведения о каждой сортировке
    def datum_bubble(countner):
        print('Number of comparisons by the bubble method', countner)
        print('Number of swap by the bubble method', swap_bubble)
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)  # время выпомнения алгоритма
        print('The program was running', t)


    def datum_selection(countner):
        print('Number of comparisons by the selection method', countner)
        print('Number of swap by the selection method', swap_selection)
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
        print('The program was running', t)


    def datum_insertion(countner):
        print('Number of comparisons by the insertion method', countner)
        print('Number of swap by the insertion method', swap_insertion)
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
        print('The program was running', t)


    if method == '1': # вывод ф-и в зависимости от выбора метода
        if sort == '1':  # от выбора способа сортировки
            bubble_up(k)
            datum_bubble(countner=count_bubble)  # параметр ф-и
        elif sort == '2':
            bubble_down(k)
            datum_bubble(countner=count_bubble)
        else:
            print('Enter 1 or 2: ')
    elif method == '2':
        if sort == '1':
            selection_up(k)
            datum_selection(countner=count_selection)
        elif sort == '2':
            selection_down(k)
            datum_selection(countner=count_selection)
        else:
            print('Enter 1 or 2: ')
    elif method == '3':
        if sort == '1':
            insertion_up(k)
            datum_insertion(countner=count_insertion)
        elif sort == '2':
            insertion_down(k)
            datum_insertion(countner=count_insertion)
        else:
            print('Enter 1 or 2: ')
    else:
        print('Enter 1, 2 or 3 ')

    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break


