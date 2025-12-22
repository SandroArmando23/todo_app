from modules import functions
from modules.functions import get_todos, write_todos
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")    # la key di default è 0
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button =sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
"""
Layout vuole una lista. All'interno della lista scriviamo altre liste e ognuna 
corrisponde a una riga nella finestra. poi aggiungiamo font e si va a capo un po come in css
"""
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Segoe UI', 20))  # Tupla con due valori

while True:
    event, values = window.read(timeout=200)      # possiamo assegnare due variabili insieme a una tupla o una lista che abbia lo stesso numero di items quante le variabili var1 = Arg1  var2=arg2
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)    # stampa 'Add' del button che è la label dell'event
    print(2, values)   # stampa {'to-do': 'Hi'}, con Hi intendiamo il testo scritto nell input txt box
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)   #scrive nella input in tempo reale cio che clicchiamo

            """
            In Edit se nell'interfaccia non clicchiamo su nessun todo e premiamo Edit ci restituisce un errore (IndexError) perciò aggiungiamo un try 
            ci permette di sapere dell'errore e con .popup() mostrare nell'interfaccia il messaggio che ci dice di premere su un elemento prima di editarlo
            stessa cosa faremo per complete
            """
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)      #aggiorna in tempo reale la lista nella finestra
            except IndexError:
                sg.popup("Pleas select an item first", font=('Segoe UI', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Pleas select an item first", font=('Segoe UI', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break   # quando chiudiamo la finestra il break ferma il while

window.close()