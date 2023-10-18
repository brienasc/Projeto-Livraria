from cadastro import clientes, funcionarios, livros
from time import sleep

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        print('=-=' * 10)
        sleep(2)
    else:
        for i, cliente in enumerate(clientes):
            print("Cliente {}: ".format(i + 1))
            print("ID: ", cliente['ID'])
            print("Nome: ", cliente['Nome'])
            print("CPF: ", cliente['CPF'])
            print("Endereço: ", cliente['Endereço'])
            print("Telefone: ", cliente['Telefone'])
            print("E-mail: ", cliente['E-mail'])
            print("Ano de Nascimento: ", cliente['Ano de Nascimento'])
            print('=-=' * 10)
            
def listar_funcionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        print('=-=' * 10)
        sleep(2)
    else:
        for i, funcionario in enumerate(funcionarios):
            print("ID: ", funcionario['ID'])
            print("Nome: ", funcionario['Nome'])
            print("CPF: ", funcionario['CPF'])
            print("Endereço: ", funcionario['Endereço'])
            print("Telefone: ", funcionario['Telefone'])
            print("Gênero: ", funcionario['Gênero'])
            print("Ano de Nascimento: ", funcionario['Ano de Nascimento'])
            print("Cargo: ", funcionario['Cargo'])
            print("Salário: R$", funcionario['Salário'])
    
def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        print('=-=' * 10)
        sleep(2)
    else:
        for i, livro in enumerate(livros):
            print("ID; ", livro['ID'])
            print("Título: ", livro['Título'])
            print("Autor: ", livro['Autor'])
            print("ISBN: ", livro['ISBN'])
            print("Editora: ", livro['Editora'])
            print("Gênero: ", livro['Gênero'])
            print("Preço: R$", livro['Preço'])
            print("Quantidade em estoque: ", livro['Quantidade'])            

def menu_exibir():
    while True:
        print('''---------- LIVRARIA INDIGO ----------
                EXIBIR
        [1] CLIENTE
        [2] FUNCIONÁRIO
        [3] LIVRO
        [4] VOLTAR''')
        opcao = int(input("SELECIONE UMA OPÇÃO: "))
        if opcao == 1:
            listar_clientes()
        elif opcao == 2:
            listar_funcionarios()
        elif opcao == 3:
            listar_livros()
        elif opcao == 4:
            import menu
            break
        else:
            print("Opção inválida. Tente novamente!")
            sleep(1)
            print('=-=' * 10)
        