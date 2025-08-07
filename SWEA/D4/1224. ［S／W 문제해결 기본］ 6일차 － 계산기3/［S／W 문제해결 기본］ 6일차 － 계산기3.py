for test_case in range(1, 11):
    n = int(input())
    exp = list(input())
    
    prior = {'(': 1, '+':2, '*':3} # 연산자 우선순위

    post = [] # 후위 표기식
    op = [] # 연산자 스택
    cal = []

    # 후위로 변환
    for e in exp:
        if e.isdigit():
            post.append(e)
        elif e == '(':
            op.append(e)
        elif e == ')':
            while op[-1] != '(':
                post.append(op.pop())
            op.pop()
        else:
            while op and prior[e] <= prior[op[-1]]:
                post.append(op.pop())
            op.append(e)
        
    while len(op) != 0:
        post.append(op.pop())

    for p in post:
        if p.isdigit():
            cal.append(int(p))
        elif p == '+':
            a = cal.pop()
            b = cal.pop()
            cal.append(a+b)
        elif p == '*':
            a = cal.pop()
            b = cal.pop()
            cal.append(a*b)
       
    print(f'#{test_case} {cal.pop()}')