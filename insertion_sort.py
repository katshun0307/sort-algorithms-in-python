import RandomArray
import time

def insertion_sort(A):
    n = len(A)
    for j in range(1,n):
        element = A[j]
        i = j-1
        while i > -1 and A[i] > element:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = element

for i in range(0,10):
    A = RandomArray.getRandomArray(10)
    start = time.clock()
    insertion_sort(A)
    end = time.clock()
    print "process finished in %s seconds" % (end - start)


