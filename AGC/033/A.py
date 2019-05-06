import numpy as np

H,W = map(int,input().split())
A = []
for i in range(H):
    A.append([0 if i == "#" else H+W for i in list(input())])
A = np.array(A)

for i in range(H-1):
  A[i+1, :] = np.minimum(A[i, :] + 1, A[i+1, :])
for i in range(H-1,0,-1):
  A[i-1,:] = np.minimum(A[i,:]+1,A[i-1,:])
for i in range(W-1):
  A[:,i+1] = np.minimum(A[:,i]+1,A[:,i+1])
for i in range(W-1,0,-1):
  A[:,i-1] = np.minimum(A[:,i]+1,A[:,i-1])
print(np.max(A))