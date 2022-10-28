# Tela de usuário Simples.

from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [ 
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
Janela = sg.Window('Tela de Login',layout)
# Ler os eventos
while True:
  eventos, valores = Janela.read()
  if eventos == sg.WINDOW_CLOSED:
    break
if eventos == 'Entrar':
    if valores['usuario'] == 'hitalo' and valores ['senha'] == '123456':
        print ('Bem vindo ao novo mundo!')
