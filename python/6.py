sum_of_squares = 0  # сумма квадратов 1^2+2^2+3^2....
squared_amount = 0  # квадрат суммы (1+2+3+...)^2
sum = 0  # накапливание суммы для квадрата суммы (1+2+3+...)
answer = 0  # Итоговый ответ

for i in range(1, 101):
    sum_of_squares += i ** 2
    sum += i

squared_amount = sum ** 2  # превращаение (1+2+3...) в (1+2+3...)^2
answer = squared_amount - sum_of_squares
print(answer)
