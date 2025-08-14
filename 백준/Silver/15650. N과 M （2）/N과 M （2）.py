def perm(depth, start):
    global arr

    if depth == m: # m짜리의 순열이 만들어졌다면 출력 후 종료
        print(*arr)
        return

    for i in range (start, n+1):
        arr[depth] = i
        perm(depth+1, i+1) # 조합의 경우 start 파라미터를 추가해준다

n, m = map(int, input().split())

arr = [0] * m # 길이가 m인 수열을 담을 배열

perm(0, 1) # depth가 0인채로 순열 생성 시작