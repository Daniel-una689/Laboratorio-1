class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class simpleList:
    def __init__(self): #en este caso solo es self porque unicamente nos importa
        self.head  = None #tambien podemos decir que self es el primer nodo de la listaq
        self.tail = None #el tail es el ultimo nodo de la lista
        self.size = None #el tamaño de la lista es 0 porque no hay nodos

    def insert(self, valor):
        new_node = Node(valor)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        #notemos tambien que una lista avanza, por lo tanto, queremos insertar el nodo en el
        #ultimo lugar por lo tanto tenemos que hacer que el siguiente nodo de tail sea el nuevo nodo y que el tail sea el nuevo nodo

        #creamos un current el cual nos ayudara a recorrer la lista 

        current = self.head

        while (current.next):
            current = current.next
        current.next = new_node
        self.tail = new_node

    def display(self):
        current = self.head
        while (current):
            print(current.data, end=" ")
            current = current.next
        print("None")


    def queHace(self):
        if self.head is None: 
            print("La lista está vacía.")
            return

        #si el siguiente del head es none, significa que solo hay un nodo en la lista
        #por lo tanto eliminamos el nodo haciendo que el head sea none y retornamos
        if self.head.next is None:
            self.head = None 
            return
        
        #recorremos la lista hasta el penultimo nodo
        actual = self.head

        while actual.next.next is not None: #mientrs que el siguiente del siguiente actual no sea none, significa que aun hay nodos en la lista, por lo tanto avanzamos el actual al siguiente nodo 
            actual = actual.next

        actual.next = None #y lo ponemos en None para eliminar todo el contenido de la lista


#por lo tanto, lo que hace el codigo es una constante verificacion del codigo, en caso de encontrar
#un nodo que no sea none, lo elimina si es que el siguiente de este es NONE


def main():
    list = simpleList()
    list.insert(10)
    list.insert(20)
    list.insert(30)
    list.insert(40)
    list.display()
    print("\nAhora llamamos a queHace():")
    list.queHace()
    list.display()

if __name__ == "__main__":
    main()


    