min=100
max=999
list_palin=[]

for i in range(min,max):
    for j in range(min,max):

        num=i*j
        num_s=str(num)
        num_s_1=num_s[::-1]
        if num_s==num_s_1:
            list_palin.append(num)

max=list_palin[0]
for i in list_palin:
    if i>max:
        max=i

print(max)

