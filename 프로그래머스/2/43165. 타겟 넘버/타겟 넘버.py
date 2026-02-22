def solution(numbers, target):
    answer = 0
    m = len(numbers)
    
    def dfs(i, cur):
        nonlocal answer
        
        if i>=m:
            if cur == target:
                answer += 1

            return

        
        dfs(i+1, cur+numbers[i])
        dfs(i+1, cur-numbers[i])

    dfs(0, 0)

    return answer
