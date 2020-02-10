from math import factorial
from math import exp

def NonRec(x,n):
        '''
        From start s is 1. n+1 times function will totalize conjunctions.
        Then return our sum.
        Parameters:
        x,n
        '''
        s = 1
        for i in range(1,n+1):
                x+=x**i/factorial(i)
        return s

def Rec(x,n):
        '''
        Then n is 0, function return 1.
        If n is anything else, function return recursive of itself.
        Parameters:
        x,n
        '''
        if n == 0:
                return 1
        else:
                return x**n/factorial(n)+Rec(x,n-1)

x = float(input('x = '))
eps = float(input('eps = '))

n = 0
term = 1
while (abs(term)>eps):
	term = term*x/(n+1)
	n+=1
print('number of terms = ',n)

y2 = Rec(x,n)
y3 = exp(x)
y4 = NonRec(x,n)
error2 = abs(y2-y3)
error3 = abs(y4-y3)

print('y2(NonRec) = ',y4)
print('y(math) = ',y3)
print('y(Rec) = ',y2)
print('error2 = ',error2)
print('error3 = ',error3)
