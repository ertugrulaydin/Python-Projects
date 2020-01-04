import turtle       
def kare(kenar_uzunluk):
    for x in range(4):
        turtle.forward(kenar_uzunluk)
        turtle.right(90)
def eskenar_ucgen(kenar_uzunluk):
    for x in range(3):
        turtle.forward(kenar_uzunluk)
        turtle.right(120)
def ikizkenar_dik_ucgen(kenar_uzunluk):
    turtle.forward(kenar_uzunluk)
    turtle.right(90)
    turtle.forward(kenar_uzunluk)
    hipotenus=kenar_uzunluk*(2**(0.5))
    turtle.right(135)
    turtle.forward(hipotenus)
def daire(cap,derece):
    birim = (cap/3.14)/36
    for x in range(derece):
        turtle.forward(birim)
        turtle.right(1)
def elips(cap,basiklik):
    #elips fonksyonu cok küçük bir sapma iceriyor 
    birim = (cap/3.14159265)
    donme = 1
    for x in range(360):
        turtle.forward(birim)
        turtle.right(donme)
        if 0<x<=90 or 180<x<=270:
            birim += (birim*basiklik)/1000
        else:
            birim -= ((birim*basiklik)/1000)-((birim*basiklik)/100000)


            
def zincir(cap,basiklik,halka_sayisi):
    birim = (cap/3.14)
    donme = 1.0000000
    for x in range(halka_sayisi*180):
        turtle.forward(birim)
        turtle.right(donme)
        if 0<x<=90 or 180<x<=270:
            donme += (donme*basiklik)/1000
        else:
            donme -= (donme*basiklik)/1000

#def hatasiz_elips(cap,basiklik):  
 #   birim = (cap/3.14159265)
  #  donme = 1
    
    
   # for x in range(360,0):
    #    turtle.forward(birim)
     #   turtle.right(donme)
      #  if 0<x<=90 or 180<x<=270:
       #     a = 90-(x%90)
         #   while a>=0:
        #        birim += (birim*basiklik)/(1000**a)
          #      a +=1

       # else:
        #    birim -= (birim*basiklik)/1000
#harfler##harfler##harfler##harfler##harfler##harfler##harfler#

def A(punto):
    turtle.penup()
    turtle.forward(punto/10)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(punto*(2**(0.5)))
    turtle.right(90)
    turtle.forward(punto*(2**(0.5)))
    turtle.left(180)
    turtle.forward(punto*(2**(0.5))/2)
    turtle.left(45)
    turtle.forward(punto)
    turtle.penup()
    turtle.left(90)
    turtle.forward(punto/2)
    turtle.left(90)
    turtle.forward(punto*1.5)
def B(punto):
    turtle.penup()
    turtle.forward(punto/10)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(punto)
    turtle.right(90)
    for x in range(2):
        daire(punto/2,180)
        turtle.left(180)
    turtle.penup()
    turtle.forward(punto/2)
def C(punto):
    turtle.penup()
    turtle.forward(punto/10)
    turtle.forward(punto/2)
    turtle.left(90)
    turtle.forward(punto)
    turtle.left(90)
    turtle.pendown()
    birim = (punto/3.14)/36
    for x in range(180):
        turtle.forward(birim)
        turtle.left(1)
    turtle.penup()
def D(punto):
    turtle.penup()
    turtle.forward(punto/10)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(punto)
    turtle.right(90)
    daire(punto,180)
    turtle.left(180)
    turtle.penup()
    turtle.forward(punto/2)
def E(punto):
    turtle.penup()
    turtle.forward(punto/10)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(punto)
    turtle.right(90)
    turtle.forward(punto*0.75)
    turtle.penup()
    turtle.right(90)
    turtle.forward(punto*0.5)
    turtle.right(90)
    turtle.forward(punto*0.25)
    turtle.pendown()
    turtle.forward(punto*0.5)
    turtle.penup()
    turtle.left(90)
    turtle.forward(punto*0.5)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(punto*0.75)
#devam eder
def yaz(punto,yazi):
        alfabe={ A:A(punto) , B:B(punto) , C:C(punto), D:D(punto), E:E(punto),}#defam eder }
        for x in range(yazi):
            alfabe[x]
yaz(30,'ABCDE')
