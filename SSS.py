from __future__ import division
from __future__ import print_function
import secrets
import re
from colorama import Back, Fore, Style, deinit, init
from f_crypto import getMode, clear_console
import pandas as pd 



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
        mod=secrets.randbelow(30000000000000000)
        negorposx=secrets.randbelow(2)
        if negorposx == 1:
            x=secrets.randbelow(300)
            y=sum(a *x**i for i, a in enumerate(coefficients))
            print(Fore.GREEN+"("+str(x)+","+str(y+10000003*mod)+")"+Fore.WHITE)
        else:
            x=secrets.randbelow(300)
            x=int(-x)
            y=sum(a * int(-x)**i for i, a in enumerate(coefficients))
            print(Fore.GREEN+"("+str(x)+","+str(y+1000003*mod)+")"+Fore.WHITE)


def getPoints():
    print(Fore.RED+'How many points do you need ?\n'+Fore.GREEN)
    k=int(input())
    clear_console()
    print(Fore.RED+'Enter your point, one by one :')
    x_s=[]
    y_s=[]
    for i in range (0, k):
        print (Fore.RED+"Point x "+str(i)+" :\n"+Fore.GREEN)
        xpoint=input()
        x_s.append(xpoint)
        print (Fore.RED+"Point y "+str(i)+" :\n"+Fore.GREEN)
        ypoint=input()
        y_s.append(ypoint)
    xory=[x_s, y_s]
    return xory


#________\ NOT MY CODE that's why this shit doesn't work /________

def lagrange_interpolate(x, x_s, y_s, p):
    """
    Find the y-value for the given x, given n (x, y) points;
    k points will define a polynomial of up to kth order.
    """
    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (divmod(num, den, p) + p) % p

#_________________________________


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
    r=lagrange_interpolate(0, xory[0], xory[1], 1000003)
    


