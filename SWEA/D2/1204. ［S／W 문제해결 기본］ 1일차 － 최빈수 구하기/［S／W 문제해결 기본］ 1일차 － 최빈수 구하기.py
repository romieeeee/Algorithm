T = int(input())
for test_case in range(1, 11):
    _ = int(input()) # 테스트케이스 번호
    
    freq = [0] * 101 # 100까지 배열 생성
    scores = list(map(int, input().split()))    

    most_freq = 0
    for s in scores:
        freq[s] += 1 # 해당하는 숫자의 위치에 +1

        if freq[s] >= freq[most_freq]: # 빈도수를 비교해서 최빈수 업데이트
            most_freq = s

    print(f'#{test_case} {most_freq}')