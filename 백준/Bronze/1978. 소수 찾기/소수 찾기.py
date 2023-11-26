import sys
input = sys.stdin.readline

# 소수 판별
def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5)+1): # 제곱근까지만 확인
        if N % i == 0:
            return False
    return True

count = 0
T = int(input())
nums = list(map(int, input().split()))
for i in range(T):
    if is_prime(nums[i]):
        count += 1

print(count)