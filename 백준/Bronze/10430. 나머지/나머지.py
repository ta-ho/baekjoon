input_num_list = list(map(int, input().split()))
A = input_num_list[0]
B = input_num_list[1]
C = input_num_list[2]
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)