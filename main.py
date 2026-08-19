print("¡Hola mundo!")
import os
import platform

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase de una simple lista
class simpleList:
    def __init__(self):
        # En este caso solo es self porque únicamente nos importa el objeto que se está creando
        self.head = None # También podemos decir que self es el primer nodo de la lista
        self.tail = None # El tail es el último nodo de la lista
        self.size = 0    # El tamaño de la lista es 0 porque no hay nodos en la lista

    def display(self):
        current = self.head
        while (current):
            print(current.data, end="->")
            current = current.next
        print("None")

    def insertarInicio(self, valor):
        # Queremos insertar un nodo al inicio de la lista por lo tanto tenemos que hacer que el siguiente nodo del nuevo nodo sea el head y que el head sea el nuevo nodo
        new_node = Node(valor)

        # Confirmamos que la lista no esté vacía
        if (self.head is None):
            self.head = new_node
            self.tail = new_node # LOGICA: Si la lista estaba vacía, el primer nodo también es el último (tail).
            self.size += 1       # LOGICA: Incrementamos el tamaño de la lista de 0 a 1.
            return

        # El siguiente del nuevo nodo toma el valor del head y el head toma el valor del nuevo nodo
        # para que el nuevo nodo sea el primero de la lista y el head apunte al nuevo nodo
        new_node.next = self.head
        self.head = new_node
        self.size += 1           # LOGICA: Sumamos 1 al tamaño porque añadimos un elemento con éxito.

    def insertmiddle(self, valor, posicion):
        new_Node = Node(valor) # Creamos un nuevo nodo con el valor que se le pasa a la función

        # LOGICA CONTROL DE LIMITES: Si intentan meter una posición negativa o mayor al tamaño actual, frena el código.
        if posicion < 0 or posicion > self.size:
            print("La posición está fuera de los límites de la lista")
            return None

        # CASO 1: Insertar en la posición 0 (Inicio de la lista)
        if (posicion == 0):
            new_Node.next = self.head
            self.head = new_Node # LOGICA: ¡CORREGIDO! Antes el nodo quedaba flotando porque no actualizabas self.head.
            if self.tail is None: # Si la lista estaba vacía, este nodo inicial también pasa a ser la cola.
                self.tail = new_Node
            self.size += 1       # LOGICA: Modificamos el contador de tamaño global.
            return self.head

        # CASO 2: Si la posición pedida coincide con el tamaño actual, significa que va al final de la lista.
        if posicion == self.size:
            self.insertarFinal(valor)
            return self.head

        # CASO 3: Insertar en el medio exacto solicitado por parámetro.
        # Creamos la variable current para recorrer la lista
        current = self.head
        count = 0

        # LOGICA: ¡CORREGIDO! Eliminamos por completo la antigua variable 'mid = count // 2' que calculaba otra cosa.
        # Avanzamos hasta 'posicion - 1' porque queremos que el current sea el nodo ANTERIOR al que queremos insertar.
        while (current is not None and count < posicion - 1):
            count += 1
            current = current.next

        # Conectamos los punteros
        new_Node.next = current.next
        current.next = new_Node
        self.size += 1 # LOGICA: Sumamos 1 al contador global de nodos.
        return self.head

    def insertarFinal(self, valor):
        new_node = Node(valor)

        if self.head is None:
            self.head = new_node
            self.tail = new_node # LOGICA: Si la lista estaba vacía, este primer elemento es cabeza y cola.
            self.size += 1       # LOGICA: Actualizamos el contador.
            return new_node

        # LOGICA OPTIMIZACIÓN: Como tu clase tiene 'self.tail', ya no necesitas usar un bucle 'while'
        # que recorra toda la lista (Eficiencia O(n)). Ahora puedes colgar el nodo directamente al tail en un solo paso (Eficiencia O(1)).
        self.tail.next = new_node # El que era el último nodo ahora apunta al nuevo.
        self.tail = new_node      # El puntero tail se desplaza y ahora apunta al nuevo nodo.
        self.size += 1            # LOGICA: Sumamos 1 al tamaño global.
        return new_node

    def deleteFirst(self):
        if self.head is None:
            print("La lista esta vacia")
            return None

        currentdelte = self.head
        self.head = self.head.next

        if self.head is None: # LOGICA: Si al borrar el elemento la lista se quedó vacía, tail también debe ser None.
            self.tail = None

        self.size -= 1 # LOGICA: Al remover un elemento restamos 1 de forma global a size.
        return currentdelte.data

    def deletePosition(self, position):

        if position < 0:
            print("La posición no puede ser negativa")
            return None

        # CASO 0: La lista ya está completamente vacía
        if self.head is None:
            print("La lista está vacía")
            return None

        # CASO 1: Eliminar el primer nodo (Posición 0)
        if position == 0:
            return self.deleteFirst() # Delegamos la acción a tu método existente

        # CASO GENERAL: Eliminar en posiciones intermedias o al final
        current = self.head
        count = 0

        # Recorremos la lista para posicionarnos en el nodo ANTERIOR al que queremos borrar
        # Nos detenemos si llegamos al final de la lista o al índice (position - 1)
        while (current is not None and count < position - 1):
            count += 1
            current = current.next

        # CONTROL DE ERRORES: Si la posición buscada está fuera de los límites de la lista
        if current is None or current.next is None:
            print("La posición está fuera de los límites de la lista")
            return None

        # El nodo que vamos a borrar es el que está justo después de current
        node_to_delete = current.next

        # RECONEXIÓN: El nodo actual se salta al siguiente y apunta al "nieto"
        current.next = node_to_delete.next

        # CONTROL DEL TAIL: Si el nodo eliminado era el último, actualizamos el puntero tail al nodo anterior (current)
        if node_to_delete == self.tail:
            self.tail = current

        # Opcional: Desconectamos el nodo eliminado por completo de la memoria
        node_to_delete.next = None

        self.size -= 1 # LOGICA: Restamos 1 al tamaño de la lista porque quitamos un elemento.

        # Retornamos el valor del nodo eliminado
        return node_to_delete.data

    def deletelast(self):
        if self.head is None:
            print("La lista está vacía")
            return None # LOGICA: Cambiado a retornar None para ser consistente con deleteFirst.

        if self.head.next is None:
            valor = self.head.data
            self.head = None
            self.tail = None # LOGICA: Si la lista queda vacía, tail también vuelve a None.
            self.size -= 1   # LOGICA: Restamos 1 a size.
            return valor

        current = self.head
        while current.next.next is not None:
            current = current.next

        valor_eliminado = current.next.data
        current.next = None
        self.tail = current # LOGICA: Como borramos el último, el penúltimo (current) pasa a ser el nuevo tail.
        self.size -= 1      # LOGICA: Restamos 1 al contador global de tamaño.
        return valor_eliminado

    # Método que verifica que la lista no esté vacía
    def listavacia(self):
        # Un método de consulta solo debe retornar el estado booleano
        return self.head is None
    #return self.size == 0 # Alternativa: También podrías usar el tamaño para determinar si está vacía.

    def cantidadElemento(self, dato):
        c = 0
        current = self.head

        # Recorremos la lista UNA SOLA VEZ (Eficiencia O(n))
        while current is not None:
            if current.data == dato:
                c += 1
            current = current.next

        return c

    # No dice dónde se encuentra el elemento ni tampoco la cantidad de elementos iguales hay
    def buscarElemento(self, dato):
        current = self.head
        while current is not None:
            if current.data == dato:
                return True # Retorno temprano apenas lo encuentra
            current = current.next
        return False

    # CORREGIDO: Cambiado de getNode a obtenerValor para ser coherente con que retorna el .data (el entero), NO el objeto Nodo.
    def getNode(self, position):
        if self.head is None:
            print("La lista esta vacia")
            return None

        if position < 0:
            print("La posicion no puede ser menor a cero ni negativa")
            return None

        current = self.head
        index = 0

        while current is not None and index < position-1:
            current = current.next
            index += 1

        if current is None:
            print("La posicion es mayor o igual al tamaño de la lista")
            return None

        return current.data

def clear():
    # Limpiamos la pantalla de la consola
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    lista = simpleList()

    while True:
        clear()

        print("==============================================")
        print("       MENÚ - LISTA ENLAZADA SIMPLE")
        print("==============================================")
        print("1. Insertar nodo al inicio")
        print("2. Insertar nodo en una posición")
        print("3. Insertar nodo al final")
        print("4. Eliminar primer nodo")
        print("5. Eliminar último nodo")
        print("6. Eliminar nodo en una posición")
        print("7. Obtener valor en una posición")
        print("8. Mostrar lista")
        print("9. Salir")
        print("==============================================")

        option_str = input("Ingrese una opción: ")

        # Validamos que la opción sea un número
        if not option_str.isdigit():
            print("La opción debe ser un número.")
            input("Presione ENTER para continuar...")
            continue

        option = int(option_str)

        # Salir
        if option == 9:
            print("Saliendo del programa...")
            break

        match option:

            # ==========================================
            # 1. INSERTAR AL INICIO
            # ==========================================
            case 1:
                valor_str = input("Ingrese el valor del nodo: ")

                if valor_str.isdigit():
                    valor = int(valor_str)
                    lista.insertarInicio(valor)
                    print("Nodo insertado correctamente.")
                    lista.display()
                else:
                    print("El valor ingresado no es un número.")

                input("Presione ENTER para continuar...")

            # ==========================================
            # 2. INSERTAR EN UNA POSICIÓN
            # ==========================================
            case 2:
                valor_str = input("Ingrese el valor del nodo: ")
                posicion_str = input("Ingrese la posición: ")

                if valor_str.isdigit() and posicion_str.isdigit():
                    valor = int(valor_str)
                    posicion = int(posicion_str)

                    lista.insertmiddle(valor, posicion)

                    print("Lista actual:")
                    lista.display()
                else:
                    print("El valor y la posición deben ser números.")

                input("Presione ENTER para continuar...")

            # ==========================================
            # 3. INSERTAR AL FINAL
            # ==========================================
            case 3:
                valor_str = input("Ingrese el valor del nodo: ")

                if valor_str.isdigit():
                    valor = int(valor_str)
                    lista.insertarFinal(valor)

                    print("Nodo insertado correctamente.")
                    lista.display()
                else:
                    print("El valor ingresado no es un número.")

                input("Presione ENTER para continuar...")

            # ==========================================
            # 4. ELIMINAR PRIMER NODO
            # ==========================================
            case 4:
                eliminado = lista.deleteFirst()

                if eliminado is not None:
                    print(f"Se eliminó el nodo con valor: {eliminado}")

                lista.display()

                input("Presione ENTER para continuar...")

            # ==========================================
            # 5. ELIMINAR ÚLTIMO NODO
            # ==========================================
            case 5:
                eliminado = lista.deletelast()

                if eliminado is not None:
                    print(f"Se eliminó el nodo con valor: {eliminado}")

                lista.display()

                input("Presione ENTER para continuar...")

            # ==========================================
            # 6. ELIMINAR POR POSICIÓN
            # ==========================================
            case 6:
                posicion_str = input("Ingrese la posición a eliminar: ")

                if posicion_str.isdigit():
                    posicion = int(posicion_str)

                    eliminado = lista.deletePosition(posicion)

                    if eliminado is not None:
                        print(f"Se eliminó el nodo con valor: {eliminado}")

                    lista.display()
                else:
                    print("La posición debe ser un número.")

                input("Presione ENTER para continuar...")

            # ==========================================
            # 7. OBTENER VALOR
            # ==========================================
            case 7:
                posicion_str = input("Ingrese la posición: ")

                if posicion_str.isdigit():
                    posicion = int(posicion_str)

                    nodo = lista.getNode(posicion)

                    if nodo is not None:
                        print(f"El valor en la posición {posicion} es: {nodo}")
                else:
                    print("La posición debe ser un número.")

                input("Presione ENTER para continuar...")

            # ==========================================
            # 8. MOSTRAR LISTA
            # ==========================================
            case 8:
                print("Lista actual:")
                lista.display()

                print(f"Cantidad de elementos: {lista.size}")

                if lista.listavacia():
                    print("La lista está vacía.")
                else:
                    print("La lista contiene elementos.")

                input("Presione ENTER para continuar...")

            # ==========================================
            # OPCIÓN NO EXISTENTE
            # ==========================================
            case _:
                print("Opción no válida.")
                print("Por favor, ingrese una opción del 1 al 9.")

                input("Presione ENTER para continuar...")



if __name__ == "__main__":
    main()
