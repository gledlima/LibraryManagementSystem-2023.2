import Biblioteca
import main
import time
import json

usuariosList = []
#livrosAdquiridos = []

def novoUsuario(pNome, pUsername, pSenha, pEmail):
    global usuariosList
    #pTitulo = []
    #pAutor = []
    #pGenero = []
    #pDescricao = []
    novaLista = {'Nome': pNome, 'Senha': pSenha, 'Username': pUsername, 'Email': pEmail}
    usuariosList.append(novaLista)

def removeUsuario(usuario_lista):
    global usuariosList
    BiblioteList = [profile for profile in usuariosList if profile['Email'] != usuario_lista]


# Função para adicionar o nome do livro a lista dentro do dicionario

def adicionarLivro(livro, email):
    global usuariosList  # continue daqui
    nome = livro

    usuariosList = loadFromJSON('usuario.json')
    nAccounts = len(usuariosList)
    print("44444")
    for accountNumber in range(nAccounts):
        if usuariosList[accountNumber]['Email'] == email:
            usuariosList[accountNumber]['LivrosAdicionados'] += [livro]
            print(livro+email)
    
    saveChanges('usuario.json', usuariosList)
    


def loadFromJSON(archive):
    global usuariosList
    try:
        with open(archive, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []
    return data

def saveChanges(data, list):
    with open(data, "w") as file:
        json.dump(list, file, indent=2)



def login(action):
        
        while True:
            global usuariosList
            #global livrosAdquiridos

            usuariosList = loadFromJSON('usuario.json')

            print()

            if action == 'c':
                time.sleep(0.5)
                print('PÁGINA DE CADASTRO')
                nome = input("Digite seu nome: ")
                username = input("Digite seu username: ")
                for a in usuariosList:
                    if a['Username'] == username:
                        print("Username já está em uso! Tente novamente.")
                        #main.menu() # remover o main menu
                else:
                    senha = input("Digite sua senha: ")
                    email = input("Qual seu email: ")
                    for b in usuariosList:
                        if b['Email'] == email:
                            print("Esse email já está em uso. Tente novamente!")
                            #main.menu()
                    else:
                        novoUsuario(nome, username, senha, email)
                        print()
                        print("Usuario Criado com Sucesso!")
                        print()
                         # salva as informações no arquivo json
                        #main.menu()


            elif action == 'l':
                time.sleep(0.5)
                print()
                print()
                print('FAÇA LOGIN NA SUA CONTA')
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                nAccounts = len(usuariosList)
                account_found = False
                for accountNumber in range(nAccounts):
                    if usuariosList[accountNumber]['Email'] == email and usuariosList[accountNumber]['Senha'] == senha:
                        account_found = True
                        print()
                        print("Seja Bem vindo " + usuariosList[accountNumber]['Nome'])
                        print()
                        Biblioteca.operations(email)
                else:
                    if not account_found:
                        print()
                        print("Credenciais invalidas. Tente novamente!")
                        print()
            

            elif action == "a":
                time.sleep(0.5)
                print('Exclusão de usuário:')
                seuEmail = input('Insira o seu Email: ')
                remove_usuario = []
                for a in usuariosList:
                    if a['Email'] == seuEmail:
                        remove_usuario.append(a['Email'])
                        usuariosList.remove(a)
                        removeUsuario(a['Email'])
                        print('Usuário excluido com sucesso!')
                        break
                else:
                    print('Credenciais inválidas. Não foi possível excluir o usuário.')



            
            saveChanges('usuario.json', usuariosList)
            main.menu()
            #saveChanges('usuario.json', usuariosList) 


if __name__ == '__main__':
    login()