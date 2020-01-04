toplam=0
for i in range(3,1000):
    if(i%3==0):
        toplam=toplam+i
    elif(i%5==0):
        toplam=toplam+i
    else:
        continue
print(toplam)
