# s = list(input())
# t = list(input())

# list = 'a t c o d e r'.split()

# flag = False
# for i in range(len(s)):
#   if s[i] != t[i] and not (s[i] == '@' and t[i] in list) and not (t[i] == '@' and s[i] in list):
#     flag = True

# if flag:
#   print('You will lose')
# else:
#   print('You can win')

# reffer
S = input()
T = input()
ans = 'You can win'
for a, b in zip(S, T):
  print(a,b)
  if a != b and a + b not in ('@a@t@c@o@d@e@r@'):
    ans = 'You will lose'
    break
print(ans)
