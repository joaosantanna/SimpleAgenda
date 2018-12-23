import os.path
import pickle
import PySimpleGUI as sg  

agenda = []

def novo_contato(nome, telefone):
    '''
    Adiciona novos contatos na agenda, recebe um nome e telefone,
    ambos strings
    '''
    contato ={"Nome": nome , "Telefone" : telefone}
    agenda.append(contato)

def imprimir_contatos():
    print(" Contatos cadastrados na agenda")
    if len(agenda) > 0:
        print("Nome \t  Telefone")
        for contato in agenda:
            print( contato["Nome"],"\t", contato["Telefone"])
    else:
        print("Nenhum contato na agenda")

def apagar_contato(nome):

    for contato in agenda:
        if nome == contato["Nome"]:
            agenda.remove(contato)
            return True
    return False


def editar_contato():
    print(" Editar contato")
    nome = input("Digite o nome do contato que vc quer editar:")
    for contato in agenda:
        if nome == contato["Nome"]:
            op = input("Editar nome de {} (s)=sim (n)=Não\n :>".format(contato["Nome"] )) 
            if opos.path.isfile('dados_agenda.txt') == 's' or op == 'S':
                contato["Nome"] = input("Nome:")
                print(" Nome atualizado")
            op = input("Editar Telefone de {} (s)=sim (n)=Não\n :>".format(contato["Nome"] )) 
            if op == 's' or op == 'S':
                contato["Telefone"] = input("Telefone:")
                print(" Telefone atualizado")
           

def buscar_contato(nome):
    '''
    Função que procura por um contato na agenda, recebe como parametro
    um nome em string . Retorna o contato caso ele exista ou o numero
    0(zero) caso o contato não exista
    '''
    for contato in agenda:
        if nome == contato["Nome"]:
            return contato
    sg.Popup("Contato não encontrado")
    return 0
    
def salvar_dados():
    '''
    Função para salvar os dados contidos na agenda em um arquivo binario
    '''
    with open('dados_agenda.bin','wb') as arq:
        pickle.dump(agenda , arq)

def carregar_dados():
    
    if os.path.isfile('dados_agenda.bin'):
        with open('dados_agenda.bin','rb') as arq:
            tmp = pickle.load(arq)
            for d in tmp:
                agenda.append(d)
            print('dados carregados com sucesso')
      # caso o arqivo nao exista o software inicia com uma lista vazia        

def get_nome_contatos():
    """
    Retorna o nome dos contatos para exibir na UI,
    ou uma lista vazia caso nao tenha contatos
    """
    contatos = []
    for c in agenda:
        contatos.append(c['Nome'])
    contatos.sort() # ordena antes de devolver :-)
    return contatos
        
        
    
    