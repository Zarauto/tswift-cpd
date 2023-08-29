import math

_xormap = {('0','1'):'1', ('1','0'):'1', ('1','1'):'0', ('0','0'):'0'}
def xor(x, y):
    return ''.join([_xormap[a,b] for a,b in zip(x,y)])

def str_to_value(string):
    string = str(string)
    #print(string, '&')
    resultado = '000000000000'
    i = 0
    for c in string:
        b = bin(ord(c))[2:]
        for _ in range(i%8):
            b = b[1:] + b[0] # Rotaciona os bits
        resultado = xor(resultado, f"0000{b}")
        i+=1

    return int(resultado, 2)

class Termo():
    def __init__(self, palavra, freq):
        self.palavra = palavra
        self.freq = freq

    def __lt__(self, b):
        if self.freq != b.freq:
            return self.freq > b.freq 
        return self.palavra < b.palavra


class Hash():
    def __init__(self, size):
        self.dicionario = [-1] * size
        self.size = size
        self.conteudo   = [None] * size
        self.used       = [False] * size

    def f1(self, c):
        return str_to_value(c)%self.size
    
    def f2(self, c):
        return str_to_value(c)%(int(self.size**(2/3)))
    
    def atualiza(self, termo):
        j = 1
        i = self.f1(termo)
        #print(termo)

        while self.used[i] and self.dicionario[i] != termo:
            i = (self.f1(termo)+ j*self.f2(termo) + j)%self.size
            #print(i)
            j+=1

        if not self.used[i]:
            self.used[i] = True
            self.dicionario[i] = termo
            self.conteudo[i] = 1
            return
        
        self.conteudo[i] += 1
        return
    
    def print(self):
        for i in range(self.size):
            print(f"{i} | {self.dicionario[i]} | {self.conteudo[i]} | {self.used[i]}")

    def to_list(self):
        lista = []

        for i in range(self.size):
            if not self.used[i]:
                continue

            #print(i)
            lista.append(Termo(self.dicionario[i],self.conteudo[i]))

        return lista
    
def printFreq(lista):
    for t in lista:
        print(f"{t.palavra} | {t.freq}")