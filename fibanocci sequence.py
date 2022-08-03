# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:41:19 2022

@author: LENOVO
"""

n_terms = int(input("Enter number of terms:"))

n1 = 0
n2 = 1
count = 0

if n_terms <= 0:
    print("Enter a postive number")
elif n_terms == 1:
    print("Fibanocci sequence is:",n1 )
else:
    print("Fibanocci sequence:")
    while count < n_terms:
          print(n1)
          nth = n1 + n2
          n1 = n2
          n2 = nth
          count +=1
          


