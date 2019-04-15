A, B = map(int, input().split())
ans = [A + B, A + A - 1, B + B -1]
print(max(ans))
