T = int(input())
N = int(input())
A = map(int, input().split())
M = int(input())
B = map(int, input().split())

if N == M:
  for a, b in zip(A, B):
    print( a+T, b+T)
  #   if (a + T) != (b + T):
  #     print('no')
  #     break;
  # print('yes')
else:
  print('no')