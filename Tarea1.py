# Tarea 1
# Marcos Alvarado y Daniel Brenes

# creamos la clase del producto
class Product:
    def __init__(self, product_id, name, price, origin_country, existence):
        self.id = product_id
        self.name = name
        self.price = price
        self.origin_country = origin_country
        self.existence = existence

    def subtotal(self):
        return self.price * self.existence

    def product_print(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.name}")
        print(f"Precio: {self.price}")
        print(f"Pais de origen: {self.origin_country}")
        print(f"Existencias: {self.existence}")
        print(f"Subtotal: {self.subtotal()}")
        print("-" * 40)

    Productprint = product_print


# Clase para la cola de compras
class NodeQueue:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, product):
        new_node = NodeQueue(product)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def print_queue(self):
        if self.is_empty():
            print("La cola de compras esta vacia.")
            return
        print("Productos en la cola de compras (existencia = 0):")
        current = self.head
        while current is not None:
            current.value.product_print()
            current = current.next


# Nodo de la lista doblemente enlazada
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


# Clase principal de la lista doblemente enlazada
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def agregar_producto(self, product):
        if self.buscar_producto(product.id) is not None:
            print(f"Ya existe un producto con ID {product.id}.")
            return False

        new_node = Node(product)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.size += 1
        print("Producto agregado correctamente.")
        return True

    # Alias para mantener compatibilidad con el nombre original del proyecto
    agregarProducto = agregar_producto

    def buscar_producto(self, product_id):
        current = self.head
        while current is not None:
            if current.value.id == product_id:
                return current.value
            current = current.next
        return None

    search = buscar_producto

    def eliminar_producto(self, product_id):
        if self.is_empty():
            print("La lista esta vacia.")
            return False

        current = self.head
        while current is not None:
            if current.value.id == product_id:
                if current.previous is None:
                    self.head = current.next
                else:
                    current.previous.next = current.next

                if current.next is None:
                    self.tail = current.previous
                else:
                    current.next.previous = current.previous

                self.size -= 1
                print(f"Producto con ID {product_id} eliminado.")
                return True
            current = current.next

        print(f"No se encontro un producto con ID {product_id}.")
        return False

    deleteProduct = eliminar_producto

    def mostrar_recursivo(self):
        if self.is_empty():
            print("La lista de productos esta vacia.")
            return
        print("Lista de productos (recursivo):")
        self._mostrar_recursivo(self.head)

    def _mostrar_recursivo(self, node):
        if node is None:
            return
        node.value.product_print()
        self._mostrar_recursivo(node.next)

    printRecursive = _mostrar_recursivo

    def generar_cola_existencia_cero(self):
        cola = Queue()
        current = self.head
        while current is not None:
            if current.value.existence == 0:
                cola.enqueue(current.value)
            current = current.next
        return cola

    generarColaDeCompras = generar_cola_existencia_cero

    def generar_lista_frecuencia_paises(self):
        frecuencias = FrequencyList()
        current = self.head
        while current is not None:
            frecuencias.agregar_pais(current.value.origin_country)
            current = current.next
        return frecuencias

    def generar_reporte(self, nombre_archivo="archivo.txt"):
        if self.is_empty():
            print("No hay productos para generar el reporte.")
            return 0

        total_general = 0
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Reporte de recuperacion del supermercado\n")
            archivo.write("-" * 50 + "\n")
            current = self.head
            while current is not None:
                producto = current.value
                subtotal = producto.subtotal()
                total_general += subtotal
                archivo.write(
                    f"ID: {producto.id}, Nombre: {producto.name}, "
                    f"Existencias: {producto.existence}, Precio: {producto.price}, "
                    f"Subtotal: {subtotal}\n"
                )
                current = current.next
            archivo.write("-" * 50 + "\n")
            archivo.write(f"Total general a recuperar: {total_general}\n")

        print(f"Reporte generado en '{nombre_archivo}'.")
        print(f"Total general a recuperar: {total_general}")
        return total_general

    generar_Rerporte = generar_reporte


# Lista de frecuencias para contar los paises de origen
class FrequencyNode:
    def __init__(self, country):
        self.country = country
        self.frequency = 1
        self.next = None


class FrequencyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # Alias para preservar el nombre original del proyecto
    empty = is_empty

    def agregar_pais(self, country):
        if self.is_empty():
            nuevo = FrequencyNode(country)
            self.head = nuevo
            self.tail = nuevo
            self.size += 1
            return

        current = self.head
        while current is not None:
            if current.country == country:
                current.frequency += 1
                return
            current = current.next

        nuevo = FrequencyNode(country)
        self.tail.next = nuevo
        self.tail = nuevo
        self.size += 1

    agregarPais = agregar_pais

    def imprimir_frecuencias(self):
        if self.is_empty():
            print("No hay frecuencias para mostrar.")
            return

        print("Frecuencia de paises de origen:")
        current = self.head
        while current is not None:
            print(f"Pais: {current.country} | Frecuencia: {current.frequency}")
            current = current.next

    recorrerListaFrecuencia = imprimir_frecuencias

    def pais_mas_frecuente(self):
        if self.is_empty():
            return None

        current = self.head
        mayor = current
        while current is not None:
            if current.frequency > mayor.frequency:
                mayor = current
            current = current.next
        return mayor

    paises_mas_frecuentes = pais_mas_frecuente


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
    lista_productos = LinkedList()

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
                producto.product_print()

        elif opcion == "4":
            lista_productos.mostrar_recursivo()

        elif opcion == "5":
            cola = lista_productos.generar_cola_existencia_cero()
            cola.print_queue()

        elif opcion == "6":
            frecuencias = lista_productos.generar_lista_frecuencia_paises()
            frecuencias.imprimir_frecuencias()
            mayor = frecuencias.pais_mas_frecuente()
            if mayor is not None:
                print(
                    f"Pais con mayor frecuencia: {mayor.country} "
                    f"({mayor.frequency} productos)"
                )

        elif opcion == "7":
            lista_productos.generar_reporte("archivo.txt")

        elif opcion == "8":
            cargar_datos_prueba(lista_productos)

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida. Intente de nuevo.")


FrequencyNode.NodoFrecuencia = FrequencyNode
FrequencyList.ListaFrecuencia = FrequencyList

if __name__ == "__main__":
    main()
