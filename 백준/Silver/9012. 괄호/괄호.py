t = int(input())

for _ in range (t):
    stack = []
    ps = input()

    is_vps = True
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                is_vps = False
                break

    if is_vps and not stack:
        print('YES')
    else:
        print('NO')
