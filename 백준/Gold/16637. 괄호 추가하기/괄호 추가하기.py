import sys
input = sys.stdin.readline

def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2

def dfs(idx, val):
  global result

  if idx == n:
      result = max(result, val)
      return
    
  # 괄호 없이 계산
  dfs(idx+2, calc(val, data[idx+1], data[idx]))

  # 괄호 계산
  if idx+3 < n:
    tmp = calc(data[idx+1], data[idx+3], data[idx+2])
    dfs(idx+4, calc(val, tmp, data[idx]))

n = int(input())
data = list(map(lambda x: int(x) if x.isdigit() else x, input()))

result = int(-1e9)
dfs(1, data[0])

print(result)