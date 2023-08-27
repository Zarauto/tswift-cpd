import pandas as pd
import pickle
from os.path import join

# Define endereços de arquivo
root = join('.','')
src_name = join(root,'taylor_swift_spotify.csv')
tgt_name = join(root,'dados.csv')
dir_letras = join(root,'letras')

print(src_name)

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

df.to_csv(tgt_name, index=False)


# TESTE
rep = df[df['album'] == "reputation"]

links = join(root,"urls")
links = join(links,'reputation.txt')

with open(links, 'r') as t:
    for line in t:
        #print(line.split('#'))
        [name, link, mood] = line[:-1*(line[-1]=='\n')].split('#')
        rep.loc[rep['name'] == name, 'url'] = link
        rep.loc[rep['name'] == name, 'tematica'] = mood


from googleapiclient.discovery import build
import re

API_KEY = 'AIzaSyCpvKDb0XAjR2Jgq-7FsOo36UNfEUqpFM8'

# Extract video ID from URL
def get_video_id(url):
    video_id_match = re.search(r'(?<=v=)[^&#]+', url)
    video_id_match = video_id_match or re.search(r'(?<=be/)[^&#]+', url)
    #print(video_id_match.group(0))
    return video_id_match.group(0) if video_id_match else None

# Get view count using video ID
def get_view_count(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(part='statistics', id=video_id)
    response = request.execute()
    view_count = response['items'][0]['statistics']['viewCount']
    return view_count

for index, row in rep.iterrows():
    url = row['url']
    rep.at[index, 'views'] = get_view_count(get_video_id(url))

with open(join(root,'rep.bin'), 'wb') as save:
    pickle.dump(rep,save)
    
    
with open(join(join(root,'letras'),'reputation.txt')) as file:
    content = file.read()
    lista = content.split('@')
    
nomes = [lista[i][1:] for i in range(len(lista)) if i%2 == 0]
letras = [lista[i][1:] for i in range(len(lista)) if i%2 == 1]

if(len(nomes)>len(letras)):
    nomes.pop(-1)

for i in range(len(nomes)):
    print(nomes[i])
    letra_bin = letras[i].encode()
    
    with open(join(root,'letras.bin'), 'ab') as bf:
        ini = bf.tell()
        bf.write(letra_bin)
        length = len(letra_bin)
        
    rep.loc[rep['name'] == nomes[i], 'letra_ini'] = ini
    rep.loc[rep['name'] == nomes[i], 'letra_len'] = length


rep.to_csv(tgt_name)