n, k = map(int, input().split()) 
arr = list(map(int, input().split()))

cur = sum(arr[0:k])

answer = cur
for i in range (k, n):
    cur += arr[i]
    cur -= arr[i-k]

    if cur > answer:
        answer = cur

print(answer)