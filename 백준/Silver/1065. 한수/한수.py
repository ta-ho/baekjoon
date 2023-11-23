# 1~99는 무조건 한수
# 111, 123, 135, 147, 159, 
# 210, 222, 234, 246, 258,
# 321, 333, 345, 357, 369,
# 420, 432, 444, 456, 468,
# ...

def finding_han_num(N):
    han_num = []
    for i in range(100, N+1):
        n = str(i)
        if (int(n[2])-int(n[1])) == (int(n[1])-int(n[0])):
            han_num.append(int(n))
    return han_num

N = int(input())
if N <= 99:
    print(N)
else:
    print(99 + len(finding_han_num(N)))