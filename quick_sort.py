import time
import RandomArray

def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q-1)
        Quicksort(A,q+1, r)



def Partition(A, p, r):
    x = A[r] #pivot
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

for i in range(0,10):
    A = RandomArray.getRandomArray(10000)
    start = time.clock()
    Quicksort(A, 0, len(A)-1)
    end = time.clock()
    print "Process finished in %s seconds"%(end-start)