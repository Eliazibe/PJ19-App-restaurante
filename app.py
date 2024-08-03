import os

restaurantes = [{'nome': 'maripi', 'categoria': 'japonesa', 'ativo': False},
                {'nome': 'adress', 'categoria': 'cafe', 'ativo': True},
                {'nome': 'zibzz', 'categoria': 'coxinha', 'ativo': True}]

def exibir_nome_do_programa():
    '''Exibi o nome do programa na tela print'''

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():   
    '''Essa funcao exibe as opcoes primarias do codigo'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa funcao fecha a api'''

    exibir_subtitulo('Finalizando o app')

def voltar_ao_menur_principal():
    '''Essa funcao serve para voltar ao menu inicial
    
    - Input: retorna ao menu inicial

     Outputs:
    - Retorna ao menu principal
    '''

    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Essa funcao da o retor quando uma opcao e invalida
    
     Outputs:
    - Retorna ao menu principal
    '''

    print('Opcao invalida!\n')
    voltar_ao_menur_principal()

def cadastrar_novo_restaurante():
    '''Essa funcao e responsavel por cadastrar um novo restaurante
    
    inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante na lista de restaurantes
    
    ''' #docstrings
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante{nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} # dicionario dos restaurantes
    restaurantes.append(dados_do_restaurante) # append -> coloca dentro da lista 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menur_principal()

def listar_restaurante():
    '''Essa funcao mostra a lista de restaurantes cadatrados'''

    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menur_principal()    

def exibir_subtitulo(texto):
    '''Essa funcao exibe alguns subtitulos antes e depois de alguns textos'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def alternar_estado_restaurante():
    
    '''Essa funcao altera o estado do restaurante
    
    - Input:
    - Nome restaurante = escolhe qual o restaurante que vai ser alterado o estado

    
    '''

    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do estaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado =True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')        

    voltar_ao_menur_principal()  
   
def escolher_opcoes():
    '''Essa funcao escolhe qual a opcao que voce solicitou
    
    - input: opcao escolhida = onde voce vai escolher a sua opcao
    
    '''


    try: # tenta executar isso
        opcao_escolhida = int(input('Escolha uma opcao: '))
        # opcao_escolhida = int(opcao_escolhida)    

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()    
        elif opcao_escolhida == 3:
            alternar_estado_restaurante() 
        elif opcao_escolhida == 4:
            finalizar_app()   #print('Encerrando o Prodgrama') 
        else:
            opcao_invalida()
    except: # caso ele nao consiga executar, ira exibir a opcao invalida
        opcao_invalida()    

# outra opcao ultilizando o - match - 
#def escolher_opcoes():  
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Adicionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        case _:
            print('Opção inválida!')
      
def main():
    '''Essa funcao vai voltar ao menu inicial'''

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
