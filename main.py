lista_livro = [] # armazena os livros cadastrados
id_global = 0 # variavel acumuladora para o id dos livros cadastrados

# cadastro de livros na lista de livros 
def cadastrar_livro(id_global):

    print('-' * 40)
    print('-' * 8, 'MENU CADASTRAR LIVRO','-' * 10)

    nome_livro = input('Por favor digite o nome do livro: ')
    autor = input('Por favor digite o nome do autor do livro: ')
    editora = input('Por favor digite o nome da editora do livro: ')
    print('-' * 40)
    
    # armazena o cadastro dos inputs dentro de um dicionario
    livro = {
        'id': id_global,
        'nome': nome_livro,
        'autor': autor,
        'editora': editora
    }

    # cria uma copia do dicionario e adiciona na lista de livros
    lista_livro.append(livro.copy())

def consultar_livro():
    while True:
        print('-' * 40)
        print('-' * 10, 'MENU CONSULTAR LIVRO', '-' * 8)
        print('1 - Consultar todos os livros')
        print('2 - Consultar livro por id')
        print('3 - consultar livro(s) por autor')
        print('4 - Retornar')
        print('-' * 20)

        op = input('>> ')

        # estrutura para verificar o input digitado pelo usuario, retornando uma das opçoes do menu de consulta
        # a estrutura se repete ate o usuario digitar 4 para voltar ao menu principal
        if op == '1':
           for livro in lista_livro:
                print(f'ID: {livro["id"]} \nNome: {livro["nome"]} \nAutor: {livro["autor"]} \nEditora: {livro["editora"]}\n')

        elif op == '2':
            
                consulta_id_livro = int(input('Digite o ID do livro: '))
                for livro in lista_livro:
                    if livro['id'] == consulta_id_livro:
                        print(f'ID: {livro["id"]} \nNome: {livro["nome"]} \nAutor: {livro["autor"]} \nEditora: {livro["editora"]}\n')
            
                
        elif op == '3':
            consulta_autor = input('Digite o autor dos(s) livro(s): ').lower()
            for livro in lista_livro:
                if livro['autor'].lower() == consulta_autor:
                    print(f'ID: {livro["id"]} \nNome: {livro["nome"]} \nAutor: {livro["autor"]} \nEditora: {livro["editora"]}\n')
        
        elif op == '4':
            break
        else:
            continue


def remover_livro():
    while True:
        print('-' * 40)
        print('-' * 10, 'MENU REMOVER LIVRO', '-' * 10)

        # verifica se foi digitado um numero pelo usuario e verifica se existe um id com o numero digitado na lista
        try:
            remover_livro_id = int(input('Digite o ID do livro que deseja remover: '))
        except ValueError:  
            continue

            # faz um loop no dicionario livro na lista de livros cadastrados, procura pelo id e remove, se repete o loop caso nao exista o id digitado
        for livro in lista_livro:
            if livro['id'] == remover_livro_id:
                lista_livro.remove(livro)                   
                print('Livro removido com sucesso!')
                return
        else:
            print('ID invalido')
    

# programa principal

print('Bem Vindo a Livraria do Bruno Fonseca')

while True:
 
    print('-' * 40)
    print('-' * 12, 'MENU PRINCIPAL', '-' * 12)
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s) ')
    print('3 - Remover Livro')
    print('4 - Retornar')

    menu = input('>> ')
    # estrutura que verifica o qual opçao o usuario escolhe, e retorna uma das opçoes do Menu principal
    if menu == '1':
        id_global += 1 # incrementa o id global em cada livro cadastrado
        cadastrar_livro(id_global)
    elif menu == '2':
        consultar_livro()
    elif menu == '3':
        remover_livro()
    elif menu == '4':
        print('ENCERRANDO')
        break
    else:
        print('Opção inválida. Tente novamente ')

