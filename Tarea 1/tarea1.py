import os
import platform



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



#clase de una simpre lsita

class simpleList:
    def __init__(self): #en este caso solo es self porque unicamente nos importa 
    #el objeto que se esta creando

        self.head  = None #tambien podemos decir que self es el primer nodo de la lista
        self.tail = None #el tail es el ultimo nodo de la lista
        self.size = None #el tamaño de la lista es 0 porque no hay nodos en la lista


    def display(self):
        current = self.head
        while (current):
            print(current.data, end="->")
            current = current.next
        print("None")

    def insertarInicio(self, valor):

        #queremos insertar un nodo al inicio de la lista por lo tanto tenemos que hacer que el siguiente nodo del nuevo nodo sea el head y que el head sea el nuevo nodo

        new_node = Node(valor)

        #confirmamos que la lista no este vacia

        if (self.head is None):
            self.head = new_node
            return

        #el siguiente del nuevo nodo toma el valor del head y el head toma el valor del nuevo nodo
        #para que el nuevo nodo sea el primero de la lista y el head apuunte al nuevo nodo

        new_node.next = self.head
        self.head = new_node

#=====SUGERENCUAS PARA EL EJERCICIO=====
#CONFIRMAR QUE LA CABEZA DE LA LISTA ESTE VACIA EN CASO DE QUE NO SE ESPECIFIQUE EN EL EJERCICIO,
#DE QUE DEBE DE SOBRE ESCRIBIRSE 


#solucion de la profe del ejercicio soebre insterar en el inicio



    def insertmiddle(self, valor, posicion):

        new_Node = Node(valor) #creamos un nuevo nodo con el valor que se le pasa a la funcion

        #ahora lo que queremos hacer es insertar un nodo en el medio de la lista, para esto tenemos que recorrer la lista hasta llegar a la mitad y luego insertar el nodo en esa posicion

        if (posicion ==0):
            new_Node.next = self.head
            return new_Node #retornamos el nuevo nodo para que sea el head de la lista 

        #creamos la variable current para recorrer la lista

        current = self.head

        #creamos una variable para contar los nodos de la lista
        count = 0

        while (current is not None and count < posicion -1): 

            #posicion -1 porque queremos que el current sea el nodo anterior al que queremos insertar 
            count += 1
            current = current.next

        #ahora que tenemos el tamano de la lista, podemos calcular la posicion del medio

        mid = count // 2

        if mid ==0:
            new_Node.next = self.head
            self.head = new_Node
            return new_Node


        current = self.head
    
        #recorremos la lista hasta llegar al nodo anterior al que queremos insertar el nuevo nodo   
        for i in range(mid-1): 
            current = current.next

        new_Node.next = current.next 
        current.next = new_Node
        return new_Node 


    def insertarFinal(self, valor):
        new_node = Node(valor)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while (current.next):
            current = current.next
        current.next = new_node
        return new_node



    def deleteFirst(self):
        if self.head is None:
            print("La lista esta vacia")
            return None

        currentdelte = self.head
        self.head = self.head.next
        return currentdelte.data



    def deletePosition(self, position):
        if self.head is None:
            print("La lista esta vacia")
            return None

        if position == 0:
            return self.deleteFirst()



    def deletelast(self):

        currentdelete = self.head
        #verificamos que la lista no este vacia

        if self.head is None:
            print("La lista esta vacia")
            return None

        #verificamos que la lista tenga mas de un nodo
        if self.head.next is None:
            self.head = None
            return currentdelete.data

        #recorremos la lista hasta llegar al penultimo nodo
        while currentdelete.next.next is not None:
            current = current.next

        current.next = None
        return currentdelete.data #eliminamos el ultimo nodo de la lista y retornamos el valor del nodo eliminado


#metodo que verifica que la lista no este vacia
    def listavacia(self):
        if self.head is None:
            print("La lista esta vacia")
            return True
        else:
            print("La lista no esta vacia")
            return False


    def cantidadElemento(self, dato):
        if not self.buscarElemento(dato):
            return 0
        c=0
        current = self.head
        while current is not None:
            if current.data == dato:
                c+=1
                current = current.next
        return c


#no dice donde se encuentra el elemento ni tampoco la cantidad de elementos iguales hay
#
    def buscarElemento(self, dato):
        current = self.head
        while  current is not None:
            if current.data == dato:
                return True
            current = current.next
        return False
            
    
        

#metodo el cual obtiene el nodo segun la posicion que se le pase como parametro a al metodo getNode, 
    def getNode(self, position):
        if self.head is None:
            print("La lista esta vacia")
            return None
        
        if position == 0:
            return self.head.data

        if position <0:
            print("La posicion no puede ser menor a cero ni negativa")
            return None

        if position >= self.size:
            print("La posicion es mayor o igual al tamaño de la lista")
            return None

        #otra forma de hacerlo
        #current = self.head

        #for i in range(position):
        #current = current.next

        #return current.data


        return self.get_node(position).data
    #get_node es un metodo privado que nos ayuda a obtener el nodo segun la posicion que se le pase como parametro al metodo getNode
    #get_node viene de la libreria de python

    



def clear():
    #limpiamos la patntalla de la consola
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")



def loquequieroquehaga():
    print("\n")
    print("Lista Actualizada:")
    list.display()
    print("\n")



#Solucion del ejercicio de la profe sobre insercion en el medio
#RECOMENDACIONES
#Para temas de obtener el tamano podemos hacer una def que conteee el tamano de la lista
#size = int(self.get_size()) // 2
#mejorar el diseno del codigo


def main():
    list = simpleList()
    list.insertarFinal(1)
    list.insertarFinal(2)
    list.insertarFinal(3)
    list.insertarFinal(4)
    list.insertarFinal(5)
    list.insertarFinal(6)

  #mostramos la lista antes de insertar el nodo en el medio
    list.display()
    print("\n") 

    print("Insertando nodo en el medio de la lista")
    list.insertarInicio(0)
    list.display()
    print("\n") 

    print("Insertando nodo en el medio de la lista")
    list.insertmiddle(10, 3)
    list.display()
    print("\n")

    #datos de entrada
    clear() #REVISAR
    #tenemos que hacer un menu para la cantidad de metodos que tenemos

    while True:
        print("-----------Bienvenido al menu de la lista enlazada-----------")
        print("\n")
        print("1. Insertar nodo al inicio")
        print("2. Insertar nodo en el medio")
        print("3. Insertar nodo al final")
        print("4. Eliminar primer nodo")
        print("5. Eliminar ultimo nodo")
        print("6. Eliminar nodo en una posicion especifica")
        print("7. Obtener nodo en una posicion especifica")
        print("8. Mostrar lista")
        print("9. Salir")

        print("\n")
        option_str = input("Ingrese una de las opciones anteriores:")
        if not option_str.isdigit():
            print("Por favor ingrese un numero valido (1-9).")
            continue
        option = int(option_str)

        match option:
            case 1:
                valor_str = input("Ingrese el valor del nodo a insertar al inicio:")
                if valor_str.isdigit():
                    valor = int(valor_str)
                    list.insertarInicio(valor)
                    loquequieroquehaga()
                else:
                    print("El valor ingresado no es un numero")
            case 2:
                valor_str = input("Ingrese el valor del nodo a insertar en el medio:")
                posicion_str = input("Ingrese la posicion en la que desea insertar el nodo:")
                if valor_str.isdigit() and posicion_str.isdigit():
                    valor = int(valor_str)
                    posicion = int(posicion_str)
                    list.insertmiddle(valor, posicion)
                    loquequieroquehaga()
                else:
                    print("El valor ingresado no es un numero")
            case 3:
                valor_str = input("Ingrese el valor del nodo a insertar al final:")
                if valor_str.isdigit():
                    valor = int(valor_str)
                    list.insertarFinal(valor)
                    loquequieroquehaga()
                else:
                    print("El valor ingresado no es un numero")
            case 4:
                list.deleteFirst()
                loquequieroquehaga()
            case 5:
                list.deletelast()
                loquequieroquehaga()
            case 6:
                posicion_str = input("Ingrese la posicion del nodo a eliminar:")
                if posicion_str.isdigit():
                    posicion = int(posicion_str)
                    list.deletePosition(posicion)
                    loquequieroquehaga()
                else:
                    print("El valor ingresado no es un numero")
            case 7:
                posicion_str = input("Ingrese la posicion del nodo a obtener:")
                if posicion_str.isdigit():
                    posicion = int(posicion_str)
                    nodo = list.getNode(posicion)
                    if nodo is not None:
                        print(nodo)
                    loquequieroquehaga()
                else:
                    print("El valor ingresado no es un numero")
            case 8:
                loquequieroquehaga()
            case 9:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida")
                print("Por favor, ingrese una opcion valida.")



if __name__ == "__main__":
    main()

