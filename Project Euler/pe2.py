fib1=1
fib2=2
fib3=0
toplam=0
while (fib3<4000000):
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    if(fib3%2==0):
        toplam=toplam+fib3
print(toplam)
    
