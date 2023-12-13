import time
import sys
import usuario

def menu():
    print()
    print("-------- Menu ----------")
    print("Pressione L para fazer login no sistema da biblioteca")
    print('Pressione C para criar uma conta na biblioteca central')
    print("Pressione A para apagar um conta de usuário do sistema")
    print('Pressione X para sair')
    print()
    
    action = input('O que você deseja fazer? ')
    action = action.lower()
    #action = action[0]

    if action == 'l' or action == 'c' or action == 'a':
        usuario.login(action)
    
    elif action == 'x':
        print("Programa Fechado!")
        sys.exit()

    else:
        print("Opção invalida, tente novamente.")

if __name__ == '__main__':
    menu()

        
        
    
    