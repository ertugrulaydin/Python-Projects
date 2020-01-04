# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 02:08:08 2019

@author: Ertugrul_pc
"""
sonuc=0
sayilar={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:7,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:4,50:5,60:5,70:7,80:6,90:6,100:7,1000:10}
for i in range(1,1001):
    if(i<=20):
        a=sayilar[i]
        sonuc=sonuc+a
    elif(i>20 and i<100):
        for j in range(0,2):
            onlar=int(i/10)
            a=sayilar[onlar]
            sonuc=sonuc+a
        birler=i%10
        if(birler==0):
            a=sayilar[i]
            sonuc=sonuc+a
        else:
            a=sayilar[birler]
            sonuc=sonuc+a
    elif(i>=100 and i<1000):
        yuzler=int(i/100)
        if(yuzler==1):
            for j in range(0,3):
                if(j==0):
                    birler=i%10
                    if(birler!=0):
                        a=sayilar[birler]
                        sonuc=sonuc+a
        
                elif(j==1):
                    sayi=i%100
                    onlar=i-sayi
                    if(onlar!=0):
                        a=sayilar[onlar]
                        sonuc=sonuc+a
                elif(j==2):
                    sayi=int(i/100)
                    yuzler=sayi%10
        elif(yuzler>1):
            a=sayilar[yuzler]
            sonuc=sonuc+a+10
    else:
        sonuc=sonuc+10
print(sonuc)
        
        
        
