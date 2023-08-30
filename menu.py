import arquivos as arq
import operacoes as op
import patricia as pat
from os.path import exists
import math


# Verifica se precisa inicializar
def checaInicializacao():
    
    # Se não existir o arquivo com os dados ou se ele estiver vazio
    if not exists(arq.tgt_name) or len(arq.abreLeitura()) == 0:
        print("O programa está sendo inicializado. Isso pode demorar alguns instantes.\n")
        arq.inicializaFromKaggle()


def mostraOpcoesMenuPrincipal():
    print("Selecione uma opção:\n\n[1] Listar Músicas\n[2] Buscar Música\n[3] Ver Estatísticas\n[4] Adicionar Música\n[0] Fechar Programa\n")        
        
def menuPrincipal():
    escolhaUsuario = -1
    
    while True:
        
        mostraOpcoesMenuPrincipal()
        escolhaUsuario = input()
        print("\n")
        
        # Verificação de input
        if not '0'<=escolhaUsuario<='4':
            print("Opção inválida. Insira um número de 0 a 4.\n")
            continue
        
        escolhaUsuario = int(escolhaUsuario)
        
        if escolhaUsuario == 0:
            return
        
        if escolhaUsuario == 1:
            menuListaMusicas()
            continue
        
        if escolhaUsuario == 2:
            menuBusca()
            continue
            
        if escolhaUsuario == 3:
            menuEstatisticas()
            continue
        
        menuAddMusica()
        
def menuListaMusicas():
    print('------------------------')
    
    entrada = -1
    
    while entrada != '0':
    
        print("Selecione uma opção:")
        print("[1] Listar todas as músicas")
        print("[2] Listar por álbum")
        print("[3] Listar por temática")
        print("[0] Voltar para o menu principal\n")
        
        entrada = input()
        
        if not '0' <= entrada <= '3':
            print("Opção inválida. Insira um número entre 0 e 3\n")
            continue    
        
        if entrada == '1':
            listaTodas()
            entrada = '0'
            
        if entrada == '2':
            listaPorAlbum()
            entrada = '0'
            
        if entrada == '3':
            listaPorTema()
            entrada = '0'
            
        if entrada == '0':
            return
    

def listaTodas():
    a = arq.abreArvore()
    
    todas = a.listaTodas()
    
    entrada = -1
    
    while True:
    
        for i in range(len(todas)):
            print(f"[{i+1}] {todas[i][1].titulo}")
            
        print("\n[I] Inverter ordem de exibição")
        print("[X] Voltar ao menu principal")
        
        entrada = input('\nSeleção: ')
            
        if entrada.lower() != 'i' and entrada.lower() != 'x' and not 0 < int(entrada) <= (len(todas)):
            print("Opção inválida. Tente novamente.\n")
            continue
            
        if entrada.lower() == 'x':
            return
        
        if entrada.lower() == 'i':
            todas.reverse()
            continue
            
        i = int(entrada)
    
        index = todas[i-1][1].indice
        op.exibeInfoMusica(index)
        return
    
def listaPorAlbum():
    albums = arq.abreAlbums()
    
    j = 1
    for i, row in albums.iterrows():
        print(f"[{j}] {row['album']}")
        j += 1
        
    entrada = int(input('\nSeleção: '))
    
    j = 1
    for i, row in albums.iterrows():
        if j == entrada:
            a = row['album']
            df = arq.abreLeitura()
            df = df[df['album'] == a]
            
            arv = pat.criaArvoreFromDF(df)
            
            todas = arv.listaTodas()
            
            for i in range(len(todas)):
                print(f"[{i+1}] {todas[i][1].titulo}")
            
            #print("\n[I] Inverter ordem de exibição")
            print("\n[X] Voltar ao menu principal")
            
            entrada = input('\nSeleção: ')
                
            if entrada.lower() != 'i' and entrada.lower() != 'x' and not 0 < int(entrada) <= (len(todas)):
                print("Opção inválida. Tente novamente.\n")
                continue
                
            if entrada.lower() == 'x':
                return
            
            if entrada.lower() == 'i':
                todas.reverse()
                continue
                
            i = int(entrada)
        
            index = todas[i-1][1].indice
            op.exibeInfoMusica(index)
            return
        
        j += 1
        
def listaPorTema():
    temas = ['Romantica','Melancolica','Lembranca','Vingativa','Misc.']
    
    for i in range(len(temas)):
        print(f"[{i+1}] {temas[i]}")
    entrada = int(input('\nSeleção: '))
    
    tema = temas[entrada-1]
    
    print('\n')
    
    df = arq.abreLeitura()
    df = df[df['tematica'] == tema]
    
    arv = pat.criaArvoreFromDF(df)
            
    todas = arv.listaTodas()
    
    for i in range(len(todas)):
        print(f"[{i+1}] {todas[i][1].titulo}")
    
    print("\n[X] Voltar ao menu principal")
    
    entrada = input('\nSeleção: ')
    
    if entrada.lower() == 'x':
        return
    i = int(entrada)
        
    index = todas[i-1][1].indice
    op.exibeInfoMusica(index)
    return
    

def menuBusca():
    termo = input("\nDigite o termo a ser buscado: ")
    print()

    arv = arq.abreArvore()

    achou = any(chave[0] == termo[0] for chave in arv.filhos_raiz)
    
    if not achou:
        print("Não houve correspondência ao seu termo de pesquisa.\n")
        return

    resultados = arv.buscaPorString(termo)

    if len(resultados) == 0:
        print("Não houve correspondência ao seu termo de pesquisa.\n")
        return
    
    for i in range(len(resultados)):
        print(f"[{i+1}] {resultados[i][1].titulo}")
    
    print("\n[X] Voltar ao menu principal")
    
    entrada = input('\nSeleção: ')
    
    if entrada.lower() == 'x':
        return
    i = int(entrada)
        
    index = resultados[i-1][1].indice
    op.exibeInfoMusica(index)
    return
    
    

def menuEstatisticas():
    print("[1] Comparar visualizações das músicas no YouTube")
    print("[2] Ver frequência das palavras nas letras das músicas") 
    print("[0] Voltar ao menu principal\n")
    
    entrada = input()
    
    if entrada == '0':
        return
    
    if entrada == '1':
        menuViews()
        return
    
    if entrada == '2':
        verFrequencia()
        return
    
    print("Opção inválida.\n")
    menuEstatisticas()
    return

def menuViews():
    print()
    print("[1] Comparar músicas de um mesmo álbum")
    print("[2] Comparar por temática")
    print("[3] Mostrar todas as músicas em ordem descrescente")
    print("[4] Mostrar todas as músicas em ordem crescente")
    print("[0] Voltar ao menu principal\n")
    
    entrada = input('\n')
    
    if entrada == '0':
        return
    
    if entrada == '1':
        viewsAlbum()
        return
    
    if entrada == '2':
        viewsTema()
        return
    
    if entrada == '3':
        op.graficoBarrasTodas(True) 
        return
    
    if entrada == '4':
        op.graficoBarrasTodas(False) 
        return
    
    print("Opção inválida.\n")
    menuViews()
    return

def viewsAlbum():
    albums = arq.abreAlbums()
    
    j = 1
    for i, row in albums.iterrows():
        print(f"[{j}] {row['album']}")
        j += 1
        
    entrada = int(input('\nSeleção: '))
    
    j = 1
    for i, row in albums.iterrows():
        if j == entrada:
            a = row['album']
            break   
        j+=1
        
    op.graficoBarrasAlbum(a)
    
def viewsTema():
    temas = ['Romantica','Melancolica','Lembranca','Vingativa','Misc.']
    
    for i in range(len(temas)):
        print(f"[{i+1}] {temas[i]}")
    entrada = int(input('\nSeleção: '))
    
    tema = temas[entrada-1]
    
    print('\n')
        
    op.graficoBarrasTema(tema)
    
def verFrequencia():
    print("[1] Mostrar por ordem decrescente de frequência")
    print("[2] Mostrar por ordem crescente de frequência")
    
    entrada = input()
    
    h = arq.abreHash()
    
    a = arq.abreArvore()
    num = a.num_nodos
    del a
    
    lista = h.to_list()
    lista.sort()
    
    if entrada == '2':
        lista.reverse()
    
    print("\n----------------------------------------------")
    
    esp = 16
    
    print(f"Palavra{' '*(esp-len('palavra'))} | Ocorrências | Frequência\n")
    for t in lista:
        print(f"{t.palavra}{' '*(esp-len(t.palavra))} | {t.freq}{' '*(len('ocorrencias')-int(math.log10(t.freq))-1)} | {(t.freq/num)*100:.2f} %")
        
    print('----------------------------------------------\n')
        
    

def menuAddMusica():
    pass