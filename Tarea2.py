#Codigo hecho por Marcos Alvarado y Daniel Brenes



class Node:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def insertarAlInicio(self, valor):
        nuevo_nodo = Node(valor)

        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.head
            self.head.anterior = nuevo_nodo
            self.head = nuevo_nodo

        self.size += 1

    def imprimirAdelante(self):
        current = self.head
        while current:
            print(current.valor, end=" -> ")
            current = current.siguiente
        print("None")

    def cantidadElementos(self):
        return self.size


    #hacer un metodo que recorra la lista y obtenga el promedio de los valores dentro de la lista

    def vacia(self):
        return self.size == 0

    def promedio(self):
        if self.vacia():
            print("La lista esta vacia")
            return 0

        #hacemos una variable que nos ayude a recorrer la lista

        current = self.head

        #variable que nos ayudara a sumar los valores dentro de la lista
        total= 0

        while current is not None:
            total += current.valor
            current = current.siguiente

        return total / self.size








if __name__ == "__main__":
# Crear la lista doblemente enlazada
    lista = LinkedList()
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip() # Eliminar espacios en blanco
                # Evitar líneas vacías
                if linea != "":
                    valor = int(linea)
                    # Insertar el valor en la lista
                    lista.insertarAlInicio(valor)
                    lista.imprimirAdelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    except ValueError:
        print("Error: el archivo contiene un dato que no es entero.")
        exit()
