import numpy as np
import matplotlib.pyplot as plt
def least_squares(I, D, b, lambd):
    A =  np.concatenate((I, D*lambd))
    transposeA = A.transpose()
    mult = np.matmul(transposeA,A)
    inverse = np.linalg.inv(mult)
    mult2 = np.matmul(transposeA,b) 
    x = np.matmul(inverse,mult2) 
    return x
test=np.load('./btc_price.npy',mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
plt.plot(test)
n = len(test)
I = np.identity(n)
y = np.zeros((n, 1))
zeroMatrix = np.zeros((n-1, 1))
D = np.zeros((n-1, n))
for i in range(n):
    y[i] = test[i]
for i in range(n-1):
    for j in range(n):
        if i == j:
            D[i][j] = 1
        if j - i == 1:
            D[i][j] = -1
b =  np.concatenate((y, zeroMatrix))
lambd = 25 # preferred value for lambda is 25 after testing values between 0 to 50
x = least_squares(I, D, b, lambd)
plt.plot(x)