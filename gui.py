from modules import functions
from modules.functions import get_todos, write_todos
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")    # la key di default è 0
add_button = sg.Button("Add")

"""
Layout vuole una lista. All'interno della lista scriviamo altre liste e ognuna 
corrisponde a una riga nella finestra. poi aggiungiamo font e si va a capo un po come in css
"""
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Segoe UI', 20))  # Tupla con due valori

while True:
    event, values = window.read()      # possiamo assegnare due variabili insieme a una tupla o una lista che abbia lo stesso numero di items quante le variabili var1 = Arg1  var2=arg2
    print(event)    # stampa 'Add' del button che è la label dell'event
    print(values)   # stampa {'to-do': 'Hi'}, con Hi intendiamo il testo scritto nell Input txt box
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break   # quando chiudiamo la finestra il break ferma il while

window.close()