N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in range(len(A)):
    if A[i] < X:
        B.append(A[i])
for i in range(len(B)):
    print(B[i],end=' ')