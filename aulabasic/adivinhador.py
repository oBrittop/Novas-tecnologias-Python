# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:05:34 2026

@author: gustavo.rbrito
"""
n = 0
MAX = 5
numero_secreto = 33
print("Tente adivinhar o numero secreto!!")

while n < MAX:
    num = int(input("Digite um numero: "))
    if num > numero_secreto:
        n = n+1
        print("o numero secreto e menor que isso! ")
        print(f"Tentativas{n}/5\n")
        
    elif num < numero_secreto:
        n = n+1
        print("O numero secreto e maior que isso! ")
        print(f"Tentativas{n}/5\n")
    else:
        print("Parabens, acertou!!!")
        break
        