import qrcode

adicionando = True                                                  #Apenas para debug do codigo criamos uma pequena listinha adicionado um pouco de produtos
if __name__ == '__main__':
    lista = ['tatu','cachorro','papagaio','capivara']
    with open('dados.txt', 'a') as arquivo:
        for c in lista:
            arquivo.write(f'{c}\n')

global ja_tem                                                       #variável global 'ja_tem' para verificar a existencia do produto
ja_tem = False                                                      #A variavel inicia como falsa e será verdadeira caso não exista apenas apos a leitura
products = ''
with open('dados.txt', 'r') as arquivo:
            eu_recebi = arquivo.readlines()

def leitura():                                                      #Criação de uma função de leitura(responsavel por armazenar a leitura do aquivo txt) 
    for c in eu_recebi:                                             #Um laço for para varrer a lista e verificar ja existe dentro do arquivo
        if products in c :                                                 #Se existe 
            #print('ja tem')                                        #Apenas verificação de forma visual                                      
            ja_tem = True                                           #A variavel de verificação se torna verdadeira
            break                                                   #Pausamos a leitura


def escrita():                                                      #Função de escrita do novo produto dentro da lista                                                       
    with open('dados.txt','a') as arquivo:                          #Abrimo o arquivo de produtos 'dados.txt'
            arquivo.write(f'{products}\n')                                 #Fazemos a escrita                      


def gerar_qrcode():                                                 #Função que gera o qrcode
      qrcode_generate = qrcode.make(a)                              #geramos efetivamente o qr code porém ainda não será salvo (apenas o conteudo que será salvo no qrcode ou seja a informação que el irá conter)
      #saving = 'qrs_gerados/'+ a + '.png'                           #Aqui nomeamos o qrcode e adicionamos o caminho desejado
      qrcode_generate.save(f'qrs_gerados/{a}.png')                  #Salvamos efetivamente o qrcode             


        
rodando = True                                                      #Variavel responsavel por manter o loop funcionando para a leitura e escrita do produto dentro do qrcode
while rodando:
    
    #a = str(input('Digite um produto: ')).strip().lower()           #recebe o nome do produto a ser adicionado
    leitura()                                                       #Chamamos a função de leitura para verificar se o produto já existe
    if ja_tem == False:                                             #Se ainda não tem o produto
        escrita()                                                   #Chamamos a funnção de leitura

    b = str(input('Deseja Adicionar um novo produto ?')).strip().lower()    #Teste para continuar adicionando produtos
    if b == 'n':
            rodando = False
    

    with open('dados.txt', 'r') as arquivo:
            eu_recebi = arquivo.readlines()
            gerar_qrcode()
        
        
