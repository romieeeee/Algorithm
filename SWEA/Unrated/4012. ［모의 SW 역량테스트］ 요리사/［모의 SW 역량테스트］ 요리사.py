def synergy(arr):
    ans = 0
    for i in range (size):
        for j in range (i+1, size):
            ans += food[arr[i]-1][arr[j]-1] + food[arr[j]-1][arr[i]-1]

    return ans

def dfs(depth, start):
    global res

    if depth == size:
        cook2 = []

        # cook1을 만들고 남은 재료들로 cook2 배열을 만든다
        for i in range (n):
            if (i+1) not in cook1:
                cook2.append(i+1)

        # cook1과 cook2의 시너지를 구한다
        syn1 = synergy(cook1)
        syn2 = synergy(cook2)

        res = min(res, abs(syn1-syn2))

        return
    
    for i in range (start, n):
        if not visited[i]:
            visited[i] = True
            cook1[depth] = i+1

            dfs(depth+1, i)

            visited[i] = False


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    food = [list(map(int, input().split())) for _ in range (n)]

    visited = [0] * n


    # size만큼의 조합을 만든다!
    size = n//2
    cook1 = [0] * size
    
    res = 1e9
    dfs(0, 0)

    print(f"#{test_case}", res)