import os
def main(): 
    os.system('cls')
    exibir_nome()
    opcaoes()
    escolher_opcao()

def exibir_nome():
    print('Sabor Express\n')

def exibir_sub_titulos(texto):
    os.system('cls')
    print(texto)
    print()

def voltar_ao_menu():
     input('\nPressione Uma Tecla Para Voltar Ao Menu!: ')
     main()

def opcaoes():
    print('1. Cadastar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante') 
    print('4. Sair\n')   

def escolher_opcao():
    try: 
        opçao_escolhida = int(input('Escolha Uma opção: '))
        if opçao_escolhida == 1:
            cadastarar_novo_restaurante()
        elif opçao_escolhida ==2:
           listar_restaurantes()
        elif opçao_escolhida == 3:
            alterar_estado_restaurante()
        elif opçao_escolhida == 4:
             finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastarar_novo_restaurante():
    exibir_sub_titulos('Cadastro De Novos Restaurantes')
    nome_do_restaurante = input('Digite o Nome Do Restaurante Que Deseja Cadastrar: ')
    categoria = input(f'Digite a categoria do Restaurante "{nome_do_restaurante}": ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria,'ativo': False}
    restaurates.append(dados_do_restaurante)
    print(f'O Restaurante "{nome_do_restaurante}", Foi Cadastrado Com sucesso!\n')
    voltar_ao_menu()

restaurates = [{'nome':'sushi ya','categoria':'Japonesa','ativo':False},
               {'nome':'pipers','categoria':'bar','ativo':True},
               {'nome':'dois irmaos','categoria':'Portugues','ativo':False}]

def listar_restaurantes():
    exibir_sub_titulos('Listando Restaurantes')
    
    for restaurante in restaurates:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante ['ativo']
        print(f'-{nome_restaurante}. | {categoria}. | {ativo}.')
    voltar_ao_menu() 

def alterar_estado_restaurante():
    exibir_sub_titulos('Alterar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurates:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True 
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante{nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'O restaurante {nome_restaurante} Foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')
    voltar_ao_menu()

def opcao_invalida():
    print('Opção Invalida\n')
    voltar_ao_menu()
  
def finalizar_app ():
    exibir_sub_titulos('Finalizando Programa')
    
if __name__ == '__main__': 
    main() 