"""
Projeto: Simple Agenda
Descrição : uma agenda simples para guarda o nome e telefone do contato, primira versao feita
em ambiente shell , agora portada para ambiente grafico usando o pySimpleGUI.

Modulo: auxiliar , tem as funcoes de mais baixo nivel que auxiliam a armazenamento em memoria,
acesso a disco e operacões de CRUD

Autor : Joao Santanna - joaosantanna@yahoo.com.br
versao : beta 0.1
"""
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


def apagar_contato(nome):

    for contato in agenda:
        if nome == contato["Nome"]:
            agenda.remove(contato)
            return True
    return False


def editar_contato(nome,novo_nome, novo_telefone):

    for contato in agenda:
        if nome == contato["Nome"]:
            contato["Nome"] = novo_nome
            contato["Telefone"] = novo_telefone
                
           

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
        
        
    
    