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

API_KEY = 'AIzaSyCpvKDb0XAjR2Jgq-7FsOo36UNfEUqpFM8'

def getLyricsAux(df, path):
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
            
            ini = bf.tell()
            bf.write(letra_bin)
            length = len(letra_bin)
            
            df.loc[df['name'] == nomes[i], 'letra_ini'] = ini
            df.loc[df['name'] == nomes[i], 'letra_len'] = length

def getLyrics(df):
    albuns = set(df['album'].tolist())
    
    for a in albuns:
        getLyricsAux(df, join(dir_letras,f'{a}.txt'))

def getViewsFromYT(url):
    video_id_match = re.search(r'(?<=v=)[^&#]+', url)
    video_id_match = video_id_match or re.search(r'(?<=be/)[^&#]+', url)
    video_id = video_id_match.group(0) if video_id_match else None

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(part='statistics', id=video_id)
    response = request.execute()
    return response['items'][0]['statistics']['viewCount']

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
        getLinksAux(df, join(dir_links,f'{a}.txt'))

def inicializaFromKaggle():
    # Cria dataframe reduzido a partir do arquivo fonte
    df = pd.read_csv(src_name)

    df = df[['id','name','album','release_date','track_number','duration_ms']]

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

    # Atribui ID a cada música
    df['id'] = list(range(1,len(df)+1))
    
    getLinksTematica(df)
    getViews(df)
    getLyrics(df)

    with open(tgt_name, 'wb') as arq:
        pickle.dump(df, arq)