import functools
import itertools


def my_reduce(func, it, initial=None):
    if len(it) == 0:
        raise TypeError("Empty iterable with no initial value")
    if len(it) == 1:
        if initial is None:
            return it[0]
        else:
            func(it[0], initial)
    val = func(it[0], it[1])
    for i in range(2, len(it)):
        val = func(val, it[i])
    if initial is None:
        return val
    else:
        return func(val, initial)


def my_accumulate(it, func=lambda x, y: x + y):
    if len(it) == 0:
        raise TypeError("Empty iterable with no initial value")
    if len(it) == 1:
        return it
    new_it = []
    val = it[0]
    new_it.append(val)
    for i in range(1, len(it)):
        val = func(val, it[i])
        new_it.append(val)
    return new_it


def maker(n):
    def mult(k):
        return k * n
    return mult


mult_by_2 = maker(2)
mult_by_3 = maker(3)


def is_sudoku(lst):
    for each in lst:
        for i in range(1, 10):
            if i not in each:
                return False
    for each in [[lst[i][j] for i in range(9)] for j in range(9)]:
        for i in range(1, 10):
            if i not in each:
                return False
    for each in [[lst[i][j] for i in range(n, n + 3) for j in range(m, m + 3)]
                 for n in range(0, 9, 3) for m in range(0, 9, 3)]:
        for i in range(1, 10):
            if i not in each:
                return False
    return True


lst1 = [[6, 3, 9, 5, 7, 4, 1, 8, 2],
        [5, 4, 1, 8, 2, 9, 3, 7, 6],
        [7, 8, 2, 6, 1, 3, 9, 5, 4],
        [1, 9, 8, 4, 6, 7, 5, 2, 3],
        [3, 6, 5, 9, 8, 2, 4, 1, 7],
        [4, 2, 7, 1, 3, 5, 8, 6, 9],
        [9, 5, 6, 7, 4, 8, 2, 3, 1],
        [8, 1, 3, 2, 9, 6, 7, 4, 5],
        [2, 7, 4, 3, 5, 1, 6, 9, 8]]


print([[lst1[i][j] for i in range(n, n + 3) for j in range(m, m + 3)] for n in range(0, 9, 3) for m in range(0, 9, 3)])
print(is_sudoku(lst1))

lst2 = [1, 2, 3, 4]
print(list(itertools.accumulate(lst2, lambda x, y: x * y)))
print(list(my_accumulate(lst2, lambda x, y: x * y)))