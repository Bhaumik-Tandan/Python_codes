class t:
    f=323

a=t()

a.f=23
b=t()
print(b.f)
t.f=32
print(b.f)