import heapq ### 우선순위 큐!
import sys

input = sys.stdin.readline

N = int(input())
card = []
for _ in range(N):
    num = int(input())
    heapq.heappush(card, num) # list안에 원소 넣기

result = 0
while len(card)>1: # card list가 1개 남을 때까지 더해주기
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    result += n1 + n2
    heapq.heappush(card, n1+n2)

print(result)