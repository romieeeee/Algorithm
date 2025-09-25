# 회전
def rotate():
     # belt 한 칸 시계방향 회전
    belt.insert(0, belt.pop())

    # robots 한 칸 이동
    robots.insert(0, False)
    robots.pop()

    # 내리는 위치는 항상 비워야 한다
    robots[-1] = False


# 로봇 이동
def move_robots():
    for i in range (n-2, -1, -1): # 뒤에서부터 검사한다
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            belt[i+1] -= 1

    robots[-1] = False # 내리는 위치 비우기

    
# 로봇 추가
def add_robot():
    if belt[0] > 0 and not robots[0]: 
        robots[0] = True
        belt[0] -= 1


n, k = map(int, input().split())
belt = list(map(int, input().split()))
robots = [False] * n

step = 0

while True:
    step += 1

    rotate()
    move_robots()
    add_robot()

    if belt.count(0) >= k:
        print(step)
        break