# n: 카드의 개수 m: m에 가까운 3장의 합
n, m = map(int, input().split())
card = list(map(int, input().split()))

m_sum = 0
for i in range (n):
    sum = 0

    for j in range(n):
        if j != i:
            sum = card[i] + card[j]
        
            if sum <= m:
                for k in range (n):
                    if k != i and k != j:
                        sum = card[i] + card[j] + card[k]

                        if sum <= m:
                            m_sum = max(m_sum, sum)

print(m_sum)