import sys
input = sys.stdin.readline

# 블랙잭(변형)

# N장의 카드 중 M을 넘지 않으면서 M에 가장 가까운 카드3장합을 뽑아 그 합을 출력
import itertools

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
sum_combination = []
for comb in itertools.combinations(num_list, 3):
    sum_combination.append(sum(comb))

if M in sum_combination:
    print(M)
else:
    sum_combination.append(M)
    sum_combination.sort()
    print(sum_combination[sum_combination.index(M)-1])