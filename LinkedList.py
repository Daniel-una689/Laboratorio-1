class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None



#en este caso estamos con el valor anterior porque es una lista doblemente enlazada
#lo que significa que metodos como la  busqueda, agregar y eliminar son mas eficientes que 
#una lista simple, ya que podemos recorrer la lista en ambas direcciones

class listaDobleEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None #hace referencia al ultimo nodo de la lista
        self.size = 0


    def vacia(self):
        return self.head is None




    def agregarinicio(self, valor):
        newnode = Nodo(valor)
        if self.vacia():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.siguiente = self.head
            self.head.anterior = newnode
            self.head = newnode
            #lo que esta pasando es que newnode.siguiente es nulo y apunta a la cabeza de la lista
            #el anterior el que se quiere agregar al inicio de la lista,

        self.size += 1


#vamos recorriendo hacia la derecha
    def recorrerAdelante(self):
        current = self.head
        while current:
            print(current.valor, end="->")
            current = current.siguiente
            if current is None:
                print("None")
        print()

#lo mismo pero hacia atras y con el tail 
#tambien lo podemos decir como recorrer havia la izquierda
    def recorrerAtras(self):
        current = self.tail
        while current:
            print(current.valor, end="->")
            current = current.anterior
            if current is None:
                print("None")
        print()



    def agregarFinal(self, valor):
        newnode = Nodo(valor)
        if self.vacia():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.anterior = self.tail
            self.tail.siguiente = newnode
            self.tail = newnode
        self.size+= 1
        #el size es para saber cuantos elementos hay en la lista



    def agregarmedio(self, valor, posicion):
        if self.vacia():
            print("La lista esta vacia")
            return

        if posicion < 0 or posicion > self.size:
            print("Posicion invalida")
            return

        if posicion ==0:
            self.agregarinicio(valor)
            print("El valor se agrego al inicio de la lista")
            return

        if posicion == self.size:
            self.agregarFinal(valor)
            print("El valor se agrego al final de la lista")
            return

        #creamos un nuevo nodo con el valor que queremos agregar
        newnode = Nodo(valor)

        current = self.head

        for i in range(posicion): 
            current = current.siguiente

        #conectamos el nuevo nodo con el nodo anterior
        anterior = current.anterior

        newnode.anterior = anterior
        newnode.siguiente = current

        anterior.siguiente = newnode
        current.anterior = newnode

        self.size += 1 


    def eliminarInicio(self):

        if self.vacia():
            print("La lista esta vacia")
            return

        #si queremos saber que nodo es que queremos eliminar tenemos que crear una variable

        valor_eliminado = self.head.valor

        #en caso de que solo exista un nodo dentro de la lista

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            
            self.head = self.head.siguiente
            self.head.anterior = None

            self.size -= 1

            return ("El valor eliminado es:" + str(valor_eliminado) + (",el tamano de la lista es de: " + str(self.size)))

    def eliminarFinal(self):
        if self.vacia():
            print("La lista esta vacia")
            return

        valor_eliminado = self.tail.valor

        #valoramos si en la lista solamente hay un nodo
        if self.head == self.tail:
            return self.eliminarInicio()
        else:
            self.tail = self.tail.anterior
            self.tail.siguiente = None

        self.size -= 1
        return ("El valor eliminado es:" + str(valor_eliminado) +  (",el tamano de la lista es de: " + str(self.size)))
        



    def eliminarMedio(self, posicion):

        if self.vacia():
            print("La lista esta vacia")
            return

        if posicion < 0 or posicion >= self.size:
            print("Posicion invalida")
            return

        if posicion == 0:
            return self.eliminarInicio()

        if posicion == self.size -1:
            return self.eliminarFinal()


        #buscamos el nodo que queremos eliminar
        current= self.head

        for i in range(posicion):
            current = current.siguiente

        valor_eliminado = current.valor

        #guardamos el nodo anterior y el nodo siguente

        anterior = current.anterior
        siguiente = current.siguiente

        #conectamos el nodo anterio con el nodo siguiente
        anterior.siguiente = siguiente
        siguiente.anterior = anterior

        self.size -= 1

        return ("El valor eliminado es:" + str(valor_eliminado) +  (",el tamano de la lista es de: " + str(self.size)))
        

        



    def printLista(self):
        current = self.head

        while current:
            print(current.valor, end="->")
            current = current.siguiente
            if current is None:
                print("None")

    def buscar(self, valor):
        current =self.head
        posicion = 0
        if self.vacia():
            return False

        while current is not None:
            if current.valor == valor:
                return "Se encontro el valor de la posicion " + str(posicion) + " con el valor " + str(valor)   
            current = current.siguiente
            posicion += 1
        return -1 #valor no encontrado


    def tamanio(self):
        return self.size



#definir el main no es tan necesario dado que podemos hacer lo de abajo y el programa ya se ejecutaria

def main():
    lista = listaDobleEnlazada()
    lista.agregarinicio(1)
    lista.agregarinicio(2)
    lista.agregarinicio(5)
    lista.agregarinicio(10)
    


    print(lista.vacia())  # Output: False

    #print("Recorrido hacia adelante:" + str(lista.recorrerAdelante()))  # Output: 5 2 1
    #o podemos hacerlo
    print("RECCORIDO HACIA ADELANTE: ")
    lista.recorrerAdelante()  # Output: 5 2 1


    print("RECCORIDO HACIA ATRAS: ")
    lista.recorrerAtras()  # Output: 1 2 5

    print("AGREGANDO AL FINAL: ")
    lista.agregarFinal(66)
    print("Se agrego el valor 66 al final de la lista")
    print("\n")

    print("LISTA ACTUALIZADA: ")
    lista.printLista()
    print("\n")

    print("TAMAÑO DE LA LISTA: ")
    print(lista.size)   #deberia de ser 4
    print("\n") #saltamos de linea

    print("AGREGANDO EN EL MEDIO: ")
    lista.agregarmedio(99, 2) #agregamos en la posicion 2 el valor 99
    print("\n")

    print("LISTA ACTUALIZADA: ")
    lista.printLista()
    print("\n")

    print("TAMANO DE LA LISTA:")
    print(lista.size)   #deberia de ser 5


    #o tambien podemos llamar el metodo tamanio()
    #print("Tamano de la lista" + str(lista.tamanio()))  # Output: 6


    print("BUSCANDO EL VALOR 2:" + str(lista.buscar(2)))  # Output: 1


if __name__ == "__main__":
    main()    