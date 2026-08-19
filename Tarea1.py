#Tarea 1
#Marcos Alvarado y Daniel Brenes

#creamos la clase del producto

#para la validacion del id
from unicodedata import name, numeric


class Product:
    def __init__(self, id, name, price, origin_contry, existence):
        self.id = id
        self.name = name
        self.price = price
        self.origin_contry = origin_contry
        self.existence = existence

    def subtotal(self):
        return self.price * self.existence

    def Productprint(self):
        print("ID: ", self.id)
        print("Nombre: ", self.name)
        print("Precio: ", self.price)
        print("Pais de origen: ", self.origin_contry)
        print("Existencia: ", self.existence)
        print("Subtotal: ", self.subtotal())





class NodeQueue:
        def __init__(self, valor: Product):
            self.valor = valor
            self.next = None

class Queue:
            def __init__(self):
                self.head = None
                self.tail = None
                self.size =0


            def is_empty(self):
                return self.size == 0

            def enqueue(self, producto: Product):
                new_node = NodeQueue(producto)
                if self.is_empty():
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node

                self.size += 1

                return ("Se agrego el producto a la cola")





class Node:
        #el valor que se pasa es un objeto de la clase Product
        def __init__(self, valor: Product):
            self.valor = valor
            self.next = None
            self.previous = None


class Linkedlist:
        #esta clase tendra los metodos para agregar, eliminar y mostrar los productos
        def __init__(self):
            self.head = None
            self.tail = None
            self.size =0


        def empty(self):
            return self.size == 0
    
        def agregarProducto(self, producto: Product):
            new_node = Node(producto)
            if self.empty():
                self.head = Node(producto) #basicamente en caso de que el nodo este vacio, se le asigna el valor del producto al nodo
                self.tail = self.head  

            else:
                new_node.next  = self.head
                self.head.anterior = new_node
                self.head = new_node

            self.size += 1


        def deletefirst(self):
            if self.empty():
                print("La lista esta vacia")
                return

            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.head.next = self.head
                self.head.previous = None
                self.size -= 1

                return ("se elimino el primer producto de la lista")

        def deletelast(self):
            if self.empty():
                print("La lista esta vacia")
                return

            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.tail = self.tail.previous
                self.tail.next = None
                self.size -= 1

                return ("se elimino el ultimo producto de la lista")


        def deleteProduct(self,id):
            if self.empty():
                print("La lista esta vacia")
                return


            if id is not numeric:
                print("El id debe ser un numero")
                return
            
            if self.head.valor.id == id:
                self.deletefist()
                return ("se elimino el primer producto de la lista")

            if self.tail.valor.id == id:
                self.deletelast()
                return ("se elimino el ultimo producto de la lista")

            current = self.head
            for i in range(self.size):
                if current.valor.id == id:
                    previous = current.previous
                    next = current.next

                    previous.next = next
                    next.previous = previous

                    self.size -= 1
                    return ("se elimino el producto con id: " + str(id))
                else:
                    current = current.next #ver si este ciclo esta bien integrado
                if current is None:
                     print("No se encontro el producto con id: " + str(id))
                return


            

        def search(self, id):
            if self.empty():
                print("La lista esta vacia")
                return

            if id is not numeric:
                print ("el numero de id debe de ser numerico")
                return


            current = self.head

            for i in range(self.size):
                if current.valor.id == id:
                    return current.valor
                else:
                    current = current.next

                if current is None:
                    print("No se encontro el producto con id: " + str(id))
                    return
                
        #en la clase del producto creamos un string el cual imprime el producto de manera ordenada y para hacer este metodo recursivo
        #hacemos que el mismo llame al mismo metodo de printRecursive para que le pase por parametro el nodo siguiente y asi sucesivamente hasta que llegue al final de la lista
        def printRecursive(self, node):
            if node is None:
                return
            else:
                node.valor.Productprint()
                self.printRecursive(node.next)

