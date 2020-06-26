indic = 0
x = 1

while indic==0:

    for i in range(1,21):
        if x%i==0:
            indic=1
            continue
        elif x%i!=0:
            indic=0
            break

    if indic==1:
        print(x)
    else:
        x+=1


