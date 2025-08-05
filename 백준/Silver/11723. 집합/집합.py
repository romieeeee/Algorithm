import sys

S = set()
m = int(sys.stdin.readline())

def add (x): 
    S.add(int(x))

def remove (x):
    S.discard(int(x))

def check (x):
    if int(x) in S:
        print(1)
    else:
        print(0)

def toggle (x):
    if int(x) in S:
        remove(x)
    else:
        add(x)

def all():
    global S
    S = set(range(1, 21))

def empty():
    global S
    S = set()

for _ in range (m):
    st = sys.stdin.readline().strip()

    if ' ' in st:
        op, num = st.split()
    else:
        op = st

    if op == "add":
        add(num)
    elif op == "remove":
        remove(num)
    elif op == "check":
        check(num)
    elif op == "toggle":
        toggle(num)
    elif op == "all":
        all()
    else:
        empty()