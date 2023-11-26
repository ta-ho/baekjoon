# ox퀴즈

# 연속된 O의 개수 => 점수

# OOXXOXXOOO => 1+2 + 1 + 1+2+3

def total_score(a):
    count = 0
    score = 0
    for char in a:
        if char == 'O':
            count += 1
            score += count # 이게 키 포인트!!
        else:
            count = 0
    return score

num_cases = int(input())
for _ in range(num_cases):
    string = input()
    print(total_score(string))
