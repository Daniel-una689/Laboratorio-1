#Tarea 1
#Marcos Alvarado y Daniel Brenes

#creamos la clase del producto

#para la validacion del id
#from unicodedata import name, numeric

from collections import deque


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



    def printcola(self):
            if self.is_empty():
                print("La cola esta vacia")
                return
            else:
                current = self.head
                while current is not None:
                    current.valor.Productprint()
                    current = current.next





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
    
    def agregar_producto(self, producto: Product):
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



    def eliminar_producto(self,id):
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


            

    def buscar_producto(self, id):
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

    def generar_Reporte(self, nombrearch):
        if self.empty():
            print("La lista de frecuencia está vacía")
            return
        else:
            with open(nombrearch, "w") as archivo:
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
            return pais_mas_frecuente, max_frecuencia



def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero entero.")


def solicitar_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero.")


def crear_producto_desde_input():
    print("\nIngrese los datos del producto:")
    product_id = solicitar_entero("ID: ")
    name = input("Nombre: ").strip()
    price = solicitar_decimal("Precio: ")
    origin_country = input("Pais de origen: ").strip()
    existence = solicitar_entero("Existencias: ")
    return Product(product_id, name, price, origin_country, existence)


def cargar_datos_prueba(lista_productos):
    datos = [
        Product(1, "Manzanas", 1.5, "USA", 10),
        Product(2, "Bananas", 0.5, "Ecuador", 0),
        Product(3, "Naranjas", 2.0, "Espana", 5),
        Product(4, "Uvas", 3.0, "Chile", 0),
        Product(5, "Fresas", 2.5, "Mexico", 8),
    ]
    for producto in datos:
        lista_productos.agregar_producto(producto)
    print("Datos de prueba cargados.")


def mostrar_menu():
    print("\n===== MENU SUPERMERCADO =====")
    print("1. Ingresar producto")
    print("2. Eliminar producto por ID")
    print("3. Buscar producto por ID")
    print("4. Mostrar lista de productos (recursivo)")
    print("5. Generar cola de compras (existencia = 0)")
    print("6. Mostrar frecuencia de paises de origen")
    print("7. Generar reporte (archivo.txt)")
    print("8. Cargar datos de prueba")
    print("0. Salir")


def main():
    lista_productos = Linkedlist()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            producto = crear_producto_desde_input()
            lista_productos.agregar_producto(producto)

        elif opcion == "2":
            product_id = solicitar_entero("Ingrese el ID del producto a eliminar: ")
            lista_productos.eliminar_producto(product_id)

        elif opcion == "3":
            product_id = solicitar_entero("Ingrese el ID del producto a buscar: ")
            producto = lista_productos.buscar_producto(product_id)
            if producto is None:
                print(f"No se encontro un producto con ID {product_id}.")
            else:
                print("Producto encontrado:")
                producto.Productprint()

        elif opcion == "4":
            lista_productos.printRecursive(lista_productos.head)

        elif opcion == "5":
            cola = lista_productos.generarColaDeCompras()
            cola.printcola()

        elif opcion == "6":
            frecuencias = ListaFrecuencia().generarListaFrecuencia(lista_productos)
            frecuencias.recorrerListaFrecuencia()
            resultado = frecuencias.paises_mas_frecuentes()
            if resultado is not None:
                pais, frecuencia = resultado
                print("El país con mayor frecuencia es:", pais, "con una frecuencia de:", frecuencia)

        elif opcion == "7":
            lista_productos.generar_Reporte("archivo.txt")

        elif opcion == "8":
            cargar_datos_prueba(lista_productos)

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida. Intente de nuevo.")


if __name__ == "__main__":
    main()




