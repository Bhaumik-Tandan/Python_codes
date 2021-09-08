def conv(mode):
    if mode==1:
        return lambda c : c * (9.0/5) + 32
    if mode==2:
        return lambda f : (f-32) * 5.0/9
c=conv(1)
f=conv(2)
print("58 Celcius is "+str(c(58))+" Fahrenheit")
print("58 Fahrenheit is "+str(f(58))+" Celcius")
