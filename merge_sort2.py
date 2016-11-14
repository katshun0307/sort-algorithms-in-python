import RandomArray
import time


def Mergesort(A):
    last_index = len(A) - 1
    if (len(A) == 1) or (len(A) == 0):
        pass
    else:
        #find the middle
        if last_index%2 == 0:
            middle_index = last_index/2
        else:
            middle_index = (last_index-1)/2
        #print "middle index is %s"%middle_index
        first_half = Mergesort(A[:middle_index+1])
        second_half = Mergesort(A[middle_index+1:])
        #print "first is %s and second is %s"%(first_half, second_half)
        A = Merge(first_half, second_half)
    return A


def Merge(A, B):
    size = len(A) + len(B)
    #print "size is %s"%size
    max_value = 99999999
    A.append(max_value)
    B.append(max_value)
    i, j = 0, 0
    C = [None]*size
    for k in range(0,size):
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
    #print "merged %s and %s and got %s"%(A,B,C)
    return C

times = []
for i in range(0,10):
    A = RandomArray.getRandomArray(10000)
    start = time.clock()
    print (Mergesort(A))
    stop = time.clock()
    print ("Process Finished in %s seconds"%(stop-start))
    times.append(stop-start)

for i in range(0,10):
    print ("%s"%(times[i]))









