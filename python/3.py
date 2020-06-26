x = 600851475143
cur_del = 1
indic=0
for i in range(2, int(x**0.5)):  # пробегаемся по числам-будущим делителям
    if x % i == 0:
        for j in range(2, i):  # проверка на простоту, сюда мы попадаем только если число i является делителем
            if i % j == 0:
                indic=1
                break
        if indic==0:
            cur_del=i
        indic=0

print(cur_del)

