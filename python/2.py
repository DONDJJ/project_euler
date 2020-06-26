max=4000000
summa=0
pred=1
pred_pred=0
cur=pred+pred_pred

while (cur<max):
    if cur%2==0:
        summa+=cur
    pred_pred=pred
    pred=cur
    cur=pred+pred_pred

print(summa)

#optimal decision
# a, b = 1, 1
# total = 0
# while a <= 4000000:
#     if a % 2 == 0:
#         total += a
#     a, b = b, a+b
# print (total)