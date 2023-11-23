# 백준 10869번: 사칙연산
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
input_num_list = list(map(int, input().split()))
A = input_num_list[0]
B = input_num_list[1]
print(A+B)
print(A-B)
print(A*B)
print(A//B) # 몫
print(A%B) # 나머지