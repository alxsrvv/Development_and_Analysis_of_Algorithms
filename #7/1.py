def QuickSort(A, p, r):
#worst - n^2
#best - n log(n)


    result = 0
    if p < r:
        A[p],A[r] = A[r],A[p]
        q,result = Partition(A, p, r)
        result += QuickSort(A, p, q-1)
        result += QuickSort(A, q+1, r)
    return result

def Partition(A, p, r):
    result = 0       
    m = A[r]
    i = p-1
    for j in range(p, r):
        result += 1
        if A[j] <= m:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    
    return (i+1), result


MyList = input('Enter your list: ').split()
for i in range (len(MyList)):
    MyList[i]=int(MyList[i])
print("Iterrations: ", QuickSort(MyList, 0, len(MyList)-1))
print(MyList)


