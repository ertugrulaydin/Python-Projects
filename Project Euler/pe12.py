# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:45:42 2019

@author: Ertugrul_pc
"""
#sayac=0
#ucgenSayi=1
#def ucgenSayilarinBolenleri():
#    while True:
#        for i in range(2,pass):
#           
#            if (ucgenSayi%i==0):
#                print("i=",i,"ucgenSayi=",ucgenSayi,"sayac=",sayac)
#                sayac+=1
#            
#        if(sayac==5):
#            print(ucgenSayi)
#            break;



def ucgenSayiBulma():
    ucgenSayi=0
    bolenler=0
    i=1
    liste=[]
#    a=int(input("kacinci ucgen sayisi bulunsun?"))
    while True:
#    for i in range (1,a+1):
        
        ucgenSayi+=i
#    print(ucgenSayi)
#    for i in range(2,ucgenSayi+1):
        if(ucgenSayi%i==0):
            liste.append(i)
            bolenler+=1
        if(bolenler>=500):
            print(liste)
            print(ucgenSayi)
            break
        i+=1
ucgenSayiBulma()