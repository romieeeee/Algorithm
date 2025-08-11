def inorder(node):
    if node == 0: 
        return
    
    inorder(left[node])
    print(value[node], end='')
    inorder(right[node])

for test_case in range(1, 11):
    n = int(input())

    value = [''] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)

    for _ in range(n):
        data = input().split()
        node = int(data[0])
        value[node] = data[1]
        if len(data) > 2:
            left[node] = int(data[2])
        if len(data) > 3:
            right[node] = int(data[3])

    print(f"#{test_case} ", end='')
    inorder(1)
    print()
