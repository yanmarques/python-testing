import actions
import os
import crypt
import my_encrypt
from db import DataBase

def menu():
    db = DataBase()
    escolha = ''

    while(escolha != '0'):
        print ('Digite 1 para cadastrar | 2 para listar usuarios | 3 para alterar o nome do usuario')
        print ('4 para encriptar um texto | 5 para decriptar | 0 para terminar')

        escolha = input()

        # Cadastra usuario
        if (escolha == '1'):
            actions.store(db)

        # Retorna todos os usuarios
        if (escolha == '2'):
            actions.show_all(db)

        # Altera o nome do usuario
        if (escolha == '3'):
            actions.alter_user(db)

        if escolha == '4':
            text = input('Digite o texto que deseja encriptar > ')
            print ('Saida > ' + my_encrypt.crypt(text))

        if escolha == '5':
            text = input('Digite o texto encriptado que deseja decriptar > ')
            print ('Saida > ' + my_encrypt.decrypt(text))

        # Comando clear do terminal para limpar campo de texto
        if (escolha == 'clear'):
            os.system('clear')

    print ('\n')
    print ('Ate logo ...')

menu()
