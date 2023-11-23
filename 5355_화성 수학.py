'''
문제
겨울 방학에 달에 다녀온 상근이는 여름 방학 때는 화성에 갔다 올 예정이다. (3996번) 화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다. 따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다. 입력으로 주어지는 수는 정수이거나 소수 첫째 자리까지 주어지며, 0 이상 100 이하이다. 연산자는 최대 3개 주어진다.

출력
각 테스트 케이스에 대해서, 화성 수학식의 결과를 계산한 다음에, 소수점 둘째 자리까지 출력한다.

예제 입력 1 
3
3 @ %
10.4 # % @
8 #

예제 출력 1 
14.00
25.20
1.00
'''

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