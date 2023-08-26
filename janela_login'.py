from PySimpleGUIQt import Window, Button,Text,Image,Input,theme,popup,WIN_CLOSED,Multiline,FileBrowse
import cv2
from time import sleep



theme('DarkBlue2')

mpb = (100,35)

cap = cv2.VideoCapture(0)
recording = False
global adicionado
adicionado = ''


def janela_login():
    layout_login = [[Image(filename='Start.png')],
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
                            [Input('Por favor não digita nada aqui')],
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
def generate_qrcode():
                                                  #Essa função será responsavel por gerar os qrcodes
    products = values['-NAME_PRODUCT-'].lower()           #Variavel recebe o value da key
    import qrcode

    adicionando = True                                                  #Apenas para debug do codigo criamos uma pequena listinha adicionado um pouco de produtos

    global ja_tem                                                       #variável global 'ja_tem' para verificar a existencia do produto
    ja_tem = False                                                      #A variavel inicia como falsa e será verdadeira caso não exista apenas apos a leitura
    with open('dados.txt', 'r') as arquivo:
                eu_recebi = arquivo.readlines()

    def leitura():                                                      #Criação de uma função de leitura(responsavel por armazenar a leitura do aquivo txt) 
        for c in eu_recebi:                                             #Um laço for para varrer a lista e verificar ja existe dentro do arquivo
            if products in c :                                                 #Se existe 
                print('ja tem')                                        #Apenas verificação de forma visual                                      
                ja_tem = True                                           #A variavel de verificação se torna verdadeira
                if ja_tem == True:
                     window['-TXADD-'].update('Esse Produto já foi adicionado',background_color='red')
                break                                                   #Pausamos a leitura


    def escrita():                                                      #Função de escrita do novo produto dentro da lista                                                       
        with open('dados.txt','a') as arquivo:                          #Abrimo o arquivo de produtos 'dados.txt'
                arquivo.write(f'{products}\n')                                 #Fazemos a escrita                      


    def gerar_qrcode():                                                 #Função que gera o qrcode
        qrcode_generate = qrcode.make(products)                              #geramos efetivamente o qr code porém ainda não será salvo (apenas o conteudo que será salvo no qrcode ou seja a informação que el irá conter)
        #saving = 'qrs_gerados/'+ a + '.png'                           #Aqui nomeamos o qrcode e adicionamos o caminho desejado
        qrcode_generate.save(f'qrs_gerados/{products}.png')                  #Salvamos efetivamente o qrcode 
        if ja_tem == False:
            print(f'{products} foi adicionado')
            window['-TXADD-'].update('ADICIONADO',background_color='green')            


            
    rodando = True                                                      #Variavel responsavel por manter o loop funcionando para a leitura e escrita do produto dentro do qrcode
    while rodando:
        
        #a = str(input('Digite um produto: ')).strip().lower()           #recebe o nome do produto a ser adicionado
        leitura()                                                       #Chamamos a função de leitura para verificar se o produto já existe
        if ja_tem == False:                                             #Se ainda não tem o produto
            escrita()                                                   #Chamamos a funnção de leitura

       #b = str(input('Deseja Adicionar um novo produto ?')).strip().lower()    #Teste para continuar adicionando produtos
       #if b == 'n':
                #rodando = False
        

        with open('dados.txt', 'r') as arquivo:
                eu_recebi = arquivo.readlines()
                gerar_qrcode()
                
                rodando = False
            



def janela_cadastro():
        
        layout_cadastro = [[Text('Cadastrar Produtos',font='Helvetica 20')],
                           [Text('NOME DO PRODUTO'),Input(key='-NAME_PRODUCT-')],
                           [Text('ID DO PRODUTO     '),Input(key='-ID_PRODUCT')],
                           #[Image('Qr Code gerado',filename=qr_generate,size=(300,300)),]
                           [Image('qrs_gerados/caju.png',size=(800,800)),Text('',background_color=adicionado,size=(100,50),key='-TXADD-')],
                           [Button('ADICIONAR',size=mpb,key='-ADICIONAR-'),
                            Button('REMOVER',size=mpb),
                            Button('VOLTAR',key='-BACK-',size=mpb),
                            FileBrowse('ABRIR',enable_events=True,size=mpb),
                            Button('INFORMAÇÕES',size=mpb,key='-INFORMACOES-')]                      
                           ]
        
        return Window('Janela de Cadastros',
                      layout=layout_cadastro,
                      element_justification='c',
                      size=(1000,1000))

def janela_serial():
    pass
def janela_plotgraph():             #Uma janela que plota dados qualquer
    pass

def aurora_window():                #A janela da aurora dever conter a camera e o plot dos dados seriais e o controle
    pass
    

janela_principal_ = False
window = janela_login()

#print(window.read())

while True:
    event, values = window.read()
    
    if event == '-LOGIN-':
        window.close()
        window = janela_principal()
        popup('Login Feito com Sucesso',button_color='red')
    
    if event == '-BACK-':
        window.close()
        window = janela_principal()
    
    if event == '-CADASTRAR-':
        window.close()
        window = janela_cadastro()

    if event == '-ADICIONAR-':
        generate_qrcode()
        
        
    if event == '-INFORMACOES-':
        with open('informacoes.txt','r',encoding='utf-8') as arquivo:
            text = arquivo.read()
        popup(text,title='Informações',text_color='black',custom_text=('ENTENDI'),background_color='white')

    

    if event == '-SAIR-' or event == WIN_CLOSED:
        break
        window.close()
