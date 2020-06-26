def treug_chislo(number):
    sum=0
    for i in range(number+1):
        sum+=i
    return sum

def chislo_deliteley(number):
    x=0
    for i in range(1,number+1):
       if number%i==0:
           x+=1
    return x

for i in range(1,1000000000000):
    if chislo_deliteley(treug_chislo(i))>500:
        print(treug_chislo(i))
        break