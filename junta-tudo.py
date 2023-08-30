import patricia as pat
import arquivos as arq
import pickle
import operacoes as op
import datasci as ds
import pandas as pd
import hash
import menu

#arq.inicializaFromKaggle()

df = arq.abreLeitura()
    
#arv = pat.criaArvoreFromDF(df)
    


pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)     # Display all rows
pd.set_option('display.width', None)

#print(df)
#arq.abreHash().print()

#print(df[df['album']=="Midnights"])

#ds.graficoBarrasAlbum('folklore')

"""x = [y[1].titulo for y in arv.buscaPorString('ou')]
print(x)"""




"""t = hash.Termo('man', 1)
s = hash.Termo('love',1)


h = hash.Hash(13)

h.atualiza('man')
h.atualiza('love')
h.atualiza('man')

print([[j.palavra, j.freq] for j in h.to_list()])"""

"""h = hash.Hash(307)

arq.salvaHash(h)


g, k = 1089633, 2031
i, j = 1093426, 2088
arq.adicionaFrequenciaPalavras(g, k)
arq.adicionaFrequenciaPalavras(i, j)

h = arq.abreHash()
h.print()"""

"""x = arv.buscaPorString('read')[0][1].indice
op.exibeInfoMusica(x)"""

"""l = h.to_list()
l.sort()

print([[x.palavra, x.freq] for x in l])"""

#ds.graficoBarrasAlbum('reputation')

#arq.inicializaFromKaggle()

#h = arq.abreHash()
#h.print()

#l = arq.abreFreq()

"""for i in range(35):
    print(l[i].palavra,l[i].freq)
#hash.printFreq(l)"""
#l = h.to_list()
#l.sort()

#for x in l:
#    print([[x.palavra, x.freq]])

menu.menuPrincipal()
    

#arq.adicionaFrequenciaPalavras(1089633, 2031)