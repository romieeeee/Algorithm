T = int(input())
for test_case in range(1, T + 1):
    tc = input() # test case number
    scores = list(map(int, input().split()))

    result = []
    for s in scores:
        if s not in result:
            result.append([s, scores.count(s)])

    result.sort(key = lambda x: (x[1], x[0]), reverse=True)

    print(f'#{tc} {result[0][0]}')