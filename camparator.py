def com(x):
    return x[0]
a=[(8,0),(9,1),(89,2),(9,3),(8,4)]

a.sort(key=com)
print(a)