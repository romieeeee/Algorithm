def dfs(depth, start):
    global problem, res

    if depth == cnt:
       
        # 문제 난이도의 합은 L 이상 R 이하여야 한다 
        # 가장 어려운 문제와 쉬운 문제의 차는 X 이상이어야 한다

        now_sum = sum(problem)
        difficult, easy = max(problem), min(problem)

        if (l <= now_sum <= r) and ( difficult - easy >= x):
           res += 1

        return
    
    for i in range (start, n):
        if not visited[i]:
            visited[i] = True

            problem[depth] = data[i]

            dfs(depth+1, i)

            visited[i] = False


n, l, r, x = map(int, input().split())
data = list(map(int, input().split()))

visited = [0] * n # 같은 문제를 중복해서 넣지 않도록 한다

res = 0 # 문제를 고르는 방법의 수

# 문제는 최대 n개까지 생성할 수 있으므로
# depth가 2 이상이 되는 이후부터 모든 케이스를 검사한다

cnt = 0 # 문제의 개수 (반복될 때마다 갱신된다)

for i in range (2, n+1):
    cnt = i
    problem = [0] * cnt # 문제를 담을 배열

    dfs(0, 0) # 순서가 상관없기 때문에 조합으로 생성!

print(res)
