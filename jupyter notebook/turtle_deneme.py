import turtle
t=turtle
t.title("Matematik Gösterim")
t.setup(width=500,height=500,startx=100,starty=100)
def f(a):
    t.forward(a)
def r(a):
    t.right(a)
def l(a):
    t.left(a)
def s(a,b):
    t.setpos(a,b)
def cizgi_cekx():
    for j in range(0,10):
        if(j%2):
            f(10)
            r(180)
            f(10)            
        for k in range(0,5):
            t.penup()
            PX,PY=t.pos()
            PX+=10
            s(PX,PY)
            t.pendown()
            r(180)
            f(10)
def cizgi_ceky():
    for j in range(0,10):
        if(j%2):
            r(180)
            f(20)
        for k in range(0,5):
            t.penup()
            PX,PY=t.pos()
            PY+=10
            s(PX,PY)
            t.pendown()
            r(180)
            f(10) 
def arti_ciz():
    f(250)
    r(180)
    f(500)
    r(90)
    f(10)
    cizgi_cekx()
    t.penup()
    s(0,250)
    t.pendown()
    f(500)
    r(90)
    cizgi_ceky()
    t.penup()
    s(-250,0)
    t.pendown()
# başlangıç ayarlar
class fonksyon():
    def __init__(self,a=0,b=0,c=0,d=0,e=0):
        self.a=a
        self.b=b
        self.c=c 
        self.d=d
        self.e=e       
    def geri_ver(self,X):
        return (self.a*(X**4))+(self.b*(X**3))+(self.c*(X**2))+(self.d*(X**1))+(self.d)

def grafik_ciz(girdi,olcek=1):
    t.penup()
    s(-250,0)
    t.pendown()
    PX,PY=t.pos()
    for j in range(500):
        t.setposition(PX,(girdi.geri_ver(PX)*olcek))
        PX+=1
i=0 # i'nin değerinden emin olmak için
arsiv={1:fonksyon()} #arsivi tanımladim
for i in range(5):
    arsiv[i]=fonksyon()

def son_cizdir(fonk_sayisi,renk,olcek):
    for j in range(0,fonk_sayisi):
        t.pencolor(renk[j])
        grafik_ciz(arsiv[j],olcek)
def renk_sor(fonkno):
    print("%d nolu fonsyonun rengini girin seçenekleriniz kırmızı mavi turuncu pembe sarı siyah ve gıridir" %(fonkno))
    renk = raw_input()
    if renk=="kirmizi":
        return "red"
    elif renk=="mavi":
        return "blue"
    elif renk=="turuncu":
        return "orange"
    elif renk=="pembe":
        return "pink"
    elif renk=="sari":
        return "yellow"
    elif renk=="siyah":
        return "black"
    elif renk=="giri":
        return "grey"
    else:
        print("girdiğiniz renk anlaşılamadı lütfen tekrar türkçe karakterler olmadan giriniz")
        renk_sor(fonkno)
def fonk_sor(fonkno):
    degerler=[0,1,2,3,4]
    print ("Lütfen %d nolu fonksyonu giriniz"%(fonkno))
    for i in range(5):
        degerler[i]=input('X^%d olan terimin katsayisi'%(i))
    arsiv[fonkno]=fonksyon(degerler[0],degerler[1],degerler[2],degerler[3],degerler[4],)
def olcek_belirle(fonk_sayisi):
    en_buyuk=0
    for fonk_no in range(0,fonk_sayisi):
        PX = -250
        for j in range(500):
            PX +=1
            if (arsiv[fonk_no].geri_ver(PX)>en_buyuk or -1*(arsiv[fonk_no].geri_ver(PX))>en_buyuk):
                en_buyuk = arsiv[fonk_no].geri_ver(PX)
                if en_buyuk<0:
                    en_buyuk= -1*en_buyuk
    if en_buyuk==0:
        print ("hata kodu 0")
        return 1
    return 250.000/en_buyuk
##########ANA GÖVDE###########################
kontrol=True
while kontrol:
    try:
        fonk_sayisi = input('kaç adet fonksyon girmek istiyorsunuz')
        kontrol = False
    except:    
        kontrol=True
renk=["0","0","0","0","0","0"]
fonkno=0
kontrol1=True
while kontrol1:
    try:

        for fonkno in range(fonk_sayisi):
            fonk_sor(fonkno)
            renk[fonkno]= renk_sor(fonkno)
            fonkno+=1
        kontrol1=False
    except:
        kontrol1=True


olcek=olcek_belirle(fonk_sayisi)
arti_ciz()
son_cizdir(fonk_sayisi,renk,olcek)
