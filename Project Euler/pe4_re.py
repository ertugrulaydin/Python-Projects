
liste=[]
for i in range(999,99,-1):
    for j in range(i,99,-1):
        sayi=i*j
        a=str(sayi)
        if(a==a[::-1]):
            liste.append(int(a))
print(max(liste))
        
            
##liste=[15647] len=6  int(6/2)  int(7/2)
            