def d(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i]) 
    return int(n) + sum

creator = []
for i in range(10000):
    if d(i) < 10000:
        creator.append(d(i))
# set을 이용해 중복 제거
result = set(creator)
creator = list(result)

self_num = list(range(10000))
for j in range(len(creator)):
    self_num.remove(creator[j])
for m in range(len(self_num)):
    print(self_num[m])