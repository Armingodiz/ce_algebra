import numpy
import math
def calculateLU(U,L,n):
    for k in range(n):
        beta = U[k][k]
        for i in range(k+1,n):
            L[i][k] = U[i][k]/beta
            if U[k][k]!=0:
                alpha = float(U[i][k]/U[k][k])
                for j in range(k,n):
                    temp = U[i][j] - alpha * U[k][j]
                    U[i][j] = float(temp)
    return L , U
def createI(n):
    l = numpy.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i == j:
                l[i][j] = 1
    return l
def getLU(A,n):
    return calculateLU(A.copy(),createI(n),n)
def getY(l,b,n):
    y = list()
    for i in range(n):
        y.append(b[i])
        for j in range(i):
            y[i] = y[i] - l[i][j]*y[j]
    return y
def getX(u,y,n):
    x = list()
    for i in range(n):
        x.append(0)
    for i in range(n-1,-1,-1):
        x[i] = y[i]
        for j in range(n-1,i,-1):
            x[i] = x[i] -u[i][j]*x[j]
        x[i] = x[i]/u[i][i]
    return x
n, m = input().split(); n , m = int(n),int(m)
A = numpy.zeros((n,n))
for i in range(n):
    A[i] = list(map(int,input().strip().split()))[:n]
l ,u  = getLU(A,n)
for i in range(m):
    b = list(map(int,input().strip().split()))[:n]
    y = getY(l,b,n)
    x = getX(u,y,n)
    print(*x)