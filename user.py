from datetime import date

class User():
    # Data atual
    global ANO_ATUAL
    ANO_ATUAL = date.today().year

    # Id
    global ID
    ID = 0;

    # Cria uma nova instancia de User
    # params string name
    # params string age
    # params int user_id default None
    def __init__(self, name, age, user_id = None):
        global ID

        if(user_id == None):
            ID += 1
            self.id = ID

            self.name = name
            self.age = ANO_ATUAL - int(age)
        else:
            self.id = user_id
            self.name = name
            self.age = age
