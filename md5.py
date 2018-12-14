""" XD c'est mega chaud a implementer en vrai...
https://equi4.com/md5/
https://www.ietf.org/rfc/rfc1321.txt"""
import math
import binascii
import struct

r = []
k = [None]*64

r[0:16] = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22]
r[16:32] = [5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20]
r[32:48] = [4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23]
r[48:64] = [6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]


#MD5 utilise des sinus d'entiers pour ses constantes :
for i in range(0,64):
    k[i] = hex(math.floor(abs(math.sin(i + 1)) * 2**32))

#Les boucles principales
def F(b, c, d):
    return (b & c) | (~b & d)

def G(b, c, d):
    return (b & d) | (c & ~d)

def H(b, c, d):
    return b ^ c ^ d

def I(b, c, d):
    return c ^ (b | ~d)

def add_binaire(*args) :
    return bin(sum(int(x, 2) for x in args))



#Préparation du message (padding) :
def padding(message) :
    message = (bytearray(message.encode("utf-8")))
    lenByte = (8 * len(message))%64
    message.append(0x1)
    #Ajout de 0, jusqu'à ce que la taille du message en bits soit soit congruents 
    # à 448 étant donnée que nous sommes en bytes, 448/8 = 56
    while((len(message)*8)%512  != 448) :
        message.append(0x0)
    message.append(0x0)
    message.append(0x0)
    message.append(0x0)
    message.append(0x0)
    message.append(0x0)
    message.append(0x0)
    message.append(0x0)
    message.append(lenByte)
    return message

#decoupage du message en dans une liste, par bloc de 32 bits
def decoupageByte(message) :
    decoupe = []
    for i in range(0,len(message),4) :
        decoupe.append(hex(message[i]*(16**6) + message[i+1]*(16**4) + message[i+2]*(16**2) + message[i+3]))
    return decoupe

def operationF(a,b,c,d,x,s,i) :
    val = (a+F(b,c,d) + x + int(k[i-1],16))
    val = leftrotate(val, s)
    return b+val

def operationG(a,b,c,d,x,s,i) :
    val = (a+G(b,c,d) + x + int(k[i-1],16))
    val = leftrotate(val, s)
    return b+val

def operationH(a,b,c,d,x,s,i) :
    val = (a+H(b,c,d) + x + int(k[i-1],16))
    val = leftrotate(val, s)
    return b+val

def operationI(a,b,c,d,x,s,i) :
    val = (a+I(b,c,d) + x + int(k[i-1],16))
    val = leftrotate(val, s)
    return b+val

#Retourne x avec n bits déplacer vers la gauche 
def leftrotate(x, c) :
    return (x<<c) | (x<<(32-c))

def toLittleIndian(liste) :
    little = list()
    for i in range(len(liste)):
        chaine = ''
        liste[i] = liste[i][2:]
        for j in range(len(liste[i]),0,-2):
            chaine+=liste[i][j-2]
            chaine+=liste[i][j-1]
        little.append(int(chaine,16))
    return little

#print(left_rotate(hex("Bonjour"), 3))
def md5Hash(message) :
    message = padding(message)
    messageDecoupe = decoupageByte(message)
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    AA = a
    BB = b
    CC = c
    DD = d

    for j in range(0,len(messageDecoupe),16) :
        #Calcul avec F
        a = operationF(a,b,c,d,int(messageDecoupe[j],16),r[0], 1)
        d = operationF(d,a,b,c,int(messageDecoupe[j+1],16),r[1], 2)
        c = operationF(c,d,b,a,int(messageDecoupe[j+2],16),r[2], 3)
        b = operationF(b,c,d,a,int(messageDecoupe[j+3],16),r[3], 4)
        a = operationF(a,b,c,d,int(messageDecoupe[j+4],16),r[4], 5)
        d = operationF(d,a,b,c,int(messageDecoupe[j+5],16),r[5], 6)
        c = operationF(c,d,b,a,int(messageDecoupe[j+6],16),r[6], 7)
        b = operationF(b,c,d,a,int(messageDecoupe[j+7],16),r[7], 8)
        a = operationF(a,b,c,d,int(messageDecoupe[j+8],16),r[8], 9)
        d = operationF(d,a,b,c,int(messageDecoupe[j+9],16),r[9], 10)
        c = operationF(c,d,b,a,int(messageDecoupe[j+10],16),r[10], 11)
        b = operationF(b,c,d,a,int(messageDecoupe[j+11],16),r[11], 12)
        a = operationF(a,b,c,d,int(messageDecoupe[j+12],16),r[12], 13)
        d = operationF(d,a,b,c,int(messageDecoupe[j+13],16),r[13], 14)
        c = operationF(c,d,b,a,int(messageDecoupe[j+14],16),r[14], 15)
        b = operationF(b,c,d,a,int(messageDecoupe[j+15],16),r[15], 16)
        #Calcul avec G
        a = operationG(a,b,c,d,int(messageDecoupe[j],16),r[16], 17)
        d = operationG(d,a,b,c,int(messageDecoupe[j+1],16),r[17], 18)
        c = operationG(c,d,b,a,int(messageDecoupe[j+2],16),r[18], 19)
        b = operationG(b,c,d,a,int(messageDecoupe[j+3],16),r[19], 20)
        a = operationG(a,b,c,d,int(messageDecoupe[j+4],16),r[20], 21)
        d = operationG(d,a,b,c,int(messageDecoupe[j+5],16),r[21], 22)
        c = operationG(c,d,b,a,int(messageDecoupe[j+6],16),r[22], 23)
        b = operationG(b,c,d,a,int(messageDecoupe[j+7],16),r[23], 24)
        a = operationG(a,b,c,d,int(messageDecoupe[j+8],16),r[24], 25)
        d = operationG(d,a,b,c,int(messageDecoupe[j+9],16),r[25], 26)
        c = operationG(c,d,b,a,int(messageDecoupe[j+10],16),r[26], 27)
        b = operationG(b,c,d,a,int(messageDecoupe[j+11],16),r[27], 28)
        a = operationG(a,b,c,d,int(messageDecoupe[j+12],16),r[28], 29)
        d = operationG(d,a,b,c,int(messageDecoupe[j+13],16),r[29], 30)
        c = operationG(c,d,b,a,int(messageDecoupe[j+14],16),r[30], 31)
        b = operationG(b,c,d,a,int(messageDecoupe[j+15],16),r[31], 32)
        #Calcul avec H
        a = operationH(a,b,c,d,int(messageDecoupe[j],16),r[32], 33)
        d = operationH(d,a,b,c,int(messageDecoupe[j+1],16),r[33], 34)
        c = operationH(c,d,b,a,int(messageDecoupe[j+2],16),r[34], 35)
        b = operationH(b,c,d,a,int(messageDecoupe[j+3],16),r[35], 36)
        a = operationH(a,b,c,d,int(messageDecoupe[j+4],16),r[36], 37)
        d = operationH(d,a,b,c,int(messageDecoupe[j+5],16),r[37], 38)
        c = operationH(c,d,b,a,int(messageDecoupe[j+6],16),r[38], 39)
        b = operationH(b,c,d,a,int(messageDecoupe[j+7],16),r[39], 40)
        a = operationH(a,b,c,d,int(messageDecoupe[j+8],16),r[40], 41)
        d = operationH(d,a,b,c,int(messageDecoupe[j+9],16),r[41], 42)
        c = operationH(c,d,b,a,int(messageDecoupe[j+10],16),r[42], 43)
        b = operationH(b,c,d,a,int(messageDecoupe[j+11],16),r[43], 44)
        a = operationH(a,b,c,d,int(messageDecoupe[j+12],16),r[44], 45)
        d = operationH(d,a,b,c,int(messageDecoupe[j+13],16),r[45], 46)
        c = operationH(c,d,b,a,int(messageDecoupe[j+14],16),r[46], 47)
        b = operationH(b,c,d,a,int(messageDecoupe[j+15],16),r[47], 48)
        #Calcul avec I
        a = operationI(a,b,c,d,int(messageDecoupe[j],16),r[48], 49)
        d = operationI(d,a,b,c,int(messageDecoupe[j+1],16),r[49], 50)
        c = operationI(c,d,b,a,int(messageDecoupe[j+2],16),r[50], 51)
        b = operationI(b,c,d,a,int(messageDecoupe[j+3],16),r[51], 52)
        a = operationI(a,b,c,d,int(messageDecoupe[j+4],16),r[52], 53)
        d = operationI(d,a,b,c,int(messageDecoupe[j+5],16),r[53], 54)
        c = operationI(c,d,b,a,int(messageDecoupe[j+6],16),r[54], 55)
        b = operationI(b,c,d,a,int(messageDecoupe[j+7],16),r[55], 56)
        a = operationI(a,b,c,d,int(messageDecoupe[j+8],16),r[56], 57)
        d = operationI(d,a,b,c,int(messageDecoupe[j+9],16),r[57], 58)
        c = operationI(c,d,b,a,int(messageDecoupe[j+10],16),r[58], 59)
        b = operationI(b,c,d,a,int(messageDecoupe[j+11],16),r[59], 60)
        a = operationI(a,b,c,d,int(messageDecoupe[j+12],16),r[60], 61)
        d = operationI(d,a,b,c,int(messageDecoupe[j+13],16),r[61], 62)
        c = operationI(c,d,b,a,int(messageDecoupe[j+14],16),r[62], 63)
        b = operationI(b,c,d,a,int(messageDecoupe[j+15],16),r[63], 64)
    a = AA + a
    b = BB + b
    c = CC + c
    d = DD + d
    chaine = [None]*4
    chaine[0] = hex(a)
    chaine[1] = (hex(b))
    chaine[2] = (hex(c))
    chaine[3] = (hex(d))
    return chaine


def md5Wiki(message) :
    message = padding(message)
    m = decoupageByte(message)
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    AA = a
    BB = b
    CC = c
    DD = d
    f = 0 
    g = 0
    w = toLittleIndian(m)
    for j in range(0,64) :
        #Calcul avec F
        if 0<= j < 16 :
            f = F(b,c,d)
            g = j
        if 16<= j < 32 :
            f = G(b,c,d)
            g = (5*j + 1)%16 
        if 32<= j <= 48 :
            f = H(b,c,d)
            g =  (3*j + 5)%16       
        if 48<= j <64 :
            f = I(b,c,d)
            g = (7*j) % 16
        temp = d 
        d = c
        c = b
        b = leftrotate((f + a + int(k[j],16) + w[g]), r[j])
        a = temp
    AA = AA + a
    BB = BB + b
    CC = CC + c
    DD = DD + d
    chaine = [None]*4
    chaine[0] = hex(AA)
    chaine[1] = (hex(BB))
    chaine[2] = (hex(CC))
    chaine[3] = (hex(DD))
    return chaine

test = padding("coucou")
decoupetest = decoupageByte(test)
print(decoupetest)
littleIn = toLittleIndian(decoupetest)
for i in range(len(decoupetest)) :
    print(littleIn[i])

motwiki = (md5Wiki(""))
print(motwiki)