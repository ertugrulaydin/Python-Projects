import time
start=time.time()

liste=[0]
yedek=0
for i in range(2,1000001):
    sayi=i
    sayac=0

    while(sayi!=1):
        sayac+=1
        if(sayi%2==0):
            sayi=sayi/2
        else:
            sayi=((sayi*3)+1)            
    if(sayac>yedek):
        yedek=sayac
        a=i
print(a)
elapsed = (time.time() - start)
print("elapsed time:",elapsed)
