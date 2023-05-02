import inquirer

def menu():
    options = [
        inquirer.List('option',
        message='Qual o formato de arquivo deseja?',
        choices=['.txt', '.pdf', 'Sair'])
    ]

    response = inquirer.prompt(options)

    if response['option'] == '.txt':
        resp = 'txt'
        
    elif response['option'] == '.pdf':
        resp = 'pdf'
        
    elif response['option'] == 'Sair':
        quit()

    return resp