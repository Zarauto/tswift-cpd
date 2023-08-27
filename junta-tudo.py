import patricia as pat
import arquivos as arq
import pickle

a = pat.PATRICIA()

with open('.\\rep.bin', 'rb') as f:
    rep = pickle.load(f)
    
for i, row in rep.iterrows():
    song_id = row['id']
    song_title = row['name']
    folha = pat.folhaPatricia(song_title, song_id)
    a.insereFolha(folha)
    
print(a.filhos_raiz)