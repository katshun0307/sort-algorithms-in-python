import RandomArray
import time

def Max_heapify(A, root_index):
    last_index = len(A)-1
    left = root_index*2 + 1
    right = root_index*2 + 2
    # get largest element
    if left <= last_index and A[left] > A[root_index]:
        largest = left
    else:
        largest = root_index
    if right <= last_index and A[right] > A[largest]:
        largest = right

    if not largest == root_index:
        A[root_index], A[largest] = A[largest], A[root_index] #swap
        Max_heapify(A, largest)

def Build_max_heap(A):
    last_index = len(A)-1
    start_of_leaves_index = abs(last_index/2) + 1
    for i in range(start_of_leaves_index-1,-1,-1): #Max_heapify from bottom
        Max_heapify(A,i)
    return A

def Heapsort(A):
    last_index = len(A) -1
    for i in range(last_index, 0, -1):
        A = Build_max_heap(A[0:i+1]) + A[i+1:last_index+1] #make a max heap
        A[0], A[i] = A[i], A[0]
    return A

for i in range(0,10):
    A = RandomArray.getRandomArray(10000)
    start = time.clock()
    Heapsort(A)
    stop = time.clock()
    print ("process finished in %s seconds"%(stop-start))

