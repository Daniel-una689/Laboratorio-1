#Tarea 1
#Marcos Alvarado y Daniel Brenes

#creamos la clase del producto

#para la validacion del id
#from unicodedata import name, numeric


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
            self.head.previous = new_node
            self.head = new_node

        self.size += 1


    def deletefirst(self):
        if self.empty():
            print("La lista esta vacia")
            return
        else:

            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next
                self.head.previous = None

            self.size -= 1

        return ("se elimino el primer producto de la lista")

    def deletelast(self):
        if self.empty():
            print("La lista esta vacia")
            return

        else:
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



        if not isinstance(id, (int, float)):
            print("El id debe ser un numero")
            return
        
            
        if self.head.valor.id == id:
            self.deletefirst()
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

        if not isinstance(id, (int, float)):
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


# debe recorrer la lista doblemente enlazada LinkedList, si producto.existence == 0, 
# se agrega a la cola usando el metodo enqueue de la clase Queue.

    def generarColaDeCompras(self):
        if self.empty():
            print("La lista está vacía")
            return
        else:
            # caso contrario, se recorre la lista y se agregan los productos con existencia 0 a la cola
            print("Generando cola de compras...")
            cola = Queue()
            current = self.head
            # recorremos la lista y agregamos los productos con existencia 0 a la cola
            while current is not None:
                if current.valor.existence == 0:
                    cola.enqueue(current.valor)
                    # aqui se agrega el producto a la cola
                current = current.next 
            return cola

    def generar_Rerporte(self):
        if self.empty():
            print("La lista de frecuencia está vacía")
            return
        else:
            with open("reporte.txt", "w") as archivo:
                archivo.write("-------Reporte de productos del supermercado---------\n")
                archivo.write("-----------------------------------------------------\n")
                total_general = 0
                current = self.head
                while current is not None:
                    subtotal= current.valor.subtotal()
                    archivo.write(f"Producto: {current.valor.name},id: {current.valor.id}, Subtotal: {subtotal}\n")
                    total_general += subtotal
                    current = current.next

                archivo.write(f"Total general: {total_general}\n")

class NodoFrecuencia:
    def __init__(self, pais):
        self.valor = pais
        self.next = None
        self.frequency = 1  # Inicializamos la frecuencia en 1 al crear un nuevo nodo
        # no se necesita un atributo previous ya que no se requiere recorrer hacia atrás en esta lista de frecuencia
        # ni size ya que no se necesita conocer la cantidad de elementos en la lista de frecuencia

class ListaFrecuencia:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        # se inicializa normal 

    def empty(self):
        return self.size == 0

    def agregarPais(self, pais): # ya que es un pais lo que se busca añadir 
        if self.empty():
            nuevo_nodo = NodoFrecuencia(pais)
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            # si la lista no está vacía, se recorre la lista para ver si el país ya existe
            current = self.head # se empieza a recorrer desde la cabeza de la lista
            while current is not None:
                if current.valor == pais: # si el pais que se ingresa ya existe en la lista, se incrementa su frecuencia y se retorna
                    current.frequency += 1  # Incrementamos la frecuencia si el país ya existe
                    return

                # ya aqui se recorre la lista hasta el final, si no se encuentra el país, se agrega un nuevo nodo con el pais al final de la lista
                current = current.next
                if current is None:
                    nuevo_nodo = NodoFrecuencia(pais)
                    self.tail.next = nuevo_nodo
                    self.tail = nuevo_nodo

        self.size += 1
        return ("Se agregó el país a la lista de frecuencia")


# este si fue mas complejo, se tiene que recorrer la lista de productos y por cada producto, obtener su pais de origen, para agregarlo a la lista de frecuencias
    def generarListaFrecuencia(self, linked_list): # es por esto que linked_list se pasa como parametro, para poder recorrerla y obtener los paises de origen de cada producto
        if linked_list.empty():
            print("La lista está vacía")
            return
        else:
            frecuencias = ListaFrecuencia() # frecuencias es una instancia de la clase ListaFrecuencia, que se va a llenar con los paises de origen de los productos
            current = linked_list.head # para recorrer la lista desde la cabeza 
            while current is not None:
                # se obtiene el país de origen del producto actual
                pais = current.valor.origin_contry
                # se agrega el país a la lista de frecuencias usando el método agregarPais
                frecuencias.agregarPais(pais)
                current = current.next
            return frecuencias

    def recorrerListaFrecuencia(self):
        if self.empty():
            print("La lista de frecuencia está vacía")
            return

        # si la lista no está vacía, se recorre la lista y se imprime el país y su frecuencia
        else:
            current = self.head
            while current is not None:
                print(f"País: {current.valor}, Frecuencia: {current.frequency}")
                current = current.next


    def paises_mas_frecuentes(self):
        if self.empty():
            print("La lista de frecuencia está vacía")
            return 
        else:
            # aqui se recorre la lista de frecuencia para encontrar el país con la mayor frecuencia

            #se inicializa todo para empezar
            pais_mas_frecuente = None
            max_frecuencia = 0
            current = self.head
            # recorremos la lista de frecuencia y se compara la frecuencia de cada país con la frecuencia máxima encontrada hasta el momento
            while current is not None:
                # para encontrar el pais con mayor frecuencia
                if current.frequency > max_frecuencia: 
                    max_frecuencia = current.frequency # actualiza la frecuencia máxima
                    pais_mas_frecuente = current.valor # actualiza el país con mayor frecuencia, con la lista de frecuencias y con el metodo valor, se obtiene el país del nodo actual
                current = current.next
                # ahora solo se imrpime 
            print(f"La frecuencia máxima del pais es: {pais_mas_frecuente}, con una frecuencia de: {max_frecuencia} veces") 


def main():
    # Crear una lista enlazada de productos
    lista_productos = Linkedlist()

    # Agregar productos a la lista
    lista_productos.agregarProducto(Product(1, "Manzanas", 1.5, "USA", 10))
    lista_productos.agregarProducto(Product(2, "Bananas", 0.5, "Ecuador", 0))
    lista_productos.agregarProducto(Product(3, "Naranjas", 2.0, "España", 5))
    lista_productos.agregarProducto(Product(4, "Uvas", 3.0, "Chile", 0))
    lista_productos.agregarProducto(Product(5, "Fresas", 2.5, "México", 8))

    # Generar la cola de compras con productos sin existencia
    cola_compras = lista_productos.generarColaDeCompras()
    print("Productos en la cola de compras:")
    current = cola_compras.head
    while current is not None:
        current.valor.Productprint()
        current = current.next

    # Generar la lista de frecuencia de países de origen
    lista_frecuencia = ListaFrecuencia()
    lista_frecuencia.generarListaFrecuencia(lista_productos)
    print("\nLista de frecuencia de países de origen:")
    lista_frecuencia.recorrerListaFrecuencia()
    lista_frecuencia = lista_frecuencia.generarListaFrecuencia(lista_productos)

    # Encontrar el país más frecuente
    print("\nPaís más frecuente:")
    lista_frecuencia.paises_mas_frecuentes()  

if __name__ == "__main__":
    main()

    


