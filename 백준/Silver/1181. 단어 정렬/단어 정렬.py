n = int(input())
arr = []

for _ in range (n):
    s = input()

    if arr.count(s) == 0:
        arr.append(s)

arr.sort()
arr.sort(key= lambda x: (len(x), ))

for a in arr:
    print(a)