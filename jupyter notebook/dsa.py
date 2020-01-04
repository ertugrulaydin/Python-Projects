def buyuk(liste2):
    maxNumber=int(liste2[0])
    for i in liste2:
        b=int(i)
        if (maxNumber<b):
            maxNumber = b
        
    print("en buyuk sayi=",maxNumber)
    
                
a=input("pozitif sayi listesi giriniz:")
liste=a.split(" ")

for i in liste[:]:
    if(i==" "):
        liste.remove(i)

buyuk(liste)
