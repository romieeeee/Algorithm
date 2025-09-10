import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # 0: 빈칸, 1: 집, 2:치킨집

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

res = int(1e9)
# 치킨집 중 m개를 선택하는 모든 조합
for selected in combinations(chicken, m):
    total_distance = 0

    for hx, hy in house:
        # 각 집에서 가장 가까운 치킨집 거리
        min_dist = float("inf")
        for cx, cy in selected:
            dist = abs(hx - cx) + abs(hy - cy)  #  치킨 거리는 |x1-x2| + |y1-y2|
            min_dist = min(min_dist, dist)
        total_distance += min_dist

    res = min(res, total_distance)

print(res)