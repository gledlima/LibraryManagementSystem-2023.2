import json
import time
import main
import sys

BiblioteList = []

# Método para adicionar um novo livro a biblioteca
def newLivro(pLivro, pDescrição):
    global BiblioteList
    pLivro = []
    pDescrição = []
    newList = {'name': pLivro, 'Descricao': pDescrição}
    BiblioteList.append(newList)

def removeLivro(nome_lista):
    global BiblioteList
    BiblioteList = [profile for profile in BiblioteList if profile['name'] != nome_lista]




#Metodos de manipulação de Json

def saveChanges(data, list):
    with open(data, "w") as file:
        json.dump(list, file, indent=2)

def loadFromJSON(archive):
    global BiblioteList
    try:
        with open(archive, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []
    return data

def operations():
    while True:
        global BiblioteList
        BiblioteList = loadFromJSON('Biblioteca.json')
    
        print()
        print("Pressione C para consultar um repositório da biblioteca")
        print("Pressione A para adicionar um livro ao repositório da biblioteca")
        print("Pressione B para excluir um livro do repositório da biblioteca")
        print("Pressione Q para voltar ao menu principal")
        print("Pressione X para fechar ")

        action = input("O que você quer fazer?")
        action = action.lower()
        action = action[0]
        print()

        if action == 'a':
            time.sleep(0.5)
            print('Nova Livro: ')
            nomeLivro = input('Qual o nome do livro? ')
            for a in BiblioteList:
                if a['name'] == nomeLivro:
                    print("Esse livro já foi adicionado, tente novamente")
                    break
            else:
                descrição = input("Qual será sua descrição? ")
                for c in BiblioteList:
                    if c['Descrição'] == descrição:
                        print("Essa descrição já existe. Tente novamente.")
                        break
                else:
                    newLivro(nomeLivro, descrição)
                    print("LivroAdicionado")
        
        elif action == 'b':
            time.sleep(0.5)
            print('Exclusão de livro:')
            nomeLivro = input('Insira o nome do livro: ')
            remover_livros = []
            for a in BiblioteList:
                if a['name'] == nomeLivro:
                    remover_livros.append(a['name'])
                    BiblioteList.remove(a)
                    removeLivro(a['name'])
                    print('Livro excluido com sucesso!')
                    break
            else:
                print('Credenciais inválidas. Não foi possível excluir o livro.')

        elif action == 'q':
                main.menu()
        
        elif action == 'x':
                time.sleep(0.5)
                print('Programa fechado!')
                sys.exit()
        
        time.sleep(0.5)
        saveChanges('biblioteca.json', BiblioteList)

if __name__ == '__main__':
    operations()



    




