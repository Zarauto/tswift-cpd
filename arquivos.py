import hash
import pandas as pd
import pickle
from os.path import join
from googleapiclient.discovery import build
import re

# Define endereços de arquivo
root = join('.','')
src_name = join(root,'taylor_swift_spotify.csv')
tgt_name = join(root,'dados.bin')
dir_letras = join(root,'letras')
dir_links = join(root,'urls')
letras_bin = join(root,'letras.bin')
lista_albums = join(root,'albuns.bin')
freq_palavras = join(root,'freq_letras.bin')
hash_bin = join(root,'hash.bin')

API_KEY = 'AIzaSyCpvKDb0XAjR2Jgq-7FsOo36UNfEUqpFM8'

def getLyricsAux(df, path):
    print(path)
    with open(path, 'r') as src:
        content = src.read()
        lista = content.split('@')
        
    nomes = [lista[i][1:] for i in range(len(lista)) if i%2 == 0]
    letras = [lista[i][1:] for i in range(len(lista)) if i%2 == 1]
    if(len(nomes)>len(letras)):
        nomes.pop(-1)
        
    with open(letras_bin, 'ab') as bf:
        
        for i in range(len(nomes)):
            letra_bin = letras[i].encode()

            print(nomes[i])
            
            ini = bf.tell()
            bf.write(letra_bin)
            length = len(letra_bin)
            
            df.loc[df['name'] == nomes[i], 'letra_ini'] = ini
            df.loc[df['name'] == nomes[i], 'letra_len'] = length

            adicionaFrequenciaPalavras(ini,length)

def getLyrics(df):
    albums = set(df['album'].tolist())
    
    for a in albums:
        getLyricsAux(df, join(dir_letras,f'{a}.txt'))

def getViewsFromYT(url):
    video_id_match = re.search(r'(?<=v=)[^&#]+', url)
    video_id_match = video_id_match or re.search(r'(?<=be/)[^&#]+', url)
    video_id = video_id_match.group(0) if video_id_match else None

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(part='statistics', id=video_id)
    response = request.execute()
    return int(response['items'][0]['statistics']['viewCount'])

def getViews(df):
    for index, row in df.iterrows():
        #print(row['name'])
        url = row['url']
        if url is not None:
            df.at[index, 'views'] = getViewsFromYT(url)

def getLinksAux(df, path):
    with open(path, 'r') as t:
        for line in t:
            [name, link, mood] = line[:-1*(line[-1]=='\n')].split('#')
            df.loc[df['name'] == name, 'url'] = link
            df.loc[df['name'] == name, 'tematica'] = mood

def getLinksTematica(df):
    albuns = set(df['album'].tolist())
    
    for a in albuns:
        #print(a)
        getLinksAux(df, join(dir_links,f'{a}.txt'))

def inicializaFromKaggle():
    # Cria dataframe reduzido a partir do arquivo fonte
    df = pd.read_csv(src_name)

    df = df[['id','name','album','release_date','track_number']]

    for i in ['id','url', 'views', 'tematica', 'letra_ini', 'letra_len']:
        df[i] = None

    albums_validos = ["Speak Now (Taylor's Version)","Midnights (The Til Dawn Edition)","Red (Taylor's Version)","Fearless (Taylor's Version)","evermore (deluxe version)", "folklore (deluxe version)", "Lover", "reputation", "1989 (Deluxe)", "Red (Deluxe Edition)", "Speak Now (Deluxe Package)", "Fearless (Platinum Edition)", "Taylor Swift"]

    df = df[df['album'].isin(albums_validos)]

    # Reduz nome de álbuns com versões especiais
    df.loc[df['album'] == "Midnights (The Til Dawn Edition)", 'album'] = "Midnights"
    df.loc[df['album'] == "evermore (deluxe version)", 'album'] = "evermore"
    df.loc[df['album'] == "folklore (deluxe version)", 'album'] = "folklore"
    df.loc[df['album'] == "1989 (Deluxe)", 'album'] = "1989"
    df.loc[df['album'] == "Red (Deluxe Edition)", 'album'] = "Red"
    df.loc[df['album'] == "Speak Now (Deluxe Package)", 'album'] = "Speak Now"
    df.loc[df['album'] == "Fearless (Platinum Edition)", 'album'] = "Fearless"
    
    # Elimina faixas que não serão avaliadas
    df = df[~df['name'].str.endswith(" - Voice Memo")]
    df = df[~((df['album'] == "Speak Now") & (df['track_number'] >= 20))]
    df = df[~df['name'].str.endswith(" - Pop Version")]
    df = df[~df['name'].str.endswith(" - Original Demo Recording")]
    
    # Trata títulos
    df['name'] = df['name'].str.replace(" - bonus track$", "", regex=True)
    df['name'] = df['name'].str.replace(" \(From The Vault\)$", "", regex=True)
    df['name'] = df['name'].str.replace(" - POP Mix$", "", regex=True)
    df['name'] = df['name'].str.replace(" - Radio Single Remix$", "", regex=True)
    df['name'] = df['name'].str.replace("Trouble.$", "Trouble", regex=True)
    
    # Cria um arquivo armazenando os títulos dos álbums e suas datas de lançamento
    # para eliminar esta informação repetida do arquivo principal
    df_albums = df[['album', 'release_date']].drop_duplicates()
    with open(lista_albums, 'wb') as la:
        pickle.dump(df_albums, la)
        
    df = df.drop('release_date', axis=1)
    

    open(freq_palavras,'wb')


    # Atribui ID a cada música
    df['id'] = list(range(1,len(df)+1))
    
    getLinksTematica(df)
    getViews(df)
    getLyrics(df)

    #Salva arquivo
    with open(tgt_name, 'wb') as arq:
        pickle.dump(df, arq)
        
# Retorna dataframe com os dados do arquivo principal para leitura
def abreLeitura():
    with open(tgt_name, 'rb') as f:
        return pickle.load(f)
    
    
# Retorna letra de uma música
def getLetra(ini, length):
    with open(letras_bin, 'rb') as f:
        f.seek(ini)
        return f.read(length).decode('utf-8')
    
def removePontuacao(s):
    chars_a_remover = r'^[^\w\s\']+|[^\'\w\s]+$'
    s = re.sub(chars_a_remover,'',s)

    if s.startswith("'"):
        return "'"+s[1:].capitalize()
    return s.capitalize()


def adicionaFrequenciaPalavras(ini, length):
    letra = getLetra(ini, length)
    palavras = set(re.split(r'[\s\n]+', letra))
    palavras = {removePontuacao(p) for p in palavras}

    hash = abreHash()

    for p in palavras:
        print(p,'-')
        hash.atualiza(p)

    salvaHash(hash)

def abreHash():
    with open(hash_bin, 'rb') as h:
        return pickle.load(h)

def salvaHash(hash):
    with open(hash_bin, 'wb') as h:
        pickle.dump(hash, h)

def abreFreq():
    with open(freq_palavras, 'rb') as h:
        return pickle.load(h)

def salvaFreq(lista):
    with open(freq_palavras, 'wb') as h:
        pickle.dump(lista, h)