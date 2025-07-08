from f_crypto import encode, decode, chiffrer, déchiffrer, clear_console, getMode, getMessage, getKey
import time
from colorama import Back, Fore, Style, deinit, init
import os

print(Fore.RED +'\nChoose an encryption method: \n\n'+Fore.BLUE+ \
      '         1 CCSU (Caesar Cipher Salted and Updated, Security level:'+Fore.GREEN+' low'+Fore.BLUE+')\n' \
      '         2 RSM (Random Salted Moduloes, Security level:'+Fore.GREEN+' medium'+Fore.BLUE+')\n' \
      +Fore.RED+'\n                             ! Soon available !\n\n'+Fore.BLUE+
      '         3 SSS (Shamir\'s Secret Sharing, Security level:'+Fore.GREEN+' high'+Fore.BLUE+', )\n' \
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
        print(code)
        print (Fore.RED+'\n Do not forget your key:\n'+Fore.BLUE)
        print(key)
        decode = déchiffrer(code,key)
        if decode == message:
            print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')
        else:
            print (Fore.RED+'\nSomething went wrong, retry\n')
            print (Fore.WHITE+'['+Fore.RED+decode+Fore.WHITE+']\n')
        
    if mode[0] == 'd' or mode[0]== 'encrypt':
        code = déchiffrer(message, key)
        print(code)
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')

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
            print (Fore.RED+"\n Result: \n\n"+Fore.BLUE+str(result[0])+Fore.RED+':'+"\n \n Your key is:\n\n"+Fore.BLUE+str(result[1])+'_')
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
        print (Fore.RED+"\n Your decrypted text is: \n\n"+Fore.BLUE+decode(ctext,password))
        print (Fore.WHITE+'\n['+Fore.GREEN+'SUCCESS'+Fore.WHITE+']\n')