n = int(input()) # 회원 수

members = []
for _ in range (n):
    members.append(list(input().split()))

members.sort(key = lambda x:int(x[0]))

for member in members:
    print(' '.join(member))