from time import sleep
clientes = []
funcionarios = []
livros = []
id_cliente = 1
id_funcionario = 1
id_livro = 1

def cadastrar_cliente():
    global id_cliente
    clientName = input("Nome Completo: ")
    clientCpf = int(input("CPF: "))
    clientAdress = input("Endereço: ")
    clientNumber = int(input("Número de telefone: "))
    clientEmail = input("E-mail: ")
    clientBirth = int(input("Ano de Nascimento: "))
    
    cliente = {
        'ID': id_cliente,
        'Nome' : clientName, 
        'CPF' : clientCpf,
        'Endereço' : clientAdress,
        'Telefone' : clientNumber,
        'E-mail' : clientEmail,
        'Ano de Nascimento' : clientBirth
    }
    
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    sleep(2)
    
    id_cliente += 1
    
def cadastrar_funcionario():
    global id_funcionario
    print("---------- CADASTRO DE FUNCIONÁRIO ----------")
    print("INFORMAÇÕES PESSOAIS:")
    employeeName = input("Nome Completo: ")
    employeeCpf = int(input("CPF: "))
    employeeAdress = input("Endereço: ")
    employeeNumber = int(input("Número de telefone: "))
    employeeGender = input("Gênero [F/M]: ")
    employeeBirth = int(input("Ano de Nascimento: "))
    print("INFORMAÇÕES DE TRABALHO")
    employeeRole = input("Cargo: ")
    employeeSalary = float(input("Salário: R$"))
    
    funcionario = {
        'ID' : id_funcionario,
        'Nome' : employeeName,
        'CPF' : employeeCpf,
        'Endereço' : employeeAdress,
        'Telefone' : employeeNumber,
        'Gênero' : employeeGender,
        'Ano de Nascimento' : employeeBirth,
        'Cargo' : employeeRole,
        'Salário' : employeeSalary
    }
    
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")
    sleep(2)
    
    id_funcionario += 1

def cadastrar_livro():
    global id_livro
    print("---------- CADASTRO DE LIVRO ----------")
    bookTitle = input("Título do Livro: ")
    bookAuthor = input("Autor do Livro: ")
    bookIsbn = int(input("ISBN: "))
    bookEditor = input("Editora: ")
    bookGender = input("Gênero: ")
    bookPrice = float(input("Valor: R$"))
    bookQuantity = int(input("Quantidade em estoque: "))
    
    livro = {
        'ID' : id_livro,
        'Título' : bookTitle,
        'Autor' : bookAuthor,
        'ISBN' : bookIsbn,
        'Editora' : bookEditor,
        'Gênero' : bookGender,
        'Preço' : bookPrice,
        'Quantidade' : bookQuantity
    }
    
    livros.append(livro)
    print("Livro cadastrado com sucesso!")
    sleep(2)
    
    id_livro += 1

def menu_cadastro():                 
    while True:
        print('''---------- LIVRARIA INDIGO ----------
        CADASTRO
        [1] CLIENTE
        [2] FUNCIONÁRIO
        [3] LIVRO
        [4] VOLTAR''')
        opcao = int(input("SELECIONE UMA OPÇÃO: "))
        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            cadastrar_funcionario()
        elif opcao == 3:
            cadastrar_livro()
        elif opcao == 4:
            import menu
            break
        else:
            print("Opção inválida. Tente novamente!")
            sleep(1)
            print('=-=' * 10)