# -*- coding: UTF-8 -*-

from user import User

# Cadastra o usuario
def store(db):
    print 'Digite o seu nome'
    name = raw_input()

    print 'Digite sua data de nascimento'
    date = raw_input()

    # Nova instancia de User
    user = User(name, date)

    db.store(user)

# Altera o nome do usuario
def alter_user(db):

    user = False
    user_id = ''

    while (user == False):
        print 'Digite o id onde deseja alterar'
        user_id = raw_input()

        user = db.findId(user_id)

    print 'Digite o novo nome'
    new_name = raw_input()

    # Retorna uma instancia de User
    new_altered_user = db.alter_where_id(user_id, new_name)

    print '\n'

    print "Nome alterado para '%s'" % (new_altered_user.name)

# Mostra todos os usuarios
def show_all(db):
    print '\n'

    users = db.all()

    if (users == None):
        print 'Nao ha nenhum usuario cadastrado'
    else:
        for user in users:
            print 'Usuario Id = %s' % (user.id)
            print '\t Nome = %s' % (user.name)
            print '\t Idade = %s' % (user.age)

    print '\n'
