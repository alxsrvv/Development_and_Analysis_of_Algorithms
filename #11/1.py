from collections import deque

Mat = [[0,1,0,0,0,0,0,0,0],
       [1,0,1,1,1,1,0,0,0],
       [0,1,0,0,1,1,0,0,0],
       [0,1,0,0,1,0,0,1,0],
       [0,1,1,1,0,0,1,1,1],
       [0,1,1,0,0,0,0,1,1],
       [0,0,0,0,1,0,0,1,0],
       [0,0,0,1,1,1,1,0,0],
       [0,0,0,0,1,1,0,1,0]]

n1 = int(input('n1 = '))
n2 = int(input('n2 = '))

def BFS (Mat,n1,n2):
    if n1 == n2:
        return [n1]
    queue = deque([(n1,[])])
    while queue:
        current, path = queue.popleft()
        for j in range(len(Mat[current])):
            if Mat[current][n2]==1:
                return path + [current, n2]
            if Mat[current][j]==1:
                queue.append((j, path + [current]))
    return None

print(BFS(Mat,n1,n2))
