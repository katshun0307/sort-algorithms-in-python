import random

def getRandomArray(length):
    A = []
    for i in range(0,length):
        num = random.randint(0,100000)
        A.append(num)
    return A


