import patricia as pat
import arquivos as arq
import pickle
import operacoes as op
import datasci as ds
import pandas as pd

arq.inicializaFromKaggle()

busca = arq.join(arq.root,'patricia.bin')

df = arq.abreLeitura()
    
arv = pat.criaArvoreFromDF(df)
    
#x = arv.buscaPorString('the la')[0][1].indice
#op.exibeInfoMusica(x)

pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)     # Display all rows
pd.set_option('display.width', None)

print(df[df['album']=="evermore"])

#ds.graficoBarrasAlbum('folklore')

#x = [y[1].titulo for y in arv.buscaPorString('the')]
#print(x)