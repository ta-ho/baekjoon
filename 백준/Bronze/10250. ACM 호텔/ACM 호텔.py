# ACM 호텔

T = int(input())
for i in range(T):
    H,W,N = map(int, input().split())
    floor = N % H
    ho = N // H
    if floor == 0:
        print(H * 100 + ho)
    else:
        print(floor * 100 + ho + 1)