num = [str(x) for x in range (10)]

a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)

for n in num:
    print(mul.count(n))        
