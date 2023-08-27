import patricia as pat
import arquivos as arq
import pickle
import operacoes as op
import datasci as ds

#arq.inicializaFromKaggle()

busca = arq.join(arq.root,'patricia.bin')

df = arq.abreLeitura()
    
arv = pat.criaArvoreFromDF(df)
    
"""x = arv.buscaPorString('deli')[0][1].indice
op.exibeInfoMusica(x)"""

ds.graficoBarrasAlbum('reputation')

#x = [y[1].titulo for y in arv.buscaPorString('the')]
#print(x)