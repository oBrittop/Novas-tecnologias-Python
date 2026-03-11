# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:48:14 2026

@author: gustavo.rbrito
"""
lista = {}
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura:"))
mmc = peso / (altura*altura)

if mmc <= 18.5:
    print("voce ta abaixo do peso com um mmc de :")
    print(round(mmc, 2))
    
elif mmc > 18.5 and mmc <=24.9 :
    print("Ie disgrama ta com o peso normal com um mmc de :")
    print(round(mmc, 2))
    
elif mmc > 24.9 and mmc <= 29.9:
    print("Voce ta com o sobre peso com um mmc de :")
    print(round(mmc, 2))
    
elif mmc > 30:
    print("Ta na lombra da baleia fih, com um mmc de :")
    print(round(mmc, 2))
    
else:
    print("Digite um valor valido")






