import pandas as pd
import matplotlib.pyplot as plt
import arquivos as arq

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
