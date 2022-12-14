#from functions import get_todos, write_todos

import functions

import time

now = time.strftime("%d %b , %Y %H:%M:%S")

print("Agora é", now)



while True:
    user_action = input("digite adicionar, mostrar, editar, remover ou sair: ")
    user_action = user_action.strip()

    if user_action.startswith('adicionar'):
        todo = user_action[10:]
                    
        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)


        
    elif user_action.startswith('mostrar'):
        
        todos = functions.get_todos()

       
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}->{item}")
        
    elif user_action.startswith('editar'):

        try:
            number = int(user_action[7:])
            print(number)

            number = number - 1  # usa indice iniciando do 1

            todos = functions.get_todos()
            
            print('Todos cadastrados', todos)


            novo_todo = input ("Corrige ou altere o todo: ")
            todos[number] = novo_todo + '\n'

            print('Como todo vai ficar', todos)

            functions.write_todos(todos)
        
        except ValueError:
            print("Comando inválido.")
            continue

        except IndexError:
            print("Não existe esse todo.")
            continue

    elif user_action.startswith('remover'):

        try:

            number = int(user_action[8:])
            #number = number - 1  # usa indice iniciando do 1

            
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            #   todos.pop(number-1)

            functions.write_todos(todos)

            Mensagem = f"Todo {todo_to_remove} foi removido da lista."
            print(Mensagem)
        
        except IndexError:
            print("Não existe todo com esse numero.")
            continue
        
        except ValueError:
            print("Comando inválido.")
            continue

    elif user_action.startswith('sair'):
            break
    else:
        print("Comando inválido..")

print('Bye!')
