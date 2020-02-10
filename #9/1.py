
from math import inf

def Parent(i):
    return (i-1)//2

def Left(i):
    return 2 * i + 1

def Right(i):
    return 2 * i + 2

def MaxHeap(A, i):
    left = Left(i)
    right = Right(i)
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeap(A, largest)

def MinHeap(A, i):
    left = Left(i)
    right = Right(i)
    smallest = i
    if left < len(A) and A[left] < A[smallest]:
        smallest = left
    if right < len(A) and A[right] < A[smallest]:
        smallest = right
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        MinHeap(A, smallest)

def HeapIncreaseKey(A, i, key):
    A[i] = key
    while i > 0 and A[Parent(i)] < A[i]:
        A[i], A[Parent(i)]=A[Parent(i)], A[i]
        i = Parent(i)

def HeapReduceKey(A, i, key):
    A[i] = key
    while i > 0 and A[Parent(i)] > A[i]:
        A[i], A[Parent(i)]=A[Parent(i)], A[i]
        i = Parent(i)

def MaxHeapInsert(A, key):
    A.append(-inf)
    HeapIncreaseKey(A, len(A)-1, key)

def MinHeapInsert(A, key):
    A.append(inf)
    HeapReduceKey(A, len(A)-1, key)

def HeapExtractMax(A):
    heap_size=len(A)
    maxel = A[0]
    A[0], A[heap_size-1] = A[heap_size-1], A[0]
    A.remove(A[heap_size-1])
    MaxHeap(A, 0)
    return maxel

def HeapExtractMin(A):
    heap_size=len(A)
    minel = A[0]
    A[0], A[heap_size-1] = A[heap_size-1], A[0]
    A.remove(A[heap_size-1])
    MinHeap(A, 0)
    return minel


def Adder(val):

    if not maxh and not minh:
        MaxHeapInsert(maxh,val)
        return val
    elif maxh:

        if val >= maxh[0]:
            MinHeapInsert(minh,val)
        else:
            MaxHeapInsert(maxh, val)

        if len(maxh)==len(minh):
            return ("%s, %s"%(maxh[0], minh[0]))
        elif len(maxh)==len(minh)+1:
            return maxh[0]
        elif len(minh)==len(maxh)+1:
            return minh[0]


        elif len(minh)==len(maxh)+2:
            MaxHeapInsert(maxh, HeapExtractMin(minh))
            return ("%s, %s"%(maxh[0], minh[0]))
        elif len(maxh)==len(minh)+2:
            MinHeapInsert(minh, HeapExtractMax(maxh))
            return ("%s, %s"%(maxh[0], minh[0]))

with open("input_9.txt", 'r') as f:
    A = f.read()

maxh = []
minh = []
median = 0

A = list(map(int, A.split("\n")))
A.pop(0)
print(A)
for x in A:
    print(Adder(x))
    print("Heap maximum: ", maxh[:5], "\n","Heap minimum: ", minh[:5] )
