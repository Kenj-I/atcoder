import collections

N = int(input())
sides = []

for i in range(N - 1):
    sides.extend(list(map(int, input().split())))
S = collections.Counter(sides)
c = list(map(int, input().split()))
M = sorted(c, reverse=True)
print(sum(M[1:N]))
print(S)

h = 0
ans = []
for s in S:
    print(s)
