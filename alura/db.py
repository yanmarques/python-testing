class DataBase():

    DB = []

    def __init__(self):
        return DB

    def all():
        if(len(DB) != 0):

            counter = 0
            print '\n'

            for iten in DB:

                counter += 1

                print 'Usuario %s' % (counter)
                print '\t%s' % iten['id']
                print '\t' + iten['name']
                print '\t%s' % (iten['age'])

                print '\n'
        else:
            print 'Nao ha nenhum usuario cadastrado'

    def store(self, user):
        itens = {'id' : user.id, 'name' : user.name, 'idade' : user.age}

        DB.append(itens)

    def alter_where_id(self, user_id, new_name):
        status = False

        for iten in DB:
            if(iten['id'] == user_id):
                iten['name'] = new_nome
                print 'Nome alterado com sucesso'
                status = True

        return status

    def findId(self, id):
            
