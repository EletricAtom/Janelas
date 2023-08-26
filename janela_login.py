from PySimpleGUIQt import Window, Button,Text,Image,Input,theme,popup,WIN_CLOSED,Multiline,FileBrowse


theme('DarkBlue2')

mpb = (100,35)


def janela_login():
    layout_login = [[Image(filename='earth.png')],
          [Text('E-mail:'),Input(key='-EMAIL-')],
          [Text('Senha:'),Input(password_char='*',key='-SENHA-')],
          [Button('Login!',size=mpb,key='-LOGIN-'),Button('Esqueci a Senha',size=(100,35))]
               ]
    return Window("Janela Principal",
                 layout=layout_login,
                 element_justification='c',size=(1000,1000))

def janela_principal():
    try:
        layout_principal = [[Text('Aqui está a janela Principal')],
                            [Input('Digite aqui')],
                            [Button('Verificar',size=mpb),
                                Button('Atualizar',size=mpb),
                                Button('Cadastrar',size=mpb,key='-CADASTRAR-'),
                                Button('Sair',size=mpb,key='-SAIR-')]                     
                            ]
        return Window('janela Principal',
                    layout=layout_principal,
                    element_justification='c',
                    size=(1000,1000),progress_bar_color='Green')
    except:
        pass

def janela_cadastro():
        layout_cadastro = [[Text('Cadastrar Produtos',font='Helvetica 20')],
                           [Text('NOME DO PRODUTO',key='-NAME_PRODUCT-'),Input(size=(900,23))],
                           [Text('ID DO PRODUTO  ',key='-ID_PRODUCT'),Input(size=(900,23))],
                           [Button('ADICIONAR',size=mpb,),
                            Button('REMOVER',size=mpb),
                            Button('VOLTAR',key='-BACK-',size=mpb),
                            FileBrowse('ABRIR',enable_events=True,size=mpb)]                      
                           ]
        
        return Window('Janela de Cadastros',
                      layout=layout_cadastro,
                      element_justification='c',
                      size=(1000,1000))

janela_principal_ = False
window = janela_login()

#print(window.read())

while True:
    event, values = window.read()
    
    if event == '-LOGIN-':
        window.close()
        window = janela_principal()
        popup('Login Feito com Sucesso')
    
    if event == '-BACK-':
        window.close()
        window = janela_principal()
    
    if event == '-CADASTRAR-':
        window.close()
        window = janela_cadastro()

    if event == '-SAIR-' or event == WIN_CLOSED:
        break
        window.close()
        
