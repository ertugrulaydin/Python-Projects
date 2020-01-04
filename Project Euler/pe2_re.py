# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:01:12 2019

@author: Ertugrul_pc
"""

fib1=1
fib2=2
sonuc=2
fib3=3
while(fib3<=4000000):
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    if(fib3%2==0):
        sonuc=sonuc+fib3
print(sonuc)