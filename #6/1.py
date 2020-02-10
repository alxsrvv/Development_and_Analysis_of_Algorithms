import random, time
#worst - n log2 n
#best - n log2 n

def mergeSort (A):

    if len(A)>1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                A[k]=lefthalf[i]
                i=i+1
            else:
                A[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            A[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            A[k]=righthalf[j]
            j=j+1
            k=k+1
        return A

SomeList = [random.randint(0,999) for z in range (999)]
start=time.time()
lab = mergeSort(SomeList)
end=time.time()
print(lab)
print("Time:", end-start)
