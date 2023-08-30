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
    escolhaUsuário = -1
    
    while True:
        
        mostraOpcoesMenuPrincipal()
        escolhaUsuário = input()
        print("\n")
        
        # Verificação de input
        if type(escolhaUsuário) is not int or not 0<=escolhaUsuário<=4:
            print("Opção inválida. Insira um número de 0 a 4.\n")
            continue
        
        if escolhaUsuário == 0:
            return
        
        if escolhaUsuário == 1:
            menuListaMusicas()
            continue
        
        if escolhaUsuário == 2:
            menuBusca()
            continue
            
        if escolhaUsuário == 3:
            menuEstatisticas()
            continue
        
        menuAddMusica()
        
def menuListaMusicas():
    pass

def menuBusca():
    pass

def menuAddMusica():
    pass