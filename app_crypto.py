from f_crypto import encode, decode, chiffrer, déchiffrer, clear_console, getMode, getMessage, getKey, generatePoints, getA0, getPoints, lagrange_sympy, getNumberOfParts, getSecretFromPoly0
from colorama import Back, Fore, Style, deinit, init
import os
import pandas as pd 
from sympy import symbols, simplify
from sympy.abc import x
from sympy import Rational
import random

print(Fore.RED+'\033[1m'+'\nChoose an encryption method: \n\n'+Fore.BLUE+ \
      '         1 CCSU (Caesar Cipher Salted and Updated, Security level:'+Fore.GREEN+' low'+Fore.BLUE+')\n' \
      '         2 RSM (Random Salted Moduloes, Security level:'+Fore.GREEN+' medium'+Fore.BLUE+')\n' \
      '         3 SSS (Shamir\'s Secret Sharing, Security level:'+Fore.GREEN+' high'+Fore.BLUE+', )\n'
        +Fore.RED+'\n                             ! Soon available !\n\n'+Fore.BLUE+\
      '         4 OTP (One-time pad, Security level:'+Fore.GREEN+' high'+Fore.BLUE+', )\n\n'+Fore.GREEN)

method=input()

if method == "1" :
    clear_console()
    mode=getMode()
    clear_console()
    message = getMessage()
    clear_console()
    key = getKey()
    clear_console()
    print(Fore.RED+'\nYour translated text is:\n'+Fore.BLUE)
    if mode[0] == 'e' or mode[0]== 'encrypt':
        code = chiffrer(message,key)
        print('\033[0m'+Fore.BLUE+str(code)+'\033[1m')
        print (Fore.RED+'\n Do not forget your key:\n'+Fore.BLUE)
        print('\033[0m'+Fore.BLUE+str(key)+'\033[1m')
        decode = déchiffrer(code,key)
        if decode == message:
            print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')
        else:
            print (Fore.RED+'\nSomething went wrong, retry\n')
            print (Fore.WHITE+'['+Fore.RED+decode+Fore.WHITE+']\n')
        
    if mode[0] == 'd' or mode[0]== 'encrypt':
        code = déchiffrer(message, key)
        print('\033[0m'+Fore.BLUE+code+'\033[1m')
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n'+'\033[1m')

if method == "2" :
    clear_console()
    print(Fore.RED+"\n Do you want to encode (e) or decode (d) your message\n"+Fore.GREEN)    
    choice=input()
    clear_console()
    if choice == "e" or choice == "encode":
        print(Fore.RED +"\nEnter your text:\n"+Fore.GREEN)
        X=input()
        result=encode(X)
        test=decode(result[0], result[1])
        clear_console()
        if test == X :
            print (Fore.RED+"\n Result: \n\n"+'\033[0m'+Fore.BLUE+str(result[0])+Fore.RED+'\033[1m'"\n \n Your key is:\n\n"+'\033[0m'+Fore.BLUE+str(result[1])+'_'+'\033[1m')
            print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')
        else: 
            print (Fore.RED+"Something went wrong, retry")

    if choice == "d"or choice == "decode":
        clear_console()    
        print(Fore.RED+"\n Enter your crypted text:\n"+Fore.GREEN)
        ctext=input()
        clear_console()
        print(Fore.RED+"\n Enter the password:\n"+Fore.GREEN)
        password=input()
        clear_console()
        print (Fore.RED+"\n Your decrypted text is: \n\n"+'\033[0m'+Fore.BLUE+decode(ctext,password)+'\033[1m')
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')

if method == "3" :
    clear_console()
    mode=getMode()
    clear_console()
    if mode[0] == 'e' or mode[0]== 'encrypt':
        print(Fore.RED +"\nEnter your text (less than 10 symbols):\n"+Fore.GREEN)
        X=input()
        clear_console()
        a0=getA0(X)
        a0=int(a0)
        nandk=getNumberOfParts()
        clear_console()
        print(Fore.RED+'Your points are : \n'+Fore.GREEN)
        generatePoints(nandk[0], nandk[1], a0)
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')

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
        clear_console()
        print(Fore.RED+'Your text is : \n '+Fore.GREEN+str(finalmess))
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')

print('\033[0m')