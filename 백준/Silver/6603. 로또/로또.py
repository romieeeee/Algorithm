def dfs(depth, start):
    global lotto

    if depth == 6:
        print(*lotto)
        return
    
    for i in range (start, k):
        if not visited[i]:
            visited[i] = True
            lotto[depth] = data[i]

            dfs(depth+1, i)

            visited[i] = False

while True:
    data = list(map(int, input().split()))

    if data == [0]:
        exit(0)

    k = data.pop(0)

    lotto = [0] * 6
    visited = [0] * k

    dfs(0, 0)
    print()