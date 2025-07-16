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

symbol_value = pd.read_excel("symbol_value.xlsx")

def getValue(letter):
    ligne = symbol_value[symbol_value["Symbol"] == letter]
    if not ligne.empty:
        return int(ligne["Value"].values[0])

def getA0(text):
    a0=""
    for symbol in text:
        value=getValue(symbol)
        a0 += str("0"+ str(value)+"0")
    return a0

def getNumberOfParts():
    clear_console()
    print(Fore.RED+'\nNumber of parts:\n'+Fore.GREEN)
    n=int(input())
    clear_console()
    print(Fore.RED+'\nNumber of parts necessary to find the secret:\n'+Fore.GREEN)
    k=int(input())
    nork=[n, k]
    return nork 

def generatePoints(n, k, a0):
    coefficients=[a0]
    valuesofx=[]
    ypoints=[]
    for i in range (k-1):
        negorposc=secrets.randbelow(2)
        if negorposc == 1:
            ai=secrets.randbelow(3000000000000)
            coefficients.append(ai)
        else:
            ai=secrets.randbelow(3000000000000)
            coefficients.append(int(-ai))

    for z in range (n):
        negorposx=secrets.randbelow(2)
        if negorposx == 1:
            x=secrets.randbelow(300)
            y=sum(a *x**i for i, a in enumerate(coefficients))
            k=secrets.randbelow(300)
            print(Fore.GREEN+"("+str(x)+","+str(y+1596875498654165685896478585698569852589*k)+")"+Fore.WHITE)
            #print(Fore.GREEN+"("+str(x)+","+str(y)+")"+Fore.WHITE)
        
        else:
            x=secrets.randbelow(300)
            x=int(-x)
            y=sum(a *x**i for i, a in enumerate(coefficients))
            k=secrets.randbelow(300)
            print(Fore.GREEN+"("+str(x)+","+str((y+1596875498654165685896478585698569852589*k))+")"+Fore.WHITE)
            #print(Fore.GREEN+"("+str(x)+","+str(y)+")"+Fore.WHITE)

def getPoints():
    print(Fore.RED+'How many points do you need ?\n'+Fore.GREEN)
    k=int(input())
    clear_console()
    print(Fore.RED+'Enter your point, one by one :')
    x_s=[]
    y_s=[]
    for i in range (0, k):
        print (Fore.RED+"\n Point x "+str(i+1)+" :\n"+Fore.GREEN)
        xpoint=input()
        x_s.append(int(xpoint))
        print (Fore.RED+"\n Point y "+str(i+1)+" :\n"+Fore.GREEN)
        ypoint=input()
        ypoint=(int(ypoint) % 1596875498654165685896478585698569852589)
        ypoint=(int(ypoint))
        y_s.append(ypoint)
    x_s = [Rational(x) for x in x_s]
    y_s = [Rational(y) for y in y_s]
    xory=[x_s, y_s]
    return xory

def lagrange_sympy(x_vals, y_vals):
    x = symbols('x')
    n = len(x_vals)
    P = 0
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                xi=int(x_vals[i])
                xj=int(x_vals[j])
                print (type(x))
                term *= (x - xj) / (xi - xj)
        P += term
    return simplify(P)

def getLetterFromValue(number):
    ligne = symbol_value[symbol_value["Value"] == int(number) ]
    if not ligne.empty:
        return str(ligne["Symbol"].values[0])
    
def findTrueValue(text):
    return re.findall(r'0(.*?)0', text) 
    
def getSecretFromPoly0(text):
    text='0'+str(text)
    secret=findTrueValue(str(text))
    finalmess=""
    for i in range (0, len (secret)):
        letter=getLetterFromValue(secret[i])
        finalmess += str(str(letter))
    return finalmess


mode=getMode()
clear_console()
if mode[0] == 'e' or mode[0]== 'encrypt':
    print(Fore.RED +"\nEnter your text:\n"+Fore.GREEN)
    X=input()
    clear_console()
    a0=getA0(X)
    a0=int(a0)
    nandk=getNumberOfParts()
    clear_console()
    print(Fore.RED+'Your points are : \n'+Fore.GREEN)
    generatePoints(nandk[0], nandk[1], a0)

if mode[0] == 'd' or mode[0]== 'decrypt':
    xory=getPoints()
    x_vals = xory[0]
    y_vals = xory[1]
    #print(type(x_vals), x_vals)
    #print(type(y_vals), y_vals)
    poly = lagrange_sympy(x_vals, y_vals)
    #print(f"Polynôme exact : {poly}")
    x=symbols('x')
    val_at_0 = poly.subs(x, 0)
    #print(f"Valeur exacte en x = 0 : {val_at_0}")
    secret=round(val_at_0)
    finalmess=getSecretFromPoly0(secret)
    print(str(finalmess))

    


