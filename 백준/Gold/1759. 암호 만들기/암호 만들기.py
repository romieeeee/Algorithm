mo = ['a', 'e', 'i', 'o', 'u']
def dfs(depth, start):
    global res
    if depth == l:
        cnt = 0
        for p in pwd:
            if p in mo:
                cnt += 1
        
        # 모음의 개수가 1개 미만 or 자음의 개수가 2개 미만
        if not (cnt < 1 or l-cnt < 2):
            tmp = ''.join(sorted(pwd))
            res.append(tmp)
        
        return

    for i in range (start, c):
        if not visited[i]:
            visited[i] = True

            pwd[depth] = arr[i]

            dfs(depth+1, i)

            visited[i] = False

# l = depth, c = 문자들 개수
l, c = map(int, input().split())
arr = list(map(str, input().split())) # c 크기의 문자열 배열

visited = [0] * c
pwd = [0] * l

res = [] # 가능성 있는 암호들의 배열
dfs(0, 0)

for r in sorted(res):
    print(r)