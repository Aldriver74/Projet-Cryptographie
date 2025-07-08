import random
import re
import time
import secrets

full_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
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
                 'Ӹ', 'ӹ', 'Ӻ', 'ӻ', 'Ӽ', 'ӽ', 'Ӿ', 'ӿ','\'', ' ', 'ç', 'Ç', 'à', 'é', 'è', 'ê',
                 'ï', 'ë', 'ô', 'û', 'â', 'É', 'È', 'Ê', 'Ô', 'À', ',', '-', '.', '!', '?', ':',
                 ';']

sep = [':', '_']

def findTrueLetter(texte, delimiteur=':', commencer_par_pair=True):
    pattern = re.escape(delimiteur) + r'(.*?)' + re.escape(delimiteur)
    tous = re.findall(pattern, texte)
    # Garder un sur deux, à partir de l'index pair (0) ou impair (1)
    depart = 0 if commencer_par_pair else 1
    return [val for i, val in enumerate(tous) if i % 2 == depart]

    return re.findall(r':(.*?):', text)
    
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
        
print("Do you want to encode(e) or decode(d) your message")    
choice=input()  

if choice == "e":
    print("Enter your text:")
    X=input()
    result=encode(X)
    test=decode(result[0], result[1])
    if test == X :
        print ("\n Result: \n"+str(result[0])+':'+"\n \n Your key is:"+str(result[1])+'_')
    else: 
        print ("Something went wrong, retry")

if choice == "d":    
    print("\n Enter your crypted text:")
    ctext=input()
    print("\n Enter the password:")
    password=input()
    print ("\n Your decrypted text is: \n"+decode(ctext,password))

time.sleep(60)

    