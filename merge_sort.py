import random
import time

def Mergesort(A, p, q):
    if q-p == 1:
        pass
    else:
        if (p+q)%2 == 0:
            r = (p+q)/2
        else:
            r = (p+q+1)/2
        B = A[p:r]
        C = A[r:q]
        #print B
        #print C
        return Merge(B, C)

def Merge(B, C):
    max1 = max(B)
    max2 = max(C)
    maxf = max(max1, max2)
    print maxf
    B.append(maxf+1)
    C.append(maxf+1)
    i, j = 1,1
    D = [None] * (len(B)+len(C)-2)
    for k in range(0,len(B)+len(C)-2):
        if B[i] == C[j]:
            D[k] = B[i]
            i = i+1
        else:
            print str(i) + str(j) + str(k)
            D[k] = C[j]
            j = j+1
    return D

A = [1,6,2,5,9,2,5,2,3]

Mergesort(A, 0, len(A)-1)