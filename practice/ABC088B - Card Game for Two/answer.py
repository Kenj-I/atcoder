num = int(input())
scores = list(map(int, input().split()))
scores.sort()
scores.reverse()
a = 0
b = 0
ans = 0

for i, score in enumerate(scores, 1):
  if(i % 2 == 0):
    b += score
  else:
    a += score
else:
  ans = a - b
print(ans)

# refer
# n = int(input())
# a = sorted(list(map(int, input().split())), reverse=True)
# print(sum(a[::2]) - sum(a[1::2]))