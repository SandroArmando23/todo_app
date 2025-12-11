from modules.functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
   user_action = input("Type add, show, edit, complete or exit: ")
   user_action = user_action.strip()  #   in caso di spazi dopo la string strip lo elimina

   if user_action.startswith('add') :
       #todo = input("Enter a todo: ") + "\n" aggiungiamo \n per andare a capo nel txt file
       todo = user_action[4:] #significa ciò che viene scritto nell'input di user action, ma a partire dal 5 carattere in poi cosi escludiamo la parola add e lo spazio
       # file = open('todos.txt', 'r') # legge il file txt
       # todos = file.readline() # qui creiamo una lista dove la funzione readline trasforma ogni riga del file in un elemento della lista
       # file.close()
       #riscriviamo le ultime righe sopra con with. Non necessitiamo piu di chiudere il file
       todos = get_todos()  #qui il parametro diventa argomento ed è come se fosse (filepath="todos.txt")



       #da qui in poi aggiunge invece il nuovo input e lo aggiunge alla lista senza sovrascrivere
       todos.append(todo + '\n')


       #file = open('todos.txt', 'w')  #open crea un file object. 'w' sta x write
       #file.writelines(todos)  #writelines è una funzione degli oggetti che accetta una list6a come argomento
       #file.close()
       # usiamo writelines perchè vogliamo una lista. ma se volessimo inserire del testo nel file allora file.write()

       write_todos(todos, "todos.txt") #potremmo anche non riportare il path perche dichiarato come default

   elif user_action.startswith('show'):
        #file = open('todos.txt', 'r')
        #todos = file.readlines() #occhio, scrivendo readline senza s finale legge i caratteri uno x uno invece delle parole
        #file.close()

        todos = get_todos()


        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)   #il new_item viene aggiunto alla lista new_todos
        # è possibile riassumere le righe da 26 a 30 così:
        # new_todos = [item.strip('\n') for item in todos]


        for index, item in enumerate(new_todos): #enumerate accetta una lista(todos) come attributo.
            item = item.title() #converte il primo carattere di ogni parola in maiuscolo
            row = f"{index + 1}-{item}"#fa partire l'index da 1 e non da 0
            print(row)
        # stampando direttamente la row si ottiene una doppia spaziatura fra ler righe in console, questo perche sopra avevamo aggiu8nto \n per mandare a capo gli elementi nel file txt
        # ma il ciclo anche lui di natura manda a capo, quindi la soluzione è creare unanuova variabile new_items che corrisponde a item.strip(\n) in modo da eliminare \n che avevamo aggiunto



   elif user_action.startswith('edit'):
       try:
           #number = int(input("Number of todo to edit: ")) #int()converte l'input da string a intero
           number = int(user_action[5:])
           print(number)

           number = number -1  #rendiamo 1 invece di 0 il primo elemento della lista

           todos = get_todos()

           new_todo = input("Enter new todo: ")
           todos[number] = new_todo + '\n'

           write_todos(todos, "todos.txt")
       except ValueError:    #inseriamo il blocco try con except nel caso l'utente inserisca una stringa nel'edit invece che il numero del todo da editare
           print("Your command is not valid.")
           continue
   elif user_action.startswith('complete'):
       try:
           number = int(user_action[9:])

           todos = get_todos()

           index = number -1        #creiamo nuova variabile da inserire poi nel messaggio che ci dirà quale todo abbiamo completato
           todo_to_remove = todos[index].strip('\n')

           todos.pop(index)

           write_todos(todos, "todos.txt")

           message = f"Todo: {todo_to_remove}, was removed from the list."
           print(message)
       except IndexError:
           print("There is no item with that number.")
           continue

   elif user_action.startswith('exit'):
       break
   else:
       print("Command is not valid!")

print("Bye")
