# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 02:22:15 2019

@author: Ertugrul_pc
"""
sonuc=2
toplam=0
for i in range(2,1001):
    sonuc=sonuc*2
a=str(sonuc)
for j in a[:]:
    toplam=toplam+int(j)
print(toplam)