n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# 처음 들리는 주유소에서는 항상 기름을 살 수 밖에 없다
res = price[0] * distance[0]
min_price = price[0]
for i in range (1, n-1):
    if price[i] < min_price:
        min_price = price[i]

    res += min_price * distance[i]

print(res)