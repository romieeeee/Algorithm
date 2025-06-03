import sys

n = int(sys.stdin.readline()) # 입력받을 회의의 개수

reserve = [] # 에약된 회의 리스트 (start, end)
for i in range (0, n):
    start, end = map(int, sys.stdin.readline().split()) # 시작 시간, 끝나는 시간
    reserve.append([start, end])

reserve.sort(key = lambda x: (x[1], x[0])) # 끝나는 시간을 기준으로 정렬

answer = 1

now = reserve[0]
for i in range(1, n): # 회의 개수 만큼 반복
    if(reserve[i][0] >= now[1]): # 시작 시간이 지금 끝나는 시간과 같거나 클 때
        now = reserve[i]
        answer += 1
    
print(answer)