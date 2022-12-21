import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

label_relogio = sg.Text('', key="relogio")
label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))

edit_button = sg.Button("Edit")
complete_button = sg.Button("Apagar")
exit_button = sg.Button("Sair")




window = sg.Window('My TO-DO app',
                   layout=[[label_relogio],
                            [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event,values = window.read(timeout=200)
    window["relogio"].update(value=time.strftime("%d %b , %Y %H:%M:%S"))

    match event:
        case "Add":
            try:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                print("Por favor selecione um item primeiro.")

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Por favor selecione um item primeiro.", font=('Helvetica', 20))

        case "Apagar":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(vaslues=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Por favor selecione um item primeiro.", font=('Helvetica', 20))

        case "Sair":
            break


        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()



