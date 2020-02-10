def QuickSort(A,p,r):

    result = 0
    if p < r:
        (A[p],A[r])=A[r],A[p]
        q,result = Partition(A,p,r)
        result += QuickSort(A,p,q-1)
        result += QuickSort(A,q+1,r)
    return result

def Partition(A,p,r):
    result = 0
    m = A[r]
    i = p-1
    for j in range(p,r):
        result +=1
        if A[j] <= m:
            i +=1
            (A[i],A[j])=A[j],A[i]
    (A[i+1],A[r])=A[r],A[i+1]
    return (i+1), result

with open("input__10000.txt") as f:
    List = f.read()
List = [int(x) for x in List.split("\n")]
print(QuickSort(List,0,len(List)-1))
print(List)
