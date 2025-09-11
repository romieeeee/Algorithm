import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [0] * (n + 1)

for i in range(n):
    arr_sum[i + 1] += arr_sum[i] + arr[i]

for _ in range(m):
    i, j = map(int, input().split())

    if i == j:
        print(arr[i - 1])
    else:
        print(arr_sum[j] - arr_sum[i - 1])
