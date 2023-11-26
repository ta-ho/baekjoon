alphabet = "abcdefghijklmnopqrstuvwxyz"

S = input()
for i in alphabet:
    if i in S:
        print(S.index(i))
    else:
        print(-1)