from time import sleep
from cadastro import *
from exibir import *
from editar import *
from excluir import *
opcao = 0

while opcao != 5:
    print('''---------- LIVRARIA INDIGO ----------
              BEM VINDO!
    [1] CADASTRAR
    [2] EXCLUIR
    [3] EDITAR
    [4] EXIBIR
    [5] SAIR''')
    opcao = int(input("SELECIONE UMA OPÇÃO: "))
    if opcao == 1:
        menu_cadastro()
    elif opcao == 2:
        menu_excluir()
    elif opcao == 3:
        menu_editar()
    elif opcao == 4:
        menu_exibir()
    elif opcao == 5:
        print("FINALIZANDO...")
    else:
        print("Opção inválida. Tente novamente!")
    print('=-=' * 10)
    sleep(2)
print('Deslogado com sucesso!')