from time import sleep
dados_de_login = {}

def cadastrar_login():
    usuario = input("Digite um login: ")
    senha = input("Digite uma senha: ")
    dados_de_login[usuario] = senha
    print("Cadastrado com sucesso!")
    print('=-=' * 10)
    sleep(1)

def fazer_login():
    usuario = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if usuario in dados_de_login and dados_de_login[usuario] == senha:
        print('=-=' * 10)
        sleep(1)
        import menu
    else:
        print("Login incorreto. Tente novamente!")
        print('=-=' * 10)

while True:
    print('''---------- LIVRARIA INDIGO ----------
    [1] CADASTRAR
    [2] LOGIN
    [3] SAIR''')
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_login()
    elif opcao == "2":
        fazer_login()
    elif opcao == "3":
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida. Tente novamente.")
        print('=-=' * 10)
