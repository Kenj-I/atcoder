import math
A, B = map(int, input().split())

if A >= 13:
  print(B)
elif 6 <= A <= 12:
  print(math.floor(B/2))
else:
  print(0)