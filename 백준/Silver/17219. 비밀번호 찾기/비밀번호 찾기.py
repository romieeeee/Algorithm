import sys

n, m = map(int, sys.stdin.readline().strip().split())

store = {}
for _ in range (n):
    site, pw = sys.stdin.readline().strip().split()
    store[site] = pw

for _ in range (m):
    site = sys.stdin.readline().strip()
    print(store[site])