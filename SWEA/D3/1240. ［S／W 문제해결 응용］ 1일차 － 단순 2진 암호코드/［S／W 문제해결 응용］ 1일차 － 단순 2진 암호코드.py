code_dict = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    code = []

    codes = []
    for _ in range(n):
        codes.append(input())

    for row in codes:
        # 암호는 1이 나오는 줄이 유효하고
        # 각 줄은 다 같기 때문에 한 줄만 검사하면 된다!
        start = 0
        if "1" in row:  # 모든 암호는 1로 끝난다! > 암호의 끝 위치를 찾는다
            start = row.rfind("1")

            # 암호의 길이는 56
            for i in range(start - 55, start + 1, 7):
                tmp = row[i : i + 7]
                code.append(code_dict.get(tmp, -1))
            break

    odd_sum = 0
    even_sum = 0
    for i in range(len(code)):
        if (i + 1) % 2 == 0:  # 짝수 자리
            even_sum += code[i]
        else:  # 홀수 자리
            odd_sum += code[i]

    res = 0
    if (odd_sum * 3 + even_sum) % 10 == 0:
        res = sum(code)

    print(f"#{test_case} {res}")
