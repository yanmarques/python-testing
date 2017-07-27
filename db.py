from user import User

class DataBase():

    # Lista onde ficarao armazenado os usuarios
    global DB
    DB = []

    def __init__(self):
        self.table = DB

    # Retorna uma lista com instancia de cada usuario
    def all(self):
        global DB

        if(len(DB) != 0):
            users = []

            for iten in DB:
                users.append(User(iten['name'], iten['age'], iten['id']))

            return users
        else:
            return None

    # Cadastra um usuario
    # params User user
    def store(self, user):
        itens = {'id' : user.id, 'name' : user.name, 'age' : user.age}

        DB.append(itens)

    # Altera o nome de um usuario, e retorna uma instancia do Usuario se o id for encontrado
    # Retorna nulo se aconteceu um erro, ou nao encontrou o id informado
    # params string id do usuario
    def alter_where_id(self, user_id, new_name):
        find_user_id = self.findId(int(user_id))

        user = None

        if (find_user_id != False):
            for iten in DB:
                if(iten['id'] == find_user_id['id']):
                    iten['name'] = new_name
                    user = User(iten['name'], iten['age'], iten['id'])

        return user

    # Busca pelo id do usuario, retornando um directionary com os dados do usuario
    # retorna false se nao encontra o id informado
    def findId(self, user_id):
        global DB

        for iten in DB:
            if(iten['id'] == int(user_id)):
                return iten

        return False
