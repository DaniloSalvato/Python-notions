from PySimpleGUI import PySimpleGUI as sg

#teste de tela de login

#layout
sg.theme('Reddit')
layout = [[sg.Text('Usuário'), sg.Input(key='usuario', size = (20,1))],
          [sg.Text('Senha'), sg.Input(key='senha',size = (20,1), password_char = '*')],
          [sg.Checkbox('salvar login?')],
          [sg.Button('Entrar')]]

# janela
janela = sg.Window('Tela de Login', layout)

# Ler os evento
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Danilo' and valores['senha'] == '12345':
            print('Bem vindo!')