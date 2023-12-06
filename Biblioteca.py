import json
import time
import main
import sys

BiblioteList = []

# Método para adicionar um novo livro a biblioteca
def newLivro(pTitulo, pAutor, pGenero, pDescricao):
    global BiblioteList
    #pTitulo = []
    #pAutor = []
    #pGenero = []
    #pDescricao = []
    newList = {'Titulo': pTitulo, 'Autor': pAutor, 'Genero': pGenero, 'Descricao': pDescricao}
    BiblioteList.append(newList)

def removeLivro(nome_lista):
    global BiblioteList
    BiblioteList = [profile for profile in BiblioteList if profile['Titulo'] != nome_lista]


# Função para printar os dados de um livro

def printarLivro(numero):

    if numero == '1':
        nomeTitulo = input("Digite o Titulo do livro:")
        for c in BiblioteList:
            if c['Titulo'] == nomeTitulo:
                print("Livro encontrado:" + nomeTitulo)
                print("Autor do Livro: " + c['Autor'])
                print("Gênero do Livro: " + c['Genero'])
                #print("Status do livro: Atualmente em uso.")
                break
    elif numero == '2':
        nomeAutor = input("Digite o nome do autor:")
        for c in BiblioteList:
            if c['Autor'] == nomeAutor:
                print("Livro encontrado:" + c['Titulo'])
                print("Autor do Livro: " + c['Autor'])
                print("Gênero do Livro: " + c['Genero'])
                #print("Status do livro: Atualmente em uso.")
                break
    elif numero == '3':
        nomeGenero = input("Digite o Genero do livro:")
        for c in BiblioteList:
            if c['Genero'] == nomeGenero:
                print("Livro encontrado:" + c['Titulo'])
                print("Autor do Livro: " + c['Autor'])
                print("Gênero do Livro: " + c['Genero'])
                #print("Status do livro: Atualmente em uso.")
                break


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


        if action == 'c':
            time.sleep(0.5)
            print("Bem vindo ao Catálogo de Livros")
            print()
            print("Escolha uma opção de pesquisa:")
            print("1 - Titulo do Livro")
            print("2 - Autor do Livro")
            print("3 - Genero do livro")

            action = input("O que você quer fazer?")
            action = action.lower()
            action = action[0]

            printarLivro(action)


        if action == 'a':
            time.sleep(0.5)
            print('Nova Livro: ')
            tituloLivro = input('Qual o Titulo do livro? ')
            for a in BiblioteList:
                if a['Titulo'] == tituloLivro:
                    print("Esse livro já foi adicionado, tente novamente")
                    break
            else:
                autorLivro = input("Qual o autor do livro? ")
                generoLivro = input("Qual o gênero do livro? ")
                descricaoLivro = input("Descreva uma breve descrição sobre o livro: ")
                for c in BiblioteList:
                    if c['Descricao'] == descricaoLivro:
                        print("Essa descrição já existe. Tente novamente.")
                        break
                else:
                    newLivro(tituloLivro, autorLivro, generoLivro, descricaoLivro)
                    print("LivroAdicionado")
        

        elif action == 'b':
            time.sleep(0.5)
            print('Exclusão de livro:')
            tituloLivro = input('Insira o Titulo do livro: ')
            remover_livros = []
            for a in BiblioteList:
                if a['Titulo'] == tituloLivro:
                    remover_livros.append(a['Titulo'])
                    BiblioteList.remove(a)
                    removeLivro(a['Titulo'])
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



    




