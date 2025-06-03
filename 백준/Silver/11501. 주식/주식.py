T = int(input())
for _ in range (T):
    N = int(input())
    price = list(map(int, input().split()))

    high = 0
    profit = 0
    for i in range (N-1, -1, -1):
        if price[i] > high:
            high = price[i]
        else:
            profit += high - price[i]

    print(profit)