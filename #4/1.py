import random

first = []
second = []

n,k=int(input("n=")),int(input("k="))

for i in range (n):
    first.append(random.randint(0,100))
first.sort()
for i in range (k):
    second.append(random.randint(0,100))
print(first, second)

def binar(f,s):
    #worst - 1 + log 2 n
    #best - 1
    for k in s:
        left = 0
        right = len(f)
        while left < right-1:
            mid = (left+right)//2
            if f[mid] > k:
                right = mid
            else:
                left = mid

        if left >= 0 and f[left] == k:
            print ("YES (for", k,")")
        else:
            print ("NO (for", k,")")


binar(first,second)
