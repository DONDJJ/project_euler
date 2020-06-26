def my(number):
    kolvo = 1
    while True:

        if number % 2 == 1:
            number = 3 * number + 1
        elif number % 2 == 0:
            number /= 2
        kolvo += 1
        if number == 1:
            return kolvo



max_res = 0
max = 0
for i in range(1, 1000000):
    res = my(i)
    if res > max_res:
        max_res=res
        max = i

print(max)
