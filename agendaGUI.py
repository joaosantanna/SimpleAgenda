"""
Projeto: Simple Agenda
Descrição : uma agenda simples para guarda o nome e telefone do contato, primira versao feita
em ambiente shell , agora portada para ambiente grafico usando o pySimpleGUI.

Autor : Joao Santanna - joaosantanna@yahoo.com.br
versao : beta 0.1

Descrição dos arquivos:
- agendaGUI.py - aquivo principal que contem as chamadas a GUI
- operacoes2.py - arquivo de suporte com as funcoes do software relacionadas ao modelo, contem também a
estrutura de armazenamento , uma lista de dicionarios chamada agenda
"""
from operacoes import *
import PySimpleGUI as sg
from dialogos_suporte import get_valores_novo_contato, confirmar_remocao, dialogo_editar_contato


# carrega dados do arquivo salvo 
carregar_dados()
#alimenta a listbox com os nomes dos contatos
valores= get_nome_contatos()

# definicoes da interface
janela = sg.Window('Agenda Simples',size=(700, 400) ,font=('Helvetica', 14))

sg.ChangeLookAndFeel('BlueMono')

# Column layout      
col1 = [[sg.Text('Informações do contato',size=(30, 1),justification='center')],
        [sg.Text('Nome:',size =(25,1),auto_size_text=True, key='txt_nome')],
        [sg.Text('Telefone:',size =(25,1), auto_size_text=True, key ='txt_telefone')],      
        [sg.Text('')],
        [sg.Text('')],
        [sg.Button("Adicionar",size=(10, 1))],
        [sg.Button("Apagar",size=(10, 1)), sg.Button("Editar",size=(10, 1))]
        ]


col2 =[[sg.Listbox(values= valores ,change_submits=True, size=(30,15),key='lista_de_contatos') ]]



layout = [[sg.Column(col1),sg.Column(col2) ],
              [sg.Exit(size=(10, 1))]]      

janela.Layout(layout)

#laço de controle da janela
while True:
    
    event, values = janela.Read()  
    print(event, values)
    
    if event == "Adicionar":
        resultado = get_valores_novo_contato()
        if resultado != 0:
            nome = resultado[0]
            telefone = resultado[1]
            novo_contato(nome, telefone)
            valores = get_nome_contatos()
            janela.FindElement('lista_de_contatos').Update(valores)
            
    if event == "Apagar":
        
        nome = values['lista_de_contatos']    
        # listbox sempre retorna uma lista, mesmo a selecao sendo single element
        if len(nome) > 0:
            nome = nome[0]
            if confirmar_remocao():
                if apagar_contato(nome):
                    sg.Popup('Contato apagado\n com sucesso!')
                    valores = get_nome_contatos() # atualizar a list box
                    janela.FindElement('lista_de_contatos').Update(valores)
                    #atualizar os Texts
                    janela.FindElement('txt_nome').Update('Nome: ')
                    janela.FindElement('txt_telefone').Update('Telefone: ')
        
    if event == "Editar":
        nome = values['lista_de_contatos'][0]
        contato = buscar_contato(nome)
        resultado = dialogo_editar_contato(contato)# chama o dialogo para alterar valores
        if resultado != False: # se o usuario nao cancelou a alteracao
            editar_contato(nome, resultado[0],resultado[1])
            valores = get_nome_contatos() # atualizar a list box
            janela.FindElement('lista_de_contatos').Update(valores)
            #atualizar os Texts
            janela.FindElement('txt_nome').Update('Nome: ')
            janela.FindElement('txt_telefone').Update('Telefone: ')
                    
                    
    if event == 'lista_de_contatos': # faz a funcao de busca pelo list box
        nome = values['lista_de_contatos']    
        # listbox sempre retorna uma lista, mesmo a selecao sendo single element
        print(nome[0])
        c = buscar_contato(nome[0])
        if c != 0:
            janela.FindElement('txt_nome').Update('Nome: ' + c['Nome'])
            janela.FindElement('txt_telefone').Update('Telefone: ' + c['Telefone'])
    
    
    if event == "Exit":
        salvar_dados() # salva os dados em arquivo
        sg.Popup("Bye!","Tchau obrigado por\n usar o aplicativo")
        break # sai do laço
    
janela.Close()


'''
TODO:

     
    - Implementar a funcao de editar os dados do contato
    - usar o lint para melhorar o codigo
    - implementar as outras funcoes , deletar e editar para completar o CRUD
    - criar os testes de software para testar a camada do modelo MVC - MOdelo , view , controler
    - separar a view do controle ... ver se é possivel com o SG ( pysimpleGUI)
    - depois de testado limpar o diretorio e os arquivos não utilizados do commit da versao 1
'''