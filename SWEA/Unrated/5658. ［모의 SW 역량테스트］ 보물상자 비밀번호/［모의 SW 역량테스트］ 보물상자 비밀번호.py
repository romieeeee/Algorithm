T = int(input())
for test_case in range (1, T+1):
    n, k = map(int, input().split()) # 숫자의 개수, 순서
    s = input() # 입력 문자열

    side = n//4 # 한 면의 길이
    nums = set() # 생성된 10진수들을 담을 배열

    s += s # 인덱스 넘어가지 않게 
    for i in range (side): # 면의 개수만큼 회전한다
        for j in range (4):
            start = i + (j*side)
            part = s[start:start+side]
            nums.add(int(part, 16))

    nums = sorted(nums, reverse=True)
    print(f"#{test_case} {nums[k-1]}")
