from datetime import date

class User():
    ANO_ATUAL = date.today().year
    ID = 0;

    def __init__(self, nome, ano):
        self.nome = nome
        self.idade = ANO_ATUAL - int(ano)

        usuario_id = ID + 1

        self.id = usuario_id
    
