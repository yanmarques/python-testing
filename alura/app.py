import lib
import os

def menu():
    lista = []
    escolha = ''

    while(escolha != '0'):
        print 'Digite 1 para cadastrar | 2 para listar usuarios | 3 para alterar o nome do usuario | 0 para terminar'
        escolha = raw_input()

        if (escolha == '1'):
            lib.cadastrar(lista)

        if (escolha == '2'):
            lib.listar_nomes(lista)

        if (escolha == '3'):
            lib.altera_usuario(lista)

        if (escolha == 'clear'):
            os.system('clear')

menu()
