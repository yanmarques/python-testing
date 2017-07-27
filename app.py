import lib
import os
from db import DataBase

def menu():
    db = DataBase()
    escolha = ''

    while(escolha != '0'):
        print 'Digite 1 para cadastrar | 2 para listar usuarios | 3 para alterar o nome do usuario | 0 para terminar'
        escolha = raw_input()

        # Cadastra usuario
        if (escolha == '1'):
            lib.store(db)

        # Retorna todos os usuarios
        if (escolha == '2'):
            lib.show_all(db)

        # Altera o nome do usuario
        if (escolha == '3'):
            lib.alter_user(db)

        # Comando clear do terminal para limpar campo de texto    
        if (escolha == 'clear'):
            os.system('clear')

    print '\n'
    print 'Ate logo ...'

menu()
