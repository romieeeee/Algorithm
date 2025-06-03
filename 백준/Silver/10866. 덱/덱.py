import sys

# 앞에 넣기
def push_front(x):
    arr.insert(0, x)

# 뒤에 넣기
def push_back(x):
    arr.append(x)

# 맨 앞 pop
def pop_front():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr.pop(0))

# 맨 뒤 pop
def pop_back():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr.pop())

# 사이즈..
def size():
    print(len(arr))

# 비어있으면 1 아니면 0
def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

# 맨 앞 출력
def front():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[0])

# 맨 뒤 출력력
def back():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[-1])

arr = []
N = int(sys.stdin.readline())
for _ in range (N):
    command = sys.stdin.readline().rstrip('\n')

    if 'push_front' in command:
        c, v = map(str, command.split())
        push_front(int(v))

    elif 'push_back' in command:
        c, v = map(str, command.split())
        push_back(int(v))
    
    elif command == 'pop_front':
        pop_front()
    
    elif command == 'pop_back':
        pop_back()
    
    elif command == 'size':
        size()
    
    elif command == 'empty':
        empty()

    elif command == 'front':
        front()
    
    else:
        back()
