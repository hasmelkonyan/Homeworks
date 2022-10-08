import random


def clock():
    hour = input("Enter hour: ")
    am_pm = input("am (1) or pm (2)?: ")
    go_future = input("How many hours ahead?: ")
    if not hour.isnumeric() or int(hour) not in range(0, 13):
        print("invalid input for hour")
        return
    if am_pm not in ("1", "2"):
        print("invalid input for am - pm!\nlet's start again:")
        return clock()
    not_whole_day = (int(hour) + int(go_future)) % 24
    if not_whole_day > 12 and am_pm == "1":
        print(f"New hour: {not_whole_day - 12}pm")
    elif not_whole_day > 12 and am_pm == "2":
        print(f"New hour: {not_whole_day - 12}am")
    elif not_whole_day <= 12 and am_pm == "1":
        print(f"New hour: {not_whole_day}am")
    else:
        print(f"New hour: {not_whole_day}pm")


def questions_answers():
    true_answers = 0
    questions_dct = {
        "There are ten fingers on two hands. How many fingers are on ten hands?": "50",
        "What word in the English language uses all five vowels plus Y in alphabetical order, and uses each only once?":
            "Facetiously",
        "What is the only English word, with two synonyms that are antonyms of each other?": "Cleave",
        "Is always in front of you but cannot be seen?": "Future",
        "It is weightless, you can see it. If you put it in a barrel it will make it lighter?": "Hole",
        "What goes up and down w/o (without) moving?": "Stairs",
        "What is as light as a feather but the strongest man cannot hold for long?": "Breath",
        "Where can you find cities, towns, shops and streets but no people?": "Map",
        "If you feed it, it lives, If you water it-it dies!": "Fire",
        "What has legs but cannot walk?": "Table"
    }
    asked_questions = []
    for i in range(4):
        quest = random.choice([question for question in questions_dct.keys()])
        while quest in asked_questions:
            quest = random.choice([question for question in questions_dct.keys()])
        asked_questions.append(quest)
        print(quest)
        answer = input("Your answer: ")
        if answer.capitalize() == questions_dct[quest]:
            print("Greate, you are right!!")
            true_answers += 1
        else:
            print(f"Wrong answer! Correct answer is {questions_dct[quest]}")
    print(f"You answered {true_answers} questions correctly")


def how_many_m(arr):
    for each in arr:
        for i in each:
            print(i, end=" ")
        print()
    print()

    m_count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "M":
                print("M", end=" ")
                continue
            try:
                if arr[i + 1][j] == "M":
                    m_count += 1
            except IndexError as er:
                pass
            try:
                if arr[i - 1][j] == "M":
                    if i - 1 >= 0:
                        m_count += 1
            except IndexError as er:
                pass
            try:
                if arr[i][j + 1] == "M":
                    m_count += 1
            except IndexError as er:
                pass
            try:
                if arr[i][j - 1] == "M":
                    if j - 1 >= 0:
                        m_count += 1
            except IndexError as er:
                pass
            try:
                if arr[i + 1][j + 1] == "M":
                    m_count += 1
            except IndexError as er:
                pass
            try:
                if arr[i + 1][j - 1] == "M":
                    if j - 1 >= 0:
                        m_count += 1
            except IndexError as er:
                pass
            try:
                if arr[i - 1][j + 1] == "M":
                    if i - 1 >= 0:
                        m_count += 1
            except IndexError as er:
                pass
            try:
                if arr[i - 1][j - 1] == "M":
                    if i - 1 >= 0 and j - 1 >= 0:
                        m_count += 1
            except IndexError as er:
                pass
            print(m_count, end=" ")
            m_count = 0
        print()


arr = [[0, "M", 0, "M", 0], [0, 0, "M", 0, 0], [0, 0, 0, 0, 0], ["M", "M", 0, 0, 0], [0, 0, 0, "M", 0]]


def rotate_matrix(mx):
    for i in range(len(mx)):
        for j in range(len(mx[i])):
            print(mx[i][j], end=" ")
        print()
    print()

    mx = mx[::-1]
    for each in mx:
        for el in each[::-1]:
            print(el, end=" ")
        print()



mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(rotate_matrix(mat))
