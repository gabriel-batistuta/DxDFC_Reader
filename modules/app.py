import inquirer

def menu():
    options = [
        inquirer.List('option',
        message='Qual o formato de arquivo deseja?',
        choices=['.pdf', '.txt', 'Sair'])
    ]

    response = inquirer.prompt(options)

    elif response['option'] == '.pdf':
        resp = 'pdf'

    if response['option'] == '.txt':
        resp = 'txt'
        
    elif response['option'] == 'Sair':
        quit()

    return resp