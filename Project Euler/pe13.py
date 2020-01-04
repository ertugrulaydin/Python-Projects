file = open("pe13.txt","r",encoding= "utf-8")
liste=[]
liste1=[]
for i in file:
    liste.append(i)

file.close()

for i in liste[::]:
    liste1.append(i[:50])

toplam=0
for i in liste1:
    toplam+=int(i)
st=str(toplam)
print(st)
print(st[0:10])
