from __future__ import division
from __future__ import print_function
import secrets
import re
from colorama import Back, Fore, Style, deinit, init
from f_crypto import getMode, clear_console
import pandas as pd 
from sympy import symbols, simplify
from sympy.abc import x
from sympy import Rational
import random

def generatePoints(n, k, a0):
    coefficients=[a0]
    valuesofx=[]
    ypoints=[]
    for i in range (k-1):
        negorposc=secrets.randbelow(2)
        if negorposc == 1:
            ai=secrets.randbelow(3)
            coefficients.append(ai)
        else:
            ai=secrets.randbelow(3)
            coefficients.append(int(-ai))
    print(coefficients)
    
    for z in range (n):
        negorposx=secrets.randbelow(2)
        if negorposx == 1:
            x=secrets.randbelow(300)
            y=sum(a *x**i for i, a in enumerate(coefficients))
            print(y)
            #mod=random.randint(y, 300000000000)
            #print(Fore.GREEN+"("+str(x)+","+str(y+10000003*mod)+")"+Fore.WHITE)
            print(Fore.GREEN+"("+str(x)+","+str(y)+")"+Fore.WHITE)
        else:
            x=secrets.randbelow(300)
            x=int(-x)
            y=sum(a *x**i for i, a in enumerate(coefficients))
            print(y)
            #mod=random.randint(y, 300000000000 )
            #print(Fore.GREEN+"("+str(x)+","+str(y+10000003*mod)+")"+Fore.WHITE)
            print(Fore.GREEN+"("+str(x)+","+str(y)+")"+Fore.WHITE)

def getNumberOfParts():  
    print(Fore.RED+'\nNumber of parts:\n'+Fore.GREEN)
    n=int(input())
    print(Fore.RED+'\nNumber of parts necessary to find the secret:\n'+Fore.GREEN)
    k=int(input())
    nork=[n, k]
    return nork 

symbol_value = pd.read_excel("symbol_value.xlsx")

def getValue(letter):
    ligne = symbol_value[symbol_value["Symbol"] == letter]
    if not ligne.empty:
        print (int(ligne["Value"].values[0]))
        return int(ligne["Value"].values[0])
    
def getA0(text):
    a0=""
    for symbol in text:
        value=getValue(symbol)
        a0 += str("0"+ str(value)+"0")
    return a0

print(Fore.RED +"\nEnter your text:\n"+Fore.GREEN)
X=input()
a0=getA0(X)
a0=int(a0)
print(a0)
nandk=getNumberOfParts()
print(Fore.RED+'Your points are : \n'+Fore.GREEN)
generatePoints(nandk[0], nandk[1], a0)