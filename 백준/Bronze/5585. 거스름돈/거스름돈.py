array = [500, 100, 50, 10, 5, 1]

change = 1000-int(input())
num = 0
for i in array:
    num += change // i # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    change %= i

print(num)