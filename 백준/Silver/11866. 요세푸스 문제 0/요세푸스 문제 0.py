# 요세푸스 문제
N, K = map(int, input().split())

arr = [x for x in range (1, N+1)] # 1~N 까지 배열 생성

answer = []

K -= 1
idx = K # 시작은 K 부터

print('<', end = '')
for i in range (N):
    if len(arr) == 1:
        print(arr.pop(idx), end = '')
        break

    else:
        print(arr.pop(idx), end = ', ')

    idx += (K)
    idx %= len(arr)

print('>')