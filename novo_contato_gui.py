import PySimpleGUI as sg      

def get_valores_novo_contato():
    janela2 = sg.Window('Novo contato',size=(350, 180) ,font=('Helvetica', 14))


    layout = [[sg.Text('Informe os dados do contato')],      
              [sg.Text('Nome', size=(8,1)),sg.InputText()],
              [sg.Text('Telefone', size=(8,1)),sg.InputText()],
              [sg.Button('Adicionar'), sg.Cancel()]]      

    janela2 = janela2.Layout(layout)    

    event, values = janela2.Read()    
    print(event, values)
    janela2.Close()
    if event == 'Adicionar':
        return values
    else:
        return 0

def confirmar_remocao():