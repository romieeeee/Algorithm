def isPrime(lst):
    num = int(''.join(map(str, lst)))

    if num <= 1:
            return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

def dfs(depth):
    global res

    if depth > 0:

        # dfs 호출 할 때마다 소수 확인
        if not isPrime(res[:depth]):
            return

    if depth == n:
        res_str = ''.join(map(str, res))
        print(res_str)
        return

    for i in range (9):
        res[depth] = i+1
        dfs(depth+1)

# n 자리 소수를 생성하세요
n = int(input())
res = [0] * n

dfs(0)
