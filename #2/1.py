def rec(n,i):
   if n==1:
        return 2/7
   else:
        return (n+1)/(2*n+5) + rec(n-1,i)

n = int(input('n = '))
i = int(input('i = '))
x = rec(n,i)
print(x)
