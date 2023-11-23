input_cal = []
result = []
num_cases = int(input())
for i in range(num_cases):
    input_cal.append(list(input().split()))
    cal = float(input_cal[i][0]) # 이번에도 이놈을 j for문 안으로 넣어 답이 안 나와 헤맸다. ** 계속 계산되는 변수 초기값은 반복문 밖으로 **
    
    for j in range(1, len(input_cal[i])):
        if input_cal[i][j] == '@':
            cal *= 3
        elif input_cal[i][j] == '%':
            cal += 5
        else:
            cal -= 7
    result.append(cal)

for k in range(len(result)):
    print("%0.2f"%result[k])