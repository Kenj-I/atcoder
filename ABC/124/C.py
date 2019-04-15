# S = [ i for i in input()]

# if len(S) <= 1:
#   print(0)
#   exit()

# zerone = ['0', '1']
# a = 0
# b = 0

# def is_even(num):
#   return 0  if num % 2 == 0 else 1

# for i in range(len(S)):
#   if S[i] != zerone[is_even(i)]:
#     a += 1
#   else:
#     b += 1

# print(a if a < b else b)

# reffer
s=list(input())
odd,even=s[1::2],s[0::2]
print(min(even.count('0') + odd.count('1'), even.count('1') + odd.count('0')))
