def asalMi(sayi):
    sayac=0
    for i in range(2,int(sayi)):
          if(int(sayi)%i==0):
                sayac+=1
                break
    if(sayac!=0):
          return 0
    else:
          return 1
sayi=3
asalCount=1
asal=[2]
while True:
#    a=asalMi(sayi)
    
    if(asalMi(sayi)==1):
        asalCount+=1
    if(asalCount==10001):
        print(sayi)
        break
    sayi+=1

    
