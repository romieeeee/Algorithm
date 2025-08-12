def calc(node):
    value = tree[node][0]
    left = tree[node][1]
    right = tree[node][2]

    if left is None and right is None:
        return int(value)
    
    left_val = calc(left)
    right_val = calc(right)

    # +, -, *, /
    if value == '+':
        return left_val + right_val
    elif value == '-':
        return left_val - right_val
    elif value == '*':
        return left_val * right_val
    else: # value == '/'
        return left_val / right_val

for test_case in range(1, 11):
    n = int(input())

    tree = [None] * (n+1)

    for _ in range(n):
        data = input().split()
        idx = int(data[0])
        value = data[1]
        
        if len(data) == 4:
            left = int(data[2])
            right = int(data[3])
        else:
            left = right = None

        tree[idx] = (value, left, right)

    result = int(calc(1))  # 루트에서 시작
    print(f"#{test_case} {result}")
