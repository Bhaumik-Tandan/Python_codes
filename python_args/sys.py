#python sys.py 3 4 2 5 jljkj "eafsdfs"  32.3232 2+3i 3+9 3 + 3 i

from sys import argv
#first_argumrnt is always file name
print(len(argv),type(argv))
for i in argv:
    print(i,type(i))#all are type string and seperated by space