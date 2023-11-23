sum = []
while True:
    A, B = map(int, input().split())
    if (A==0) and (B==0):
        break
    else:
        sum.append(A+B)

for i in range(len(sum)):
    print(sum[i])