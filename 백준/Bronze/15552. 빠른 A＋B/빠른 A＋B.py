# 반복문으로 여러 줄을 입력받는 경우 시간초과 발생하지 않기 위해 sys.stdin.readline 사용

import sys
input = sys.stdin.readline
num = int(input().strip())
sum = []
for i in range(num):
    a, b = map(int, input().strip().split())
    sum.append(a+b)
for i in range(num):
    print(sum[i])