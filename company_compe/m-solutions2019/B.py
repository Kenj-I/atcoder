S = list(input())

day = len(S)
win = S.count('o')
lose = S.count('x')
if win >= 8:
    print('YES')
else:
    if (15 - day) + win >= 8:
        print('YES')
    else:
        print('NO')
