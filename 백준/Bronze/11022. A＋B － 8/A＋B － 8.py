num_case = int(input())
A = []
B = []
for i in range(num_case):
    num_list = list(map(int, input().split()))
    A.append(num_list[0])
    B.append(num_list[1])
for i in range(num_case):
    print(f"Case #{i+1}: {A[i]} + {B[i]} = {A[i]+B[i]}")