from __future__ import division
from __future__ import print_function
import random
import re
import time
import secrets
import os
from colorama import Back, Fore, Style, deinit, init
import pandas as pd 
from sympy import symbols, simplify
from sympy.abc import x
from sympy import Rational



symbol_value = pd.read_excel("symbol_value.xlsx")
SYMBOLS = 'AՒՔաբդեէըթժضЙصЦثBقУفК غC3-ሀለሐመعЕğアカサタナハマهςε567ᚱሠረሰሸᚹᚻ890\'ρ\"τЁ:;,.?!ゾドボポخDᚠᚨᛃحНجቀበቨተቸኀነûŭůυθιοù/úüūヤラワガザダバűիᚺųኘአከπασ^δφụᛗᛜᚲՋГኸወዐዘዠየደጀገጨጠጰጸፈፀፐشEسШγηသパイキシチニヒξκيЩᛟᛉ1بFԲԳԵلЗဆတနမအပကミリヰギジヂビငا2Хت4GنФمЫكHطВАذλζχψωβμIᛜᛏПءόРJؤОىЛώピウクスツヌフئKДЖوLЭàᛚᛝâáãЯMźظЧСNМစရေ်ျးယဖထИOИТPЬЪQБЮRSTUVWXYZaйцခလဘညာbуžéᛇᛒᚾèêëкムユルグズヅブcеēėęðěёdнгĕəẹeшщfзхgņňŋṅķƙфыŕプエケセテネヘřẁẃhвㅂㅈㄷㄱŵẅаɓñńiпשçԷԹԻԽԿՀՁՂՃՌՍՎՏՐՑćメレヱゲゼデベĉčדגכроĵĥоעיחלß§śŝšṣşףזסлjджkэяlペオコソトノホקч쇼ㅕㅑㅐㅔㅁㄴㅇㄹ호ㅓㅏㅣㅋㅌㅊ퓨ㅜㅡсmרмאḍɗטиוןםפ月了嘛起来nтьoъpĺľļł·бюqrstuvÿýỳŷƴwțţxṭįīïîìíị来说你好ıyþťzôœòó呀モヨロヲンゴ美啊õöøōőήọºΕΡΤΥΘΙΟΠ走路ΑΣΔΦΓΗΞ法ΚΛΖΧΨΩΒΝΜ'
MAX_KEY_SIZE = len(SYMBOLS)
sep = [':', '_']
full_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
    'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
    'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
    'Ѐ', 'Ё', 'Ђ', 'Ѓ', 'Є', 'Ѕ', 'І', 'Ї', 'Ј', 'Љ', 'Њ', 'Ћ', 'Ќ', 'Ѝ', 'Ў', 'Џ',
    'ѐ', 'ё', 'ђ', 'ѓ', 'є', 'ѕ', 'і', 'ї', 'ј', 'љ', 'њ', 'ћ', 'ќ', 'ѝ', 'ў', 'џ',
    'Ѡ', 'ѡ', 'Ѣ', 'ѣ', 'Ѥ', 'ѥ', 'Ѧ', 'ѧ', 'Ѩ', 'ѩ', 'Ѫ', 'ѫ', 'Ѭ', 'ѭ', 'Ѯ', 'ѯ',
    'Ѱ', 'ѱ', 'Ѳ', 'ѳ', 'Ѵ', 'ѵ', 'Ѷ', 'ѷ', 'Ѹ', 'ѹ', 'Ѻ', 'ѻ', 'Ѽ', 'ѽ', 'Ѿ', 'ѿ',
    'Ҁ', 'ҁ', 'Ҋ', 'ҋ', 'Ҍ', 'ҍ', 'Ҏ', 'ҏ', 'Ґ', 'ґ', 'Ғ', 'ғ', 'Ҕ', 'ҕ', 'Җ', 'җ',
    'Ҙ', 'ҙ', 'Қ', 'қ', 'Ҝ', 'ҝ', 'Ҟ', 'ҟ', 'Ҡ', 'ҡ', 'Ң', 'ң', 'Ҥ', 'ҥ', 'Ҧ', 'ҧ',
    'Ҩ', 'ҩ', 'Ҫ', 'ҫ', 'Ҭ', 'ҭ', 'Ү', 'ү', 'Ұ', 'ұ', 'Ҳ', 'ҳ', 'Ҵ', 'ҵ', 'Ҷ', 'ҷ',
    'Ҹ', 'ҹ', 'Һ', 'һ', 'Ҽ', 'ҽ', 'Ҿ', 'ҿ', 'Ӏ', 'Ӂ', 'ӂ', 'Ӄ', 'ӄ', 'Ӆ', 'ӆ', 'Ӈ',
    'ӈ', 'Ӊ', 'ӊ', 'Ӌ', 'ӌ', 'Ӎ', 'ӎ', 'ӏ', 'Ӑ', 'ӑ', 'Ӓ', 'ӓ', 'Ӕ', 'ӕ', 'Ӗ', 'ӗ',
    'Ә', 'ә', 'Ӛ', 'ӛ', 'Ӝ', 'ӝ', 'Ӟ', 'ӟ', 'Ӡ', 'ӡ', 'Ӣ', 'ӣ', 'Ӥ', 'ӥ', 'Ӧ', 'ӧ',
    'Ө', 'ө', 'Ӫ', 'ӫ', 'Ӭ', 'ӭ', 'Ӯ', 'ӯ', 'Ӱ', 'ӱ', 'Ӳ', 'ӳ', 'Ӵ', 'ӵ', 'Ӷ', 'ӷ',
    'Ӹ', 'ӹ', 'Ӻ', 'ӻ', 'Ӽ', 'ӽ', 'Ӿ', 'ӿ',
    'ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß',
    'ç', 'Ç', 'à', 'é', 'è', 'ê', 'ï', 'ë', 'ô', 'û', 'â', 'É', 'È', 'Ê', 'Ô', 'À',
    'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي',
    '\'', ' ', ',', '-', '.', '!', '?', ':', ';', '&', '%', '@', '*', '+', '/', '\n', '_',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]


#_____________\ RSM /_______________

def clear_console():
    # Clear console based on the operating system
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux/Mac

def findTrueLetter(texte, delimiteur=':', commencer_par_pair=True):
    pattern = re.escape(delimiteur) + r'(.*?)' + re.escape(delimiteur)
    tous = re.findall(pattern, texte)
    # Garder un sur deux, à partir de l'index pair (0) ou impair (1)
    depart = 0 if commencer_par_pair else 1
    return [val for i, val in enumerate(tous) if i % 2 == depart]

    
def findTrueX1X2(text):
    return re.findall(r'_(.*?)_', text)    

def getRank(letter):
    R=full_alphabet.index (letter)
    return R

def encode(text): 
    translated = ''
    key= ''
    for symbol in text:
        Rank=getRank(symbol)
        x1=secrets.randbelow(100000000)
        x2=random.randint((Rank+x1),1000000000000)
        k=secrets.randbelow(1000000000)
        n=secrets.randbelow(100000000000)
        translated += (sep[0]+(str(((Rank+x1)+(x2*k))))+sep[0]+sep[0]+str(n)+sep[0])
        key += (sep[1]+str(x2)+sep[1]+sep[1]+str(x1)+sep[1])
        tork=[translated, key]
    return tork 

def decode (text,key):
    translated = ''
    letters = findTrueLetter(text, delimiteur=':')
    x1x2 = findTrueX1X2(key)
    for i in range(0, len(letters)):
        ix1=i*2
        ix2=2*i+1
        letter = letters[i]
        x2 = x1x2[ix1] 
        C = int(letter) % int(x2)
        R = C -(int(x1x2[ix2]))
        Trueletter = full_alphabet[R]
        translated += Trueletter
    return translated   

#_____________\ CCSU /_______________

def getMode():
    while True:
        print(Fore.RED+'\nDo you wish encrypt or decrypt your text\n'+Fore.GREEN)
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print(Fore.RED+'\nEnter "encrypt" or "e" ou "decrypt" or "d".\n'+Fore.GREEN)

def getMessage():
    print(Fore.RED+'\n Enter your text: \n'+Fore.GREEN)
    return input()

def getKey():
    key = 0
    while True:
        print(Fore.RED+'\nEnter the key (1-%s)\n' % (MAX_KEY_SIZE)+Fore.GREEN)
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def chiffrer(message, key):    
    #if mode[0] == 'd':
    #    key = -key
    translated = ''

    for symbol in message:
        symbolran = SYMBOLS[random.randint (0,len(SYMBOLS))]
        symbolIndex = SYMBOLS.find(symbol)
        translated += symbolran
        if symbolIndex == -1: 
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated

def déchiffrer (message, key):
    translated = ''
    vraielettre = False
    for symbol in message:    
        symbolIndex = SYMBOLS.find(symbol)
        if vraielettre:
            if symbolIndex == -1: 
                translated += symbol
            else:
                symbolIndex -= key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            
            translated += SYMBOLS[symbolIndex]
        vraielettre = not vraielettre
            
    return translated

#_____________\ SSS /_______________

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

def getPoints_v2():
    print(Fore.RED+"Enter the points one for each line, with form (x,y) then an empty line to validate: \n \n"+Fore.GREEN)
    x_s = []
    y_s = []

    while True:
        ligne = input()
        if ligne.strip() == "":
            break  # fin de l'entrée
        ligne = ligne.strip().replace("(", "").replace(")", "")
        try:
            x_str, y_str = ligne.split(",")
            x = int(x_str)
            y = int(int(y_str) % 1596875498654165685896478585698569852589)
            x_s.append(x)
            y_s.append(y)
        except ValueError:
            print(f"Empty line ignored {ligne}")
            continue
        
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

def generatePointsverbose(n, k, a0):
    coefficients=[a0]
    print(Fore.WHITE+'generating truly random coefficients...')
    time.sleep(0.1)
    for i in range (k-1):
        negorposc=secrets.randbelow(2)
        if negorposc == 1:
            ai=secrets.randbelow(3000000000000)
            coefficients.append(ai)
        else:
            ai=secrets.randbelow(3000000000000)
            coefficients.append(int(-ai))
    print(Fore.WHITE+'generating polynomial...')
    time.sleep(0.1)
    X=symbols('x')
    poly=sum(a *X**i for i, a in enumerate(coefficients))
    print('f(x)='+str(poly))
    time.sleep(0.1)
    print('generating truly random values of x...')
    time.sleep(0.1)
    print('adding moduloes...\n ')
    time.sleep(0.3)
    print(Fore.RED+'Your points are : \n'+Fore.GREEN)
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
