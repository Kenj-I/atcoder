# Kagami Mochi
n = int(input())
mochi_list = [input() for i in range(n)]
mochi_unique = list(set(mochi_list))
print(len(mochi_unique))