import patricia as pat
import arquivos as arq
import pickle

#arq.inicializaFromKaggle()

dados = arq.tgt_name
busca = arq.join(arq.root,'patricia.bin')

with open (dados, 'rb') as src:
    df = pickle.load(src)
    
arv = pat.criaArvoreFromDF(df)
    
print([x[0] for x in arv.filhos_raiz])
pat.salvaArvore(arv, busca)
