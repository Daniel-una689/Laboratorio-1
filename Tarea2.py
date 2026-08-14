#Codigo hecho por Marcos Alvarado y Daniel Brenes



from ast import Not


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
        current =self.head
        while current is not None:
            print(current.valor, end="->")
            current = current.siguiente
            if current is None:
                print("None")
        print()

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
        total= 0.0

        while current is not None:
            total += current.valor
            current = current.siguiente

        return float(total / self.size)
    #deberia de devolver el promedio de los valores en float



    def minimo(self):
        #lo que queremos hacer con este metodo es recorrer toda la lista y obtener el valor minimo dentro de la lista

        if self.vacia():
            print("La lista esta vacia")
            return None

        current = self.head
        minimo = current.valor

        while current is not None:
            if current.valor < minimo:
                minimo = current.valor
                current = current.siguiente
            else:
                current = current.siguiente

        return minimo


    #agregamos un metodo que nos ayude a calcular el masximo valor dentro de la lista

    def maximo(self):
        if self.vacia():
            print("La lista estas vacia")

        #variable que nos ayude a recorrer la lista y otra para el maximo 
        current = self.head
        maximo = current.valor

        while current is not None:
            if current.valor > maximo:
                maximo = current.valor
                current = current.siguiente
            else:
                current = current.siguiente

        return maximo
    


if __name__ == "__main__":

    lista = LinkedList()
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    valor = int(linea)
                    lista.insertarAlInicio(valor)

                    # se imprime dentro del for como tú quieres
                    lista.imprimirAdelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    except ValueError:
        print("Error: el archivo contiene un dato que no es entero.")
        exit()

    # Aqui van las estadisticas, despues de leer todo
    print(f"Promedio: {lista.promedio()}")
    print(f"Minimo: {lista.minimo()}")
    print(f"Maximo: {lista.maximo()}")


    with open("Reporte.txt", "w") as archivo:
            archivo.write("====================================\n")
            archivo.write("    REPORTE DE TEMPERATURAS\n")
            archivo.write("====================================\n\n")
            archivo.write(
            "Cantidad de elementos dentro del archivo: "
            + str(lista.cantidadElementos())
            + "\n" + "Promedio de Temperaturas: "
            + str(lista.promedio()) + "\n" + "Mínimo: "
            + str(lista.minimo()) + "\n" + "Máximo: "
            + str(lista.maximo()) + "\n" + "Reporte hecho por Marcos Alvarado y Daniel Brenes\n"
            + "====================================\n"

        )

    
