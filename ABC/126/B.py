S = input()
S = [S[i: i+2] for i in range(0, len(S), 2) ]

L, R = int(S[0]), int(S[1])


if  1 <= L <= 12 and 1 <= R <= 12:
  print('AMBIGUOUS')
elif 1 <= R <= 12:
  print('YYMM')
elif 1 <= L <= 12:
  print('MMYY')
else:
  print('NA')
