# -*- coding: UTF-8 -*-

from user import User
import lib
import re

# Cadastra o usuario
def store(db):
    validate, name, email, date = False, False, False, False

    print ('Digite o seu nome')
    name = input()

    validate = False

    while not validate:
        print ('Digite o seu email')
        email = input()

        validate = lib.validate('email', email)

    validate = False

    while not validate:
        print ('Digite seu ano de nascimento')
        date = input()

        validate = lib.validate('date', date)

    # Nova instancia de User
    user = User(name, email, date)

    db.store(user)

# Altera o nome do usuario
def alter_user(db):

    user = False
    user_id = ''

    while (user == False):
        print ('Digite o id onde deseja alterar')
        user_id = input()

        user = db.findId(user_id)

    print ('Digite o novo nome')
    new_name = input()

    # Retorna uma instancia de User
    new_altered_user = db.alter_where_id(user_id, new_name)

    print ('\n')

    print ("Nome alterado para '%s'" % (new_altered_user.name))

# Mostra todos os usuarios
def show_all(db):
    print ('\n')

    users = db.all()

    if (users == None):
        print ('Nao ha nenhum usuario cadastrado')
    else:
        for user in users:
            print ('Usuario Id = %s' % (user.id))
            print ('\t Email = %s' % (user.email))
            print ('\t Nome = %s' % (user.name))
            print ('\t Idade = %s' % (user.age))

    print ('\n')
