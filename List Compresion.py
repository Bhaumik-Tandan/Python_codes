from random import randint as rand

l=[[rand(1, 2**31-1) for i in range(4)] for j in range(4)]
nl=[[j+j%2 for j in i] for i in l]
