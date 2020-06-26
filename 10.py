# МЕГА ДОЛГО!!!
def issimple(x):
    metka=1
    for i in range(2,x):
        if x%i==0:
            metka=0
        if metka==0:
            continue
    if metka==1:
        return True
    else:
        return False


simple_list=[]

for i in range(2,2000000):
    print(i)
    if issimple(i):
        simple_list.append(i)


print(sum(simple_list))