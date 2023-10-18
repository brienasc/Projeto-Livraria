from cadastro import clientes, funcionarios, livros
from exibir import listar_clientes, listar_funcionarios, listar_livros
from time import sleep

def excluir_cliente():
    if not clientes:
        print("Nenhum cliente cadastrado para exclusão.")
    else:
        listar_clientes()
        id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
        for cliente in clientes:
            if cliente['ID'] == id_cliente:
                clientes.remove(cliente)
                print("Cliente {} excluído com sucesso.".format(id_cliente))
                sleep(2)
                return
        print("Cliente com o ID {} não encontrado.".format(id_cliente))

def excluir_funcionario():
    if not funcionarios:
        print("Nenhum funcionário cadastrado para exclusão.")
    else:
        listar_funcionarios()
        id_funcionario = int(input("Digite o ID do funcionário que deseja excluir: "))
        for funcionario in funcionarios:
            if funcionario['ID'] == id_funcionario:
                funcionarios.remove(funcionario)
                print("Funcionário {} excluído com sucesso.".format(id_funcionario))
                sleep(2)
                return
        print("Funcionário com o ID {} não encontrado.".format(id_funcionario))

def excluir_livro():
    if not livros:
        print("Nenhum livro cadastrado para exclusão.")
    else:
        listar_livros()
        id_livro = int(input("Digite o ID do livro que deseja excluir: "))
        for livro in livros:
            if livro['ID'] == id_livro:
                livros.remove(livro)
                print("Livro {} excluído com sucesso.".format(id_livro))
                sleep(2)
                return
        print("Livro com o ID {} não encontrado.".format(id_livro))

def menu_excluir():
    while True:
        print('''---------- LIVRARIA INDIGO ----------
        EXCLUIR
    [1] CLIENTE
    [2] FUNCIONÁRIO
    [3] LIVRO
    [4] VOLTAR''')
        opcao = int(input("SELECIONE UMA OPÇÃO: "))
        if opcao == 1:
            excluir_cliente()
        elif opcao == 2:
            excluir_funcionario()
        elif opcao == 3:
            excluir_livro()
        elif opcao == 4:
            import menu
            break
        else:
            print("Opção inválida. Tente novamente!")
            sleep(1)
            print('=-=' * 10)
