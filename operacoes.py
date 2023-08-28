import patricia as pat
import arquivos as arq
import pandas as pd
import pickle

def adicionaMusica(titulo, album, duracao, url, tematica, arq_letra):
    pass

def exibeInfoMusica(num):
    df = arq.abreLeitura()
    df = df[df['id']==num]
    a = df['album'].to_list()[0]
    #print(a)
    
    with open(arq.lista_albums, 'rb') as f:
        la = pickle.load(f)
        
        la = la.reset_index(drop=True)
        data = la[la['album']==a]
        data = data['release_date'].to_list()[0]
        #print(data)
    del la
    
    print("----------------------------")
    print(df['name'].to_list()[0])
    print(f"Álbum: {a}")
    print(f"Data de lançamento: {data}")
    print(f"Temática: {df['tematica'].to_list()[0]}")
    print(f"Views no YouTube: {df['views'].to_list()[0]}")
    #print(f"\nLetra:\n{arq.getLetra(df['letra_ini'].to_list()[0],df['letra_len'].to_list()[0])}")
    print(f"{df['letra_ini'].to_list()[0],df['letra_len'].to_list()[0]}")
    
