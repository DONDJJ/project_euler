"""
 a < b < c
 a^2 + b^2 = c^2
 a + b + c = 1000
 a*b*c-?
"""
# доработать!
a = 1
b = 2
c = 3

for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if a<b<c and a**2+b**2==c**2 and a+b+c==1000:
                print(a,b,c)

            c += 1
        c=1
        b += 1
    b=1
    a += 1
    print(a)