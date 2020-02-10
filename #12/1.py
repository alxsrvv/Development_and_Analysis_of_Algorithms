from collections import deque
#worst - n log n + m
#best - n^2 + m
def BFS (Mat,n1,n2):
    cost = 0
    minway = (0,[])
    if n1 == n2:
        return cost,[n1]
    queue = deque([])
    for i in Mat:
        if i[0] == n1:
            queue.append((i[1],i[2],[n1]))
    z = 1
    while queue:
        current, cost, path = queue.popleft()
        if minway[0] == 0 or cost <= minway[0]:
            circ = False
            for i in path:
                if i == current:
                    circ = True
                    break
            if circ == False:
                if current == n2:
                    minway = (cost,path + [current])
                    print(minway)
                for i in Mat:
                    if i[0] == current and path[len(path)-2] != current :
                        queue.append((i[1],cost + i[2], path + [current]))
    return minway


with open("input.txt") as f:
    A = f.read()

A = [list(map(int,x.split())) for x in A.split("\n")]
del(A[0])

n1 = int(input('n1 = '))
n2 = int(input('n2 = '))
print("Min = ",BFS(A,n1,n2))
