n, x = map(int, input().split()) # x일 동안 가장 많이 들어온
visit = list(map(int, input().split()))
x_visit = []

cur = sum(visit[:x])
x_visit.append(cur)

for i in range (x, n):
    cur += visit[i] # 현재 방문자 수 더하고
    cur -= visit[i-x] # 어제 방문자 수 빼기

    x_visit.append(cur)

x_visit.sort(reverse=True)
if x_visit[0] == 0:
    print('SAD')
else:
    print(x_visit[0])
    print(x_visit.count(x_visit[0]))
