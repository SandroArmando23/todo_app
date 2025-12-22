from modules.functions import get_todos, write_todos
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])   # Layout vuole una lista. All'interno della lista scriviamo altre liste e ognuna corrisponde a una riga nella finestra
window.read()
window.close()