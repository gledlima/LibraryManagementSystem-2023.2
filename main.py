import time
import Biblioteca
import sys

def menu():
    print()
    print("-------- Menu ----------")
    print('Pressione A para pesquisar algum Livro')
    print('Pressione B para acessar a seção de xxxxxxx')
    print('Pressione C para acessar a seção de xxxxxxxx')
    print('Pressione X para sair')
    print()
    
    action = input('O que você deseja fazer? ')
    action = action.lower()
    action = action[0]
    
    if action == 'a':
        time.sleep(0.5)
        print()
        print()
        print('BEM VINDO AO REPOSITÓRIO GERAL DE LIVROS')
        Biblioteca.operations()
    
    elif action == 'x':
        print("Programa Fechado!")
        sys.exit()

    else:
        print("Opção invalida, tente novamente.")

if __name__ == '__main__':
    menu()

        
        
    
    