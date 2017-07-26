# -*- coding: UTF-8 -*-

from user import User

def store(db):
    print 'Digite o seu nome'
    name = raw_input()

    print 'Digite sua data de nascimento'
    date = raw_input()

    user = User.store(name, date)

    db.store(user)

def alter_user(db):
    print 'Digite o id onde deseja alterar'
    user_id = raw_input()

    db.alter_where_id()

    if (status == True):
        return "'%s' foi mudado para '%s'" % (name, new_nome)
    else:
        return "Nada foi encontrado com o nome '%s'" % (name)

    print 'Digite o novo nome'
    new_name = raw_input()

    print '\n'

def listar_nomes(db):



def get_ultimo_id(lista):

    usuario_id = 0

    for item in lista:
        if (item['id'] > usuario_id):
            usuario_id = item
