import pickle

class nodoPatricia:
    def __init__(self, casa, chave):
        self.casa = casa # Posição da string a ser olhada para comparação
        self.chave = chave # Letras em comum das chaves até a posição 'casa'
        self.folhas = []
        self.filhos = []
        
    def sortFilhos(self):
        for i in range(1,len(self.filhos)):
            if self.filhos[i][0] > self.filhos[i-1][0]:
                continue

            j = i
            while(self.filhos[j-1][0] > self.filhos[i][0]):
                j -= 1

            x = self.filhos[i]
            self.filhos.pop(i)
            self.filhos.insert(j,x)
        

    def insereFolha(self, folha):
        self.folhas.append((folha.chave[self.casa], folha))
        
    def retornaFolhas(self, entrada):  # sourcery skip: de-morgan
        # Se a entrada não compartilhar o prefixo do nodo
        #print(self.chave, entrada)
        if not (self.chave == entrada[:self.casa] or entrada == self.chave[:len(entrada)]):
            return []
        
        results = []
        if len(self.folhas) > 0:
            #print(self.folhas)
            results.extend(self.folhas)
            
        for f in self.filhos:
            results.extend(f[1].retornaFolhas(entrada))
            
        return results

class folhaPatricia:
    def __init__(self, titulo, indice):
        # No futuro, eliminar elemento titulo
        self.titulo = titulo
        self.chave = self.criaChave(titulo)
        self.indice = indice

    def criaChave(self, titulo):
        # No futuro, tratar from the vault e taylors version

        # Remove pontuação
        chave = ''.join(c for c in titulo if c.isalpha() or c.isspace() or c.isdigit())

        # Torna minúsculo
        return f"{str.lower(chave)}-" # Traço adicionado para caso de um título ser prefixo de outro

class PATRICIA:
    def __init__(self):
        self.filhos_raiz = []
        self.num_nodos = 0

    def inserePrimeiraFolha(self, folha):
        c = folha.chave[0]
        nodo = nodoPatricia(len(folha.chave)-1, folha.chave[:-1])
        self.filhos_raiz.append([c, nodo])
        nodo.insereFolha(folha)
        

    def tentaInserirFolha(self, nodo, folha):  # sourcery skip: extract-method

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
                    filho[1] = self.tentaInserirFolha(filho[1], folha)
                    nodo.sortFilhos()
                    return nodo
            
            # Senão, adiciona filho que será pai da folha
            filho = nodoPatricia(len(folha.chave)-1, folha.chave[:-1])
            filho = self.tentaInserirFolha(filho, folha)
            nodo.filhos.append([folha.chave[nodo.casa], filho])     
            nodo.sortFilhos()           
        
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
        
        
    def buscaPorString(self, entrada):
        entrada = entrada.lower()
        entrada = ''.join(c for c in entrada if c.isalpha() or c.isspace() or c.isdigit())
        prim_char = entrada[0]
        
        for f in self.filhos_raiz:
            if prim_char == f[0]:
                results = f[1].retornaFolhas(entrada)
                break
            
        return results
    
    def listaTodas(self):
        retorno = []
        for x in self.filhos_raiz:
            retorno.extend(self.buscaPorString(x[0]))
            
        return retorno
    
def criaArvoreFromDF(df):
    arv = PATRICIA()

    for i, row in df.iterrows():
        indice = row['id']
        titulo = row['name']
        folha = folhaPatricia(titulo, indice)
        arv.insereFolha(folha)
        
    return arv