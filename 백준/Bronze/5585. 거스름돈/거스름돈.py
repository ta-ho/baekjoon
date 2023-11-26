array = [500, 100, 50, 10, 5, 1]

change = 1000-int(input())
num = 0
for i in array:
    num += change // i
    change %= i

print(num)