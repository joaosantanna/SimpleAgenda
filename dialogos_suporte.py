"""
Projeto: Simple Agenda
Descrição : uma agenda simples para guarda o nome e telefone do contato, primira versao feita
em ambiente shell , agora portada para ambiente grafico usando o pySimpleGUI.

Modulo: auxiliar , tem os dialogos da UI 

Autor : Joao Santanna - joaosantanna@yahoo.com.br
versao : beta 0.1
"""
import PySimpleGUI as sg      

def dialogo_novo_contato():
    janela2 = sg.Window('Novo contato',size=(350, 180) ,font=('Helvetica', 14))


    layout = [[sg.Text('Informe os dados do contato')],      
              [sg.Text('Nome', size=(8,1)),sg.InputText()],
              [sg.Text('Telefone', size=(8,1)),sg.InputText()],
              [sg.Button('Adicionar'), sg.Cancel()]]      

    janela2 = janela2.Layout(layout)    

    event, values = janela2.Read()    
    
    janela2.Close()
    if event == 'Adicionar':
        return values
    else:
        return 0

def dialogo_confirmar_remocao():
    janela3 = sg.Window('Confirmar ?',size=(250, 100) ,font=('Helvetica', 14))

    layout = [[sg.Text('Você realmente deseja \n apagar o contato?')],      
              [sg.Button('Sim'), sg.Button('Não')]]      

    janela3 = janela3.Layout(layout)    

    event, values = janela3.Read()    
    
    janela3.Close()
    if event == 'Sim':
        return True
    else:
        return False

def dialogo_editar_contato(contato):
    janela3 = sg.Window('Editar contato',size=(350, 180) ,font=('Helvetica', 14))

    layout = [[sg.Text('Edite os dados do contato')],      
              [sg.Text('Nome', size=(8,1)),sg.InputText(contato['Nome'])],
              [sg.Text('Telefone', size=(8,1)),sg.InputText(contato['Telefone'])],
              [sg.Button('Atualizar'), sg.Cancel()]]      

    janela3 = janela3.Layout(layout)    

    event, values = janela3.Read()    
    
    janela3.Close()
    if event == 'Atualizar':
        novo_nome = values[0]
        novo_telefone = values[1]
        return (novo_nome,novo_telefone)
    else:
        return False