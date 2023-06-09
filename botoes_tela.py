from PySimpleGUI import PySimpleGUI as sg
#layout

class TelaPython:
    def __init__(self):
        sg.theme('Reddit')
        layout = [[sg.Text('nome', size = (5,0)), sg.Input(key='nome', size = (20,1))],
                  [sg.Text('idade', size = (5,0)), sg.Input(key='idade',size = (20,1))],
                  [sg.Text('Selecione a extensão do seu e-mail')],
                  [sg.Checkbox('Gmail', key = 'gmail'),sg.Checkbox('Outlook', key = 'outlook'),sg.Checkbox('Yahoo', key = 'yahoo')],
                  [sg.Text('Aceita cartão')],
                  [sg.Radio('Sim','cartoes', key = 'aceitaCartao'),sg.Radio('Não', 'cartoes', key ='naoAceitaCartao')],
                  [sg.Slider(range=(0,100),default_value=0,orientation='h', size=(15,20), key= 'sliderVelocidade')],
                  [sg.Button('Envia dados')],
                  [sg.Output(size = (30,20))]]
        #janela
        self.janela = sg.Window('Tipos de input', layout)   
        

    def Iniciar(self):
        while True:
            # Ler os evento da tela
            self.button, self.values = self.janela.read()
            nome = self.values['nome']
            idade = self.values['idade']
            checkbox_gmail = self.values['gmail']
            checkbox_outlook = self.values['outlook']
            checkbox_yahoo = self.values['yahoo']
            aceita_Cartao = self.values['aceitaCartao']
            nao_Aceita_Cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'checkbox gmail: {checkbox_gmail}')
            print(f'checkbox outlook: {checkbox_outlook}')
            print(f'checkbox yahoo: {checkbox_yahoo}')
            print(f'radio aceita cartão: {aceita_Cartao}')
            print(f'radio não aceita cartão: {nao_Aceita_Cartao}')
            print(f'velocidade script: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()
           