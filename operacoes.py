import patricia as pat
import arquivos as arq
import pandas as pd
import pickle
import matplotlib.pyplot as plt

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
    print(f"\nLetra:\n{arq.getLetra(df['letra_ini'].to_list()[0],df['letra_len'].to_list()[0])}")
    print("----------------------------\n")
    
def graficoBarrasAlbum(album):
    df = arq.abreLeitura()
    df = df[df['album'] == album]
    #df = df[df['name', 'views']]
    
    plt.bar(df['name'],df['views'])
    plt.xlabel('Músicas')
    plt.ylabel('Views')
    plt.title(f'Comparação de views no YouTube das músicas do álbum "{album}"')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def graficoBarrasTema(tema):
    df = arq.abreLeitura()
    df = df[df['tematica'] == tema]
    #df = df[df['name', 'views']]
    
    plt.bar(df['name'],df['views'])
    plt.xlabel('Músicas')
    plt.ylabel('Views')
    plt.title(f'Comparação de views no YouTube das músicas de temática "{tema}"')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def graficoBarrasTodas(decrescente):
    df = arq.abreLeitura()
    df = df.sort_values(by='views', ascending=not decrescente)
    
    plt.bar(df['name'],df['views'])
    plt.xlabel('Músicas')
    plt.ylabel('Views')
    plt.title('Comparação de views no YouTube de todas as músicas')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()
    plt.show()