def is_prime(n):
    j=2
    while j*j<=n:
        if n%j==0:
           return False
        j+=1
    return True

n=list(map(int,input().split()))
o=""
f=0
for i in range(2,len(n)):
    if n[i]<2 or n[i]>99:
        f=1
        break
    if is_prime(n[i]) and is_prime(i):
        o+="{ni} - at index {ind},".format(ind=i,ni=n[i])
        
if f==0:
    print(o)
else:
    print("invalid input")
        
        
