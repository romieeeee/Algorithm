w, h = map(int, input().split()) # 가로 세로
n = int(input()) # 칼로 잘라야 하는 점선의 개수

width = [0, h]
height = [0, w]

for _ in range (n):
    d, line = map(int, input().split())

    if d == 0: # 가로
        width.append(line)
    else:
        height.append(line)

width.sort()
height.sort()

w_max = 0
for i in range (1, len(width)):
    w_max = max(w_max, width[i] - width[i-1])

h_max = 0
for i in range (1, len(height)):
    h_max = max(h_max, height[i] - height[i-1])

print(w_max * h_max)
