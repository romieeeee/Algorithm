n, k = map(int, input().split())
num = [x for x in range (2, n+1)]

del_arr = []

i = 2
while (num):

    isPrime = 0
    for j in range (2, i):
        if i % j == 0: # 나머지가 0이다! -> 약수 존재 
            isPrime += 1
    
    if isPrime == 0: # 소수라면
        tmp = []
        for l in range (len(num)): # 배열 순회하면서
            if num[l] % i == 0:
                tmp.append(num[l])
        
        for f in range (len(tmp)):
            if tmp[f] in num:
                del_arr.append(tmp[f])
                num.remove(tmp[f])
        
    i += 1

print(del_arr[k-1])