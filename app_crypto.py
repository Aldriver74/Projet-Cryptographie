from f_crypto import encode, decode, chiffrer, déchiffrer, clear_console, getMode, getMessage, getKey, getA0, getPoints_v2, lagrange_sympy, getNumberOfParts, getSecretFromPoly0, generatePointsverbose
from colorama import Back, Fore, Style, deinit, init
import os
import time
import pandas as pd 
from sympy import symbols, simplify
from sympy.abc import x
from sympy import Rational
import random

clear_console()
print(Fore.RED+'\033[1m'+'\nChoose an encryption method: \n\n'+Fore.BLUE+ \
      '         [1] CCSU (Caesar Cipher Salted and Updated, Security level:'+Fore.GREEN+' low'+Fore.BLUE+')\n' \
      '         [2] RSM (Random Salted Moduloes, Security level:'+Fore.GREEN+' medium'+Fore.BLUE+')\n' \
      '         [3] SSS (Shamir\'s Secret Sharing, Security level:'+Fore.GREEN+' high'+Fore.BLUE+', )\n'
        +Fore.RED+'\n                             ! Soon available !\n\n'+Fore.BLUE+\
      '         [4] OTP (One-time pad, Security level:'+Fore.GREEN+' high'+Fore.BLUE+', )\n\n'+Fore.GREEN)



method=input()

if method == "1" :
    clear_console()
    mode=getMode()
    clear_console()
    message = getMessage()
    clear_console()
    key = getKey()
    clear_console()
    print('mixing letters...')
    time.sleep(0.1)
    print('adding salt...')
    time.sleep(0.3)
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
        print('refinding letters...')
        time.sleep(0.1)
        print('removing salt...')
        time.sleep(0.3)
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
        print(Fore.WHITE+'getting rank for each letter...')
        time.sleep(0.1)
        print('generating truly random x1...')
        time.sleep(0.1)
        print('generating random x2...')
        time.sleep(0.1)
        print('encoding each letter...')
        time.sleep(0.1)
        print('adding salt...')
        time.sleep(0.3)
        if test == X :
            print (Fore.RED+"\nResult: \n\n"+Fore.BLUE+str(result[0])+Fore.RED+'\nYour key is:\n\n'+Fore.BLUE+str(result[1])+'_')
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
        print(Fore.WHITE+'refinding values of x1 and x2...')
        time.sleep(0.1)
        print('removing salt...')
        time.sleep(0.1)
        print('doing somes moduloes...')
        time.sleep(0.1)
        print('solving some equations...')
        time.sleep(0.1)
        print('refinding rank of each letter...')
        time.sleep(0.3)
        time.sleep(1.2)
        print (Fore.RED+"\nYour decrypted text is: \n\n"+'\033[0m'+Fore.BLUE+decode(ctext,password)+'\033[1m')
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
        generatePointsverbose(nandk[0], nandk[1], a0)
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')

    if mode[0] == 'd' or mode[0]== 'decrypt':
        xory=getPoints_v2()
        clear_console()
        print(Fore.WHITE+'separating values of x and y...')
        time.sleep(0.1)
        x_vals = xory[0]
        y_vals = xory[1]
        print(x_vals)
        time.sleep(0.1)
        print(y_vals)
        time.sleep(0.1)
        print('refinding true y values...')
        time.sleep(0.1)
        print('searching associated polynomial...')
        time.sleep(0.1)
        poly = lagrange_sympy(x_vals, y_vals)
        print(f"f(x)= {poly}")
        time.sleep(0.1)
        x=symbols('x')
        val_at_0 = poly.subs(x, 0)
        print(f"calculating y for x= 0 ... \n{val_at_0}")
        time.sleep(0.1)
        print(f'{val_at_0}')
        time.sleep(0.3)
        secret=round(val_at_0)
        finalmess=getSecretFromPoly0(secret)
        print(Fore.RED+'\nYour text is : \n \n'+Fore.GREEN+str(finalmess))
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')


print('\033[0m')