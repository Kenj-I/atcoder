antena = [int(input()) for i in range(5)]
K = int(input())
if (antena[4] - antena[0]) > K:
  print(':(')
else:
  print('Yay!')