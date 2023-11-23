N = int(input())

sum = []
for i in range(N):
    A, B = map(int, input().split())
    sum.append(A+B)

for i in range(N):
    print(sum[i])