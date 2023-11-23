def makable():
    lt = []
    max_i = 5000 // 3
    max_j = 5000 // 5
    three_num = []
    five_num = []

    for i in range(max_i + 1):
        for j in range(max_j + 1):
            num = 3 * i + 5 * j
            if 3 <= num <= 5000:
                lt.append(num)

    lt = sorted(set(lt))
    return lt

N = int(input())

def find_N(n):
    if (n == 4) or (n == 7):
      return -1
    elif n % 5 == 0:
      return n // 5
    elif ((n % 5) == 1) or ((n % 5) == 3):
      return n // 5 + 1
    else:
      return n // 5 + 2
    
print(find_N(N))