from validator import Validator

# Valida a data para ser apenas numeros
def validate(option, argument):
    validation = Validator().make(option, argument)

    if validation.has('errors'):
        print (validation.get('errors'))

    return validation.get('validation')
