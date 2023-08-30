import arquivos as arq
from os.path import exists


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
    pass

def menuBusca():
    pass

def menuEstatisticas():
    pass

def menuAddMusica():
    pass