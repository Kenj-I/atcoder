# reffer https://atcoder.jp/contests/tenka1-2019-beginner/submissions/5060831
N = int(input())
S = [1 if x == '.'  else 0 for x in list(input())]

cost = sum(S)
min_cost = cost

for i in range(N):
    if S[i] == 0:
        cost += 1
    else:
        cost -= 1

    if min_cost > cost:
        min_cost = cost

print(min_cost)
