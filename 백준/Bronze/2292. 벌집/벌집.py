import sys
input = sys.stdin.readline

# 1: 방1개 => 1개
# 2~7: 방2개 => 6개 
# 8~19: 방3개 => 12개
# 20~37: 방4개 => 18개
# 38~61: 방5개 => 24개
# ...: 방n개 => 6x(n-1)개

N = int(input())

if N == 1:
    print(1)
else:
    room = 1 # 시작 방 번호
    count = 1 # 이동한 방의 수
    while room < N:
        room += 6 * count # 각 레벨에서 6의 배수만큼 방이 증가
        count += 1
    print(count)