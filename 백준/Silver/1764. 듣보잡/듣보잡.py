n, m = map(int, input().split())
not_see = set(input().strip() for _ in range(n))  # set으로 변경

result = set()
for i in range (m):
    p = input().strip()

    if p in not_see:
        result.add(p)

result = sorted(result)

print(len(result))
for r in result:
    print(r)