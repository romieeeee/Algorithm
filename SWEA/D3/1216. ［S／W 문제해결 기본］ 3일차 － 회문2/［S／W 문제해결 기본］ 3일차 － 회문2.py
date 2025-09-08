def isPalindrome(arr):
  for length in range(100, 0, -1):  # 길이 큰 것부터
    for start in range(100 - length + 1):
      tmp = arr[start:start + length]
      if tmp == tmp[::-1]:
        return length
  return 0

for _ in range (1, 11):
  tc = input()

  data = [list(input()) for _ in range (100)] # 100*100 

  max_row = 0
  max_col = 0

  for i in range (100):
    row = data[i] # 행 선택
    max_row = max(max_row, isPalindrome(row))

  for i in range (100):
    col = [data[x][i] for x in range (100)]
    max_col = max(max_col, isPalindrome(col))

  print(f'#{tc} {max(max_row, max_col)}')