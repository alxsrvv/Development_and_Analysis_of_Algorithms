import math

print('method karatsuba')
x = int(input('x = '))
y = int(input('y = '))

def multiply(x, y):
    sx = str(x)
    sy = str(y)
    nx = len(sx)
    ny = len(sy)
    if nx==1 or ny==1:
        r = int(x)*int(y)
        return r
    n = nx
    if nx>ny:
        sy = sy.rjust(nx, '0')
        n = nx
    elif ny>nx:
        sx = sx.rjust(ny, '0')
        n = ny
    m = n % 2
    offset = 0
    if m!=0:
        n+=1
        offset = 1
    floor = int(math.floor(n/2))-offset
    ceil = int(math.ceil(n/2))-offset
    a = sx[0:floor]
    b = sx[ceil:n]
    c = sy[0:floor]
    d = sy[ceil:n]
    r = ((10**n)*multiply(a,c)) + ((10**(n/2))*(multiply(a,d) + multiply(b,c))) + multiply(b,d)
    return r


print(multiply(x,y))