file = open("pe8.txt","r",encoding= "utf-8")
liste=[]
liste1=[]
a=''
for i in file:
    liste.append(i)
file.close()
for i in liste[::]:
    liste1.append(i[:50])
for i in liste1[::]:
    a+=i
str1=''
str2=''

for i in range(0,len(a)):
    for j in range(i,len(a)):
        if(i==13 and j==13):
            break
        str1+=str(i)
        str2+=str(j)
print(str1,str2)
            
        
            
    