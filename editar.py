from cadastro import clientes, funcionarios, livros
from exibir import listar_clientes, listar_funcionarios, listar_livros
from time import sleep

def editar_cliente():
    if not clientes:
        print("Nenhum cliente cadastrado para edição.")
    else:
        listar_clientes()
        id_cliente = int(input("Digite o ID do cliente que deseja editar: "))
        for cliente in clientes:
            if cliente['ID'] == id_cliente:
                print("O que deseja editar para o cliente {}?".format(id_cliente))
                print("[1] Nome")
                print("[2] CPF")
                print("[3] Endereço")
                print("[4] Telefone")
                print("[5] E-mail")
                print("[6] Ano de Nascimento")
                opcao = int(input("Selecione a opção: "))
                if opcao == 1:
                    cliente['Nome'] = input("Novo Nome: ")
                elif opcao == 2:
                    cliente['CPF'] = int(input("Novo CPF: "))
                elif opcao == 3:
                    cliente['Endereço'] = input("Novo Endereço: ")
                elif opcao == 4:
                    cliente['Telefone'] = input("Novo Telefone: ")
                elif opcao == 5:
                    cliente['E-mail'] = input("Novo E-mail: ")
                elif opcao == 6:
                    cliente['Ano de Nascimento'] = int(input("Novo Ano de Nascimento: "))
                else:
                    print("Opção incorreta. Tente novamente!")
                    sleep(1)
                    print('=-=' * 10)
                    return
                print("Cliente {} editado com sucesso.".format(id_cliente))
                sleep(2)
                return
        print("Cliente com o ID {} não encontrado.".format(id_cliente))

def editar_funcionario():
    if not funcionarios:
        print("Nenhum funcionário cadastrado para edição.")
    else:
        listar_funcionarios()
        id_funcionario = int(input("Digite o ID do funcionário que deseja editar: "))
        for funcionario in funcionarios:
            if funcionario['ID'] == id_funcionario:
                print("O que deseja editar para o funcionário {}?".format(id_funcionario))
                print("[1] Nome")
                print("[2] CPF")
                print("[3] Endereço")
                print("[4] Telefone")
                print("[5] Gênero")
                print("[6] Ano de Nascimento")
                print("[7] Cargo")
                print("[8] Salário")
                opcao = int(input("Selecione a opção: "))
                if opcao == 1:
                    funcionario['Nome'] = input("Novo Nome: ")
                elif opcao == 2:
                    funcionario['CPF'] = int(input("Novo CPF: "))
                elif opcao == 3:
                    funcionario['Endereço'] = input("Novo Endereço: ")
                elif opcao == 4:
                    funcionario['Telefone'] = int(input("Novo Telefone: "))
                elif opcao == 5:
                    funcionario['Gênero'] = input("Novo Gênero: ")
                elif opcao == 6:
                    funcionario['Ano de Nascimento'] = int(input("Novo Ano de Nascimento: "))
                elif opcao == 7:
                    funcionario['Cargo'] = input("Novo Cargo: ")
                elif opcao == 8:
                    funcionario['Salário'] = int(input("Novo Salário: "))
                else:
                    print("Opção incorreta. Tente novamente!")
                    sleep(1)
                    print('=-=' * 10)
                    return
                print("Funcionário {} editado com sucesso.".format(id_funcionario))
                sleep(2)
                return
        print("Funcionário com o ID {} não encontrado.".format(id_funcionario))

def editar_livro():
    if not livros:
        print("Nenhum livro cadastrado para edição.")
    else:
        listar_livros()
        id_livro = int(input("Digite o ID do livro que deseja editar: "))
        for livro in livros:
            if livro['ID'] == id_livro:
                print("O que deseja editar para o livro {}?".format(id_livro))
                print("[1] Título")
                print("[2] Autor")
                print("[3] ISBN")
                print("[4] Editora")
                print("[5] Gênero")
                print("[6] Preço")
                print("[7] Quantidade em Estoque")
                opcao = int(input("Selecione a opção: "))
                if opcao == 1:
                    livro['Título'] = input("Novo Título: ")
                elif opcao == 2:
                    livro['Autor'] = input("Novo Autor: ")
                elif opcao == 3:
                    livro['ISBN'] = input("Novo ISBN: ")
                elif opcao == 4:
                    livro['Editora'] = input("Novo Editora: ")
                elif opcao == 5:
                    livro['Gênero'] = input("Novo Gênero: ")
                elif opcao == 6:
                    livro['Preço'] = input("Novo Preço: ")
                elif opcao == 7:
                    livro['Quantidade'] = input("Nova Quantidade em Estoque: ")
                else:
                    print("Opção incorreta. Tente novamente!")
                    sleep(1)
                    print('=-=' * 10)
                    return    
                print("Livro {} editado com sucesso.".format(id_livro))
                sleep(2)
                return
        print("Livro com o ID {} não encontrado.".format(id_livro))

def menu_editar():
    while True:
        print('''---------- LIVRARIA INDIGO ----------
        EDITAR
    [1] CLIENTE
    [2] FUNCIONÁRIO
    [3] LIVRO
    [4] VOLTAR''')
        opcao = int(input("SELECIONE UMA OPÇÃO: "))
        if opcao == 1:
            editar_cliente()
        elif opcao == 2:
            editar_funcionario()
        elif opcao == 3:
            editar_livro()
        elif opcao == 4:
            import menu
            break
        else:
            print("Opção inválida. Tente novamente!")
            sleep(1)
            print('=-=' * 10)
