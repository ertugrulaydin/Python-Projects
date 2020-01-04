# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:59:28 2019

@author: Ertugrul_pc
"""
kareTop=0
top=0
topKare=0
for i in range(1,101):
    kareTop=kareTop+i*i
    top=top+i
topKare=(top)**2
print("Karelerin Toplamı= {}\nToplamların Karesi= {}\nFark= {}".format(kareTop,topKare,(topKare-kareTop)))