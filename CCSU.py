# Cryptage 
import random, time
SYMBOLS = 'AՒՔաբդեէըթժضЙصЦثBقУفК غC3-ሀለሐመعЕğアカサタナハマهςε567ᚱሠረሰሸᚹᚻ890\'ρ\"τЁ:;,.?!ゾドボポخDᚠᚨᛃحНجቀበቨተቸኀነûŭůυθιοù/úüūヤラワガザダバűիᚺųኘአከπασ^δφụᛗᛜᚲՋГኸወዐዘዠየደጀገጨጠጰጸፈፀፐشEسШγηသパイキシチニヒξκيЩᛟᛉ1بFԲԳԵلЗဆတနမအပကミリヰギジヂビငا2Хت4GنФمЫكHطВАذλζχψωβμIᛜᛏПءόРJؤОىЛώピウクスツヌフئKДЖوLЭàᛚᛝâáãЯMźظЧСNМစရေ်ျးယဖထИOИТPЬЪQБЮRSTUVWXYZaйцခလဘညာbуžéᛇᛒᚾèêëкムユルグズヅブcеēėęðěёdнгĕəẹeшщfзхgņňŋṅķƙфыŕプエケセテネヘřẁẃhвㅂㅈㄷㄱŵẅаɓñńiпשçԷԹԻԽԿՀՁՂՃՌՍՎՏՐՑćメレヱゲゼデベĉčדגכроĵĥоעיחלß§śŝšṣşףזסлjджkэяlペオコソトノホקч쇼ㅕㅑㅐㅔㅁㄴㅇㄹ호ㅓㅏㅣㅋㅌㅊ퓨ㅜㅡсmרмאḍɗטиוןםפ月了嘛起来nтьoъpĺľļł·бюqrstuvÿýỳŷƴwțţxṭįīïîìíị来说你好ıyþťzôœòó呀モヨロヲンゴ美啊õöøōőήọºΕΡΤΥΘΙΟΠ走路ΑΣΔΦΓΗΞ法ΚΛΖΧΨΩΒΝΜ'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Vous souhaitez crypter ou décrypter votre message?')
        mode = input().lower()
        if mode in ['crypter', 'c', 'décrypter', 'd']:
            return mode
        else:
            print('Entrez "crypter" ou "c" ou "décrypter" ou "d".')

def getMessage():
    print('Entrez votre message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Entrez la clé (1-%s)' % (MAX_KEY_SIZE))
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
    


mode = getMode()
message = getMessage()
key = getKey()
print('Votre texte traduit est:')
if mode[0] == 'c':
    code = chiffrer(message,key)
    print(code)
    decode = déchiffrer(code,key)
    if decode == message:
        time.sleep(1)
        print ('Le chiffrement est un succès')
    else:
        print ('Échec de chiffrement')
        print (decode)
if mode[0] == 'd':
    code = déchiffrer(message, key)
    print(code)
        