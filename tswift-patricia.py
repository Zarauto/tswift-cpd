import string

class nodoPatricia:
    def __init__(self, casa, chave):
        self.casa = casa # Posição da string a ser olhada para comparação
        self.chave = chave # Letras em comum das chaves até a posição 'casa'
        self.folhas = []
        self.filhos = []

    def insereFolha(self, folha):
        self.folhas.append((folha.chave[self.casa], folha))

class folhaPatricia:
    def __init__(self, titulo, indice):
        # No futuro, eliminar elemento titulo
        self.titulo = titulo
        self.chave = self.criaChave(titulo)
        self.indice = indice

    def criaChave(self, titulo):
        # No futuro, tratar from the vault e taylors version

        # Remove pontuação
        chave =  titulo.translate(str.maketrans('', '', string.punctuation))

        # Torna minúsculo
        chave = str.lower(chave)+'-' # Traço adicionado para caso de um título ser prefixo de outro
        return chave

class PATRICIA:
    def __init__(self):
        self.filhos_raiz = []
        self.num_nodos = 0

    def inserePrimeiraFolha(self, folha):
        c = folha.chave[0]
        nodo = nodoPatricia(len(folha.chave)-1, folha.chave[:len(folha.chave)-1])
        self.filhos_raiz.append([c, nodo])
        nodo.insereFolha(folha)
        

    def tentaInserirFolha(self, nodo, folha):

        # Se compartilhar o prefixo armazenado pelo nodo
        if nodo.chave == folha.chave[:nodo.casa]:
            # Se a chave corresponder ao prefixo do nodo, insere como folha do nodo
            if folha.chave[:-1] == nodo.chave:
                nodo.insereFolha(folha)
                return nodo

            # Caso contrário
            # Verifica se a folha será descendente de algum filho do nodo
            for filho in nodo.filhos:
                if filho[0] == folha.chave[nodo.casa]:
                    # Se será, então segue a linha de descendência
                    filho[0] = self.tentaInserirFolha(filho[0], folha)
            
            # Senão, adiciona filho que será pai da folha
            else:
                filho = nodoPatricia(len(folha.chave)-1, folha.chave[:len(folha.chave)-1])
                filho = self.tentaInserirFolha(filho, folha)
                nodo.filhos.append([folha.chave[nodo.casa], filho])                
        
            return nodo


        # Senão, cria um pai com um prefixo comum ao nodo e à folha
        for i in range(nodo.casa-1, 0, -1):
            pref = nodo.chave[:i]
            if pref == folha.chave[:i]:
                break

        pai = nodoPatricia(i, pref)
        pai.filhos.append([nodo.chave[i],nodo])
        pai = self.tentaInserirFolha(pai, folha)

        return pai

    def sortRaiz(self):
        for i in range(1,len(self.filhos_raiz)):
            if self.filhos_raiz[i][0] > self.filhos_raiz[i-1][0]:
                continue

            j = i
            while(self.filhos_raiz[j-1][0] > self.filhos_raiz[i][0]):
                j -= 1

            x = self.filhos_raiz[i]
            self.filhos_raiz.pop(i)
            self.filhos_raiz.insert(j,x)

    def insereFolha(self, folha):
        self.num_nodos+=1
        c = folha.chave[0]

        # Se já existe nodo associado à primeira letra da chave
        for f in self.filhos_raiz:
            if f[0] == c:
                f[1] = self.tentaInserirFolha(f[1], folha)
                self.sortRaiz()
                return

        # Senão, cria este nodo 
        self.inserePrimeiraFolha(folha)
        self.sortRaiz()

def salvaArvore(arvore, diretorio):
    with open(diretorio, 'wb') as arq:
        pickle.dump(pat,arq)

def abreArvore(diretorio):
    with open(diretorio, 'rb') as arq:
        return pickle.load(arq)