import random


def my_range(start=0, end=1, step=1):
    for each in (end, start, step):
        if not isinstance(each, int):
            raise TypeError
    if end < start and step > 0:
        return
    elif end < start and step < 0:
        while end < start:
            yield start
            start += step
    elif end > start and step < 0:
        return
    elif end > start and step > 0:
        while start < end:
            yield start
            start += step


def my_map(func, iterable):
    if not isinstance(iterable, (tuple, list, range)):
        raise TypeError
    for each in iterable:
        yield func(each)


def my_zip(iterable1, iterable2):
    for each in (iterable1, iterable2):
        if not isinstance(each, (tuple, list, range)):
            raise TypeError
    length = min(len(iterable1), len(iterable2))
    for i in range(length):
        yield iterable1[i], iterable2[i]


def my_enumerate(iterable, start=0):
    if not isinstance(start, int):
        raise TypeError
    if not isinstance(iterable, (tuple, list, range)):
        raise TypeError
    for each in iterable:
        yield start, each
        start += 1


def my_filter(func, seq):
    if not isinstance(seq, (tuple, list, range)):
        raise TypeError
    for each in seq:
        if func(each):
            yield each


# Tic Tac Toe
def get_0(lst):
    lst1 = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 0:
                lst1.append((i, j))
    return lst1


def tic_tac_toe(lst):
    while len(get_0(lst)) > 1:
        free = random.choice(get_0(lst))
        lst[free[0]][free[1]] = 2
        free1 = random.choice(get_0(lst))
        lst[free1[0]][free[1]] = 1
    return lst


def is_winner(lst):
    for each in lst:
        if [el for el in each] in ([1, 1, 1], [2, 2, 2]):
            return True
    if [lst[i][i] for i in range(3)] in ([1, 1, 1], [2, 2, 2]):
        return True
    for i in range(3):
        for j in range(3):
            if lst[i][j] in ([1, 1, 1], [2, 2, 2]):
                return True
    for i in range(-3, 0):
        for j in range(3):
            if lst[i][j] in ([1, 1, 1], [2, 2, 2]):
                return True
    return False


def merge(lst1, lst2):
    lst = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i < len(lst1):
        lst.extend(lst1[i:])
    if j < len(lst2):
        lst.extend(lst2[j:])
    return lst


def num_english(n):
    num_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                15: "fifteen", 16: "sixteen", "17": "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
                30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
                100: "hundred", 1000: "thousand"}
    length = len(str(n)) - 1
    while n > 99:
        el = n //(10 ** length)
        print(num_dict[el], num_dict[10 ** length], end=" ")
        n %= (10 ** length)
        length -= 1
    if n > 20:
        print(num_dict[n // 10 * 10], "-", num_dict[n % 10])
    else:
        print(num_dict[n])


def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True



