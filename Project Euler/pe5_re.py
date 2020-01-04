sayi=2520
b=True
while (b==True):
    a=True
    for i in range(2,21):
        if(sayi%i!=0):
            a=False
            break
    if(a):
        print(sayi)
        b=False
    else:
        sayi+=1
