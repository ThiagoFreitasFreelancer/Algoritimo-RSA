import os
import random
from typing import List
# path='C:/Users'
# path=os.path.realpath(path)
# aquivo = os.startfile(path)

# print(aquivo)

alphabet = {
    'A': 65,'B': 66,'C': 67,
    'D': 68,'E': 69,'F': 70,
    'G': 71,'H': 72,'I': 73,
    'J': 74,'K': 75,'L': 76,
    'M': 77,'N': 78,'O': 79,
    'P': 80,'Q': 81,'R': 82,
    'S': 83,'T': 84,'U': 85,
    'V': 86,'W': 87,'X': 88,
    'Y': 89,'Z': 90,'a': 97,
    'b': 98,'c': 99,'d': 100,
    'e': 101,'f': 102,'g': 103,
    'h': 104,'i': 105,'j': 106,
    'k': 107,'l': 108,'m': 109,
    'n': 110,'o': 111,'p': 112,
    'q': 113,'r': 114,'s': 115,
    't': 116,'u': 117,'v': 118,
    'w': 119,'x': 120,'y': 121,
    'z': 122, " ": 123
}

numberletter = {
    65: 'A',66: 'B',67: 'C',
    68: 'D',69: 'E',70: 'F',
    71: 'G',72: 'H',73: 'I',
    74: 'J',75: 'K',76: 'L',
    77: 'M',78: 'N',79: 'O',
    80: 'P',81: 'Q',82: 'R',
    83: 'S',84: 'T',85: 'U',
    86: 'V',87: 'W',88: 'X',
    89: 'Y',90: 'Z',97: 'a',
    98: 'b',99: 'c',100: 'd',
    101: 'e',102: 'f',103: 'g',
    104: 'h',105: 'i',106: 'j',
    107: 'k',108: 'l',109: 'm',
    110: 'n',111: 'o',112: 'p',
    113: 'q',114: 'r',115: 's',
    116: 't',117: 'u',118: 'v',
    119: 'w',120: 'x',121: 'y',
    122: 'z',123: ' '
}

def LetterToInt(strings: str):

    encryp = []
    for vet in strings:
        encryp.append(alphabet[vet])
    return encryp

def GetPrime():
    res = True
    n = int(random.uniform(2, 200))
    for val in range(2,n):
        if n % val != 1:
            res = False
            break
    if res:
        GetPrime()

    print("Primo: ", n)
    return n

def Mdc(a: int, b: int):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return Mdc(a, b)

def GetIntPi(piForN: int):
    return int(random.uniform(2, piForN))

def GetInt(n):
    return random.random() * n

def MultPrime():
    primeVet = []
    primeVet.append(GetPrime())
    primeVet.append(GetPrime())
    mult = primeVet[0] * primeVet[1]
    primeVet.append(mult)

    return primeVet

def GetNumberKey(prime1: int, prime2: int, n: int):

    piN = (prime1 - 1) * (prime2 - 1)

    mdcNandOne = 0
    numberKeyOne = 0
    numberKeyTwo = 0
    isOne = 0
    aux = 10

    print("piN: ", piN)

    while(mdcNandOne != 1):
        numberKeyOne = GetIntPi(piN)
        mdcNandOne = Mdc(numberKeyOne, n)
    
    print('numberKeyOne: ', numberKeyOne)

    while(isOne != 1):
        numberKeyTwo = GetIntPi(piN)
        isOne = ((numberKeyOne * numberKeyTwo) % n)
        #aux = aux + 1

    print('numberKeyTwo: ', numberKeyTwo)

    keys = [numberKeyOne, numberKeyTwo, piN, n]

    return keys

def Encryption(mensageForEncryption):

    multPrime = MultPrime()
    IntKey = GetNumberKey(multPrime[0], multPrime[1], multPrime[2])
    mensageEncryptionOneFase = LetterToInt(mensageForEncryption)

    fileOfEncryption = open("FileIncryption.txt", "w")
    fileOfEncryption.write("n:" + str(IntKey[3]) + "\n" +  "e:" + str(IntKey[0]) + "\n")

    privateKey = open("privateKey.txt", "w")
    key = str(IntKey[1])
    privateKey.write(key)
    privateKey.close()

    for n in mensageEncryptionOneFase:
        fileOfEncryption.write(str((n**IntKey[0]) % IntKey[3]) + '\n')
    print(mensageEncryptionOneFase)
    fileOfEncryption.close()

def Decryption(FileIncryption: str, FileKey):

    lista = []
    lits = []
    aux = 0
    with open(FileIncryption, 'r') as e:
        fileIncryption = open(FileIncryption, 'r')

    with open(FileKey, 'r') as f:
        key = open(FileKey, 'r')
        key = int(key.readline())

    for x in fileIncryption:
        lits.append(x)

    mod = ''.join(lits[0].split())
    mod = int(mod[2:])

    print(lits)

    for x in lits[2:]:
        aux = ''.join(x.split())
        lor = int(aux)
        var = (lor**key) % mod            
        print('var: ',var)
        if((var >= 2 and var <= 90) or (var >= 97 and var <= 123)):
            lista.append(numberletter[var])

    print(lista)

def init():
    print("Select Options")
    option = int(input("Encryption 0 or Decryption 1: "))
    if( option == 0 or option == 1 ):
        if(option == 1):
            file = input("Digite o nome do arquivo txt sem a extensão final: ")
            key = input("Digite o nome do arquivo txt da chave: ")
            Decryption(file, key)
        else:
            mensage = input("Digite sua mensagem :")
            Encryption(mensage)
            print("Um arquivo chamado FileIncryption.txt ira ser criado na pasta do aquivo com a chave publica")
            print("Outro arquivo chamado privateKey.txt ira ser criado na pasta com a chave privada")
    else:
        print("Valor incorreto")
        init()

init()