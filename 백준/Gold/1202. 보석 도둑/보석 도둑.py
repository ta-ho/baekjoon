# N: 총 보석 개수
# M: 보석 무게, V: 보석 가격
# C: 가방 최대 무게, K: 가방 최대 개수
## N=2 K=1, M1=5 V1=10, M2=100 V2=100, C=11
import sys
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())

jewels = [[*map(int,input().split())] for _ in range(N)] # 2중 리스트 생성
bags = [int(input()) for _ in range(K)]
jewels.sort(); bags.sort()

total_value = 0
available_jewels = []

for bag in bags:
  while jewels and jewels[0][0] <= bag: # while jewels: jewels의 요소가 남아있는동안 ,   jewels[0]: 현재 가장 가벼운 보석의 무게
    heapq.heappush(available_jewels, -jewels[0][1]) # 해당 보석의 가치를 최대 힙에 넣음(음수)
    heapq.heappop(jewels) # 해당 보석 jewels list에서 제거

  if available_jewels:
    total_value += -heapq.heappop(available_jewels)
    
print(total_value)