import random

w_file = open('Numbers.txt', 'w')

numbers = [str(random.randint(1, pow(2, 20))) + ' ' for _ in range(100)]

for el in numbers:
    w_file.write(el)

w_file.close()

