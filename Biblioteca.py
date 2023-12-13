import json
import time
import main
import sys
import usuario
from datetime import datetime

BiblioteList = []
livrosEmprestados = []
livrosDisponiveis = []
quempegou = []

# Método para adicionar um novo livro a biblioteca
def newLivro(pTitulo, pAutor, pGenero, pAno, pDescricao, pDisponivel, pEmprestado, pReservado, pQuemReservou):
    global BiblioteList
    #pTitulo = []
    #pAutor = []
    #pGenero = []
    #pDescricao = []
    newList = {'Titulo': pTitulo, 'Autor': pAutor, 'Genero': pGenero, 'Ano': pAno, 'Descricao': pDescricao, 'Disponivel': pDisponivel, 'UsuarioEmprestado': pEmprestado, 'DisponivelReserva': pReservado, 'QuemReservou': pQuemReservou}
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


#Função para pegar um livro

def PrintarlivrosDisponiveis():
        global livrosDisponiveis
        global BiblioteList
        global quempegou

        nAccounts = len(BiblioteList)
        for c in range(nAccounts):
            if BiblioteList[c]['Disponivel'] == True:
                print()
                print("Lista de livros disponiveis para emprestimo: ")
                print()
                print(str(c))
                print("Livro encontrado: " + BiblioteList[c]['Titulo'])
                #print("Status do livro: Atualmente em uso.")
                print()
                livrosDisponiveis.append(BiblioteList[c]) # printar livros disponiveis no mercado!
                resul = True
            else:
                print("Nenhum livro está disponivel para emprestimo!")
                resul = False
        
        return resul
            


def pegarEmprestado(titulo, email):
        
        global livrosDisponiveis
        global BiblioteList
        
        nAccount = len(livrosDisponiveis)
        nAccounts2 = len(BiblioteList)
        for j in range(nAccount):
            if livrosDisponiveis[j]['Titulo'] == titulo and livrosDisponiveis[j]['Disponivel'] == True:
                for b in range(nAccounts2):
                    if livrosDisponiveis[j]['Titulo'] == BiblioteList[b]['Titulo']:
                        BiblioteList[b]['Disponivel'] = False
                        print()
                        print("Parabens. Você acabou de pegar um livro emprestado!")
                        print()
                        # usuario.adicionarLivro(BiblioteList[b]['Titulo'], email) # chama a função em usuario para adicionar um novo livro
                        BiblioteList[b]['UsuarioEmprestado'].append(email)
                    else:
                        print("Esse livro está indisponivel ou já foi emprestado.")
            else:
                print("Titulo incorrento. Tente novamente!")
            

# função para printar inventario

def inventario():
        global livrosDisponiveis
        global BiblioteList
        global quempegou

        nAccounts = len(BiblioteList)

        print("BEM VINDO AO INVENTARIO DA BIBLIOTECA.")
        print()
        print("ATUALMENTE TEMOS " + str(nAccounts) + " LIVROS NO INVENTÁRIO")

        for c in range(nAccounts):
            if BiblioteList[c]['Disponivel'] == True:
                print()
                print(str(c))
                print("Livro encontrado: " + BiblioteList[c]['Titulo'])
                print("Autor do Livro: " + BiblioteList[c]['Autor'])
                print("Gênero do Livro: " + BiblioteList[c]['Genero'])
                print("Ano de publicação: " + BiblioteList[c]['Ano'])
                print()
                #livrosDisponiveis.append(BiblioteList[c]) # printar livros disponiveis no mercado!



# Função para reservar livro

def reservarLivro():
    
    print()
    print("Lista de livros disponiveis para reserva: ")
    print()
    nAccounts = len(BiblioteList)
    for m in range(nAccounts):
        if BiblioteList[m]['Disponivel'] == False:
            print()
            print("Livro encontrado: " + BiblioteList[m]['Titulo'])
            #print("Status do livro: Atualmente em uso.")
            print()
            resul = True
        else:
            print("Todos os livros estão disponiveis para emprestimo!")
            resul = False
    
    return resul

def reservar(titulo, email):

    global BiblioteList
        
    nAccount = len(BiblioteList)
    for j in range(nAccount):
        if BiblioteList[j]['Titulo'] == titulo and BiblioteList[j]['DisponivelReserva'] == True:
            BiblioteList[j]['DisponivelReserva'] = False
            BiblioteList[j]['QuemReservou'] = email
            print()
            print("Parabens. Você acabou reservar um livro que está em uso!")
            print()
                # usuario.adicionarLivro(BiblioteList[b]['Titulo'], email) # chama a função em usuario para adicionar um novo livro
                

    



# funções para devolver livro

def devolverLivro(email):
    global BiblioteList
    global quempegou

    nome = input("Digite o nome do livro que você quer devolver: ")

    nAccount = len(BiblioteList)
    for j in range(nAccount):
        if BiblioteList[j]['Titulo'] == nome and BiblioteList[j]['Disponivel'] == False:
            if email in BiblioteList[j]['UsuarioEmprestado']:
                BiblioteList[j]['UsuarioEmprestado'].remove(email)
                BiblioteList[j]['Disponivel'] = True
                print()
                print("Livro demovido com sucesso!")
            else:
                print("Você não pegou esse livro emprestado!")
        else:
            print("Digite o nome correto do livro!")



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



def operations(email):
    while True:

        global BiblioteList
        global quempegou

        BiblioteList = loadFromJSON('Biblioteca.json')
    
        print()
        print("BEM VINDO AO REPOSITÓRIO CENTRAL")
        print()
        print("Pressione C para consultar um repositório da biblioteca: ")
        print("Pressione A para adicionar um livro ao repositório da biblioteca: ")
        print("Pressione B para excluir um livro do repositório da biblioteca: ")
        print("Pressione E para pegar emprestado um livro do repositório: ")
        print("Pressione R para reservar um livro do repositório da biblioteca: ")
        print("Pressione D para devolver um livro: ")
        print("Pressione I para visualizar o inventario da biblioteca: ")
        print("Pressione Q para voltar ao menu principal: ")
        print("Pressione X para fechar ")
        print()

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
                
                disponivel = True
                reservado = True
                quemreservou = "ninguem"
                #quempegouemprestado = "ninguem"
                horadecadastro = datetime.now()
                ano = input("Digite o ano da publicação do livro: ")
                descricaoLivro = input("Descreva uma breve descrição sobre o livro: ")
                for c in BiblioteList:
                    if c['Descricao'] == descricaoLivro:
                        print("Essa descrição já existe. Tente novamente.")
                        break
                else:
                    newLivro(tituloLivro, autorLivro, generoLivro, ano, descricaoLivro, disponivel, quempegou, reservado, quemreservou)
                    print()
                    print("Livro Adicionado com Sucesso!")
                    print()
        

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
        
        elif action == "e":
            resul = PrintarlivrosDisponiveis()
            print()
            if resul == True:
                nomeLivro = input("Digite o nome do livro que você quer emprestado: ")
                pegarEmprestado(nomeLivro, email)
        

        elif action == "d": # função para devolver livro
            devolverLivro(email)

        elif action == "r":
            resul2 = reservarLivro()
            print()
            if resul2 == True:
                nomeLivro = input("Digite o nome do livro que você quer emprestado: ")
                reservar(nomeLivro, email)

        elif action == "i":
            inventario()

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



    




