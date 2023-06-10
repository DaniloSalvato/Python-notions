import PySimpleGUI as sg

  #Criar Janelas e estilos(layouts) 
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('nome', key= 'nome')],       
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout = layout, finalize = True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Peperoni',key = 'pizza1'), sg.Checkbox('Pizza de Frango com Catupiri',key ='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]      
    ]
    return sg.Window('Montar pedido', layout = layout, finalize = True)

#Criar janelas iniciais 
janela1, janela2 = janela_login(), None

#Criar o loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #quando queremos ir pra proxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    #quando queremos voltar para a janela anterior
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Peperoni e uma pizza Frango Catupiri')
        elif values['pizza1'] == True :
            sg.popup('Foi solicitado uma Pizza de Peperoni')
        elif values['pizza2'] == True :
            sg.popup('Foi solicitado uma Pizza de Frango Catupiri')