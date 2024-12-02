import random
def left_number():
    l_number = random.randrange(3, 21)
    print(f"Левое число: {l_number}")
    return l_number
def right_number(l_number):
    r_number_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    r_number_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    list_ = []
    for i in r_number_1:
        for j in r_number_2:
            if l_number % (i + j) == 0:
                string = str(j) + str(i)
                list_.append(string)
                continue
            else:
                break
    list_.sort()
    print(*list_)

right_number(left_number())