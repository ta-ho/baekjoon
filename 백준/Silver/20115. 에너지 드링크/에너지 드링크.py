N = int(input())
sum = 0
drink = list(map(int, input().split()))
drink.sort()
for i in drink[:-1]:
    i /= 2
    sum += i
sum += max(drink)
print(sum)