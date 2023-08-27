import patricia as pat
import arquivos as arq
import pickle

"""a = pat.PATRICIA()

with open('.\\rep.bin', 'rb') as f:
    rep = pickle.load(f)
    
for i, row in rep.iterrows():
    song_id = row['id']
    song_title = row['name']
    folha = pat.folhaPatricia(song_title, song_id)
    a.insereFolha(folha)
    
with open(arq.letras_bin, 'wb') as f:
    a = pickle.dump(a,f)
    
with open(arq.letras_bin, 'rb') as f:
    b = pickle.load(f)
    
v = b.filhos_raiz[8][1].folhas[0][1].indice
print(b.filhos_raiz[8][1].folhas[0][1].indice)
i = v

x = rep.loc[rep['id'] == i]

print(x)"""

arq.inicializaFromKaggle()