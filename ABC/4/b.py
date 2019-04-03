# C = [list(input().split()) for i in range(4)]
# for i in range(4):
#   ans = []
#   for j in range(4):
#     ans.append(C[3-i][3-j])
#   print('{0[0]} {0[1]} {0[2]} {0[3]}'.format(ans))

# reffer
C = [input()[::-1] for i in range(4)][::-1]
for c in C:
  print(c)