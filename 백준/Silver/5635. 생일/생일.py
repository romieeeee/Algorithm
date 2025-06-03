n = int(input())
stu = [list(input().split()) for _ in range (n)]

stu.sort(key = lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(stu[-1][0])
print(stu[0][0])