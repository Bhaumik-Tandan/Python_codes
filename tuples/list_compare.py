from sys import getsizeof as gs
a=[2,3,5,4]
t=(2,3,4,5)
p=tuple(a)
print(gs(a,"bytes"),gs(t,"bytes"),gs(p,"bytes"))