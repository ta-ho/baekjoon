import sys
input = sys.stdin.readline

def decomposition_add(N):
    result = N
    for i in range(len(str(N))):
        result += int(str(N)[i])
    return result

k = int(input())
li = []
for i in range(1,k):
    if decomposition_add(i) == k:
        li.append(i)
if li != []:
    print(li[0])
else:
    print(0)