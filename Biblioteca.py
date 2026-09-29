#Laboratorio Elaborado por Marcos Alvarado y Daniel Brenes


#Comprobacion de la correcta funcion del la lectura y escritura del los archivos catalogo, y movimientos







class NodoLibro:
    def __init__(self, codigo, titulo, disponibles):
        self.codigo = codigo
        self.titulo = titulo
        self.disponibles = disponibles
        self.izquierdo = None
        self.derecho = None
 
def insertar(raiz, codigo, titulo, disponibles):
    if raiz is None:
        return NodoLibro(codigo, titulo, disponibles)
    if codigo < raiz.codigo:
        raiz.izquierdo = insertar(raiz.izquierdo, codigo, titulo, disponibles)
    elif codigo > raiz.codigo:
        raiz.derecho = insertar(raiz.derecho, codigo, titulo, disponibles)
    else:
        raise ValueError(f'Código duplicado: {codigo}')
    return raiz
 
def cargar_catalogo(ruta):
    raiz = None
    with open(ruta, encoding='utf-8') as archivo:
        for numero, linea in enumerate(archivo, 1):
            if not linea.strip():
                continue
            partes = linea.strip().split('|')
            if len(partes) != 3:
                raise ValueError(f'Línea {numero} incorrecta')
            codigo, titulo, disponibles = partes
            if int(disponibles) < 0:
                raise ValueError(f'Inventario negativo en línea {numero}')
            raiz = insertar(raiz, int(codigo), titulo, int(disponibles))
    return raiz


def buscar(nodo, codigo):
    if nodo is None or nodo.codigo == codigo:
        return nodo
    if codigo < nodo.codigo:
        return buscar(nodo.izquierdo, codigo)
    return buscar(nodo.derecho, codigo)
 
def listado_inorden(nodo):
    if nodo is None:
        return []
    return (listado_inorden(nodo.izquierdo)
            + [(nodo.codigo, nodo.titulo, nodo.disponibles)]
            + listado_inorden(nodo.derecho))


def prestar(raiz, libro):
    libro = buscar(raiz, libro)

    if libro is None or libro.disponibles == 0:
        return False

    libro.disponibles -= 1
    return True


def devolver(raiz, codigo):

    libro = buscar(raiz, codigo)
    if libro is None:
        return False  # Código no encontrado

#se encontro el liboro y se aumenta en 1 la cantidad de libros disponibles
    libro.disponibles += 1
    return True


def total_disponibles(nodo):
    if nodo is None:
        return 0

    return (nodo.disponibles + total_disponibles(nodo.izquierdo) + total_disponibles(nodo.derecho))

def bajo_inventario(nodo):
    if nodo is None:
        return[]

    izquierda = bajo_inventario(nodo.izquierdo)
    #debe de imprimir en orden ascendente los codigos de los libros que tiene 2 o mas libros disponibles, si tiene menos de 2 libros disponibles se imprime el codigo del libro
    actual = [nodo.codigo] if nodo.disponibles <= 1 else []

    derecha = bajo_inventario(nodo.derecho)
    return izquierda + actual + derecha

def procesar_movimientos(raiz, ruta):
    aceptados = rechazados = 0
    with open(ruta, encoding='utf-8') as archivo:
        for numero, linea in enumerate(archivo, 1):
            if not linea.strip():
                continue
            partes = linea.strip().split('|')
            if len(partes) != 2:
                raise ValueError(f'Línea {numero} incorrecta')
            codigo_texto, operacion = partes
            codigo = int(codigo_texto)
            if operacion == 'PRESTAMO':
                exito = prestar(raiz, codigo)
            elif operacion == 'DEVOLUCION':
                exito = devolver(raiz, codigo)
            else:
                raise ValueError(f'Operación inválida en línea {numero}')
            if exito:
                aceptados += 1
            else:
                rechazados += 1
    return aceptados, rechazados


    

 








if __name__ == "__main__":

    #la lectura  y escritura de archivos funciona correctamente
    with open('catalogo_libros.txt', encoding='utf-8') as archivo:
        print('Primer libro:', archivo.readline().strip())
    with open('movimientos.txt', encoding='utf-8') as archivo:
        print('Primer movimiento:', archivo.readline().strip())


    print("Funcionamiento correcto del programa")
raiz = cargar_catalogo('catalogo_libros.txt')
print('Raíz:', raiz.codigo)  # 410

print('Libro 330:', buscar(raiz, 330).titulo)
print('Código 999 registrado:', buscar(raiz, 999) is not None)
for libro in listado_inorden(raiz):
    print(libro)



    print("PRUEBAS 1")
    hojaizquierda = raiz.izquierdo
    hojaderecha = raiz.derecho
    print('Hijo izquierdo de la raíz:', hojaizquierda.codigo)  # 205
    print("Hijo derecho de la raiz:", hojaderecha.codigo)  # 615

    hojaizquierda_izquierda = hojaizquierda.izquierdo
    hojaizquierda_derecha = hojaizquierda.derecho

    print('Hijo izquierdo del hijo izquierdo de la raíz:', hojaizquierda_izquierda.codigo)  
    print('Hijo derecho del hijo izquierdo de la raíz:', hojaizquierda_derecha.codigo) 

    print("\n")
    print("\n")
    print("\n")




    print("-----Prestar-----")
    print(prestar(raiz, 330))  # True: pasa de 2 a 1
    print(prestar(raiz, 330))  # True: pasa de 1 a 0
    print(prestar(raiz, 330))  # False: no hay ejemplares
    print(prestar(raiz, 999))  # False: código inexistente
    print(buscar(raiz, 330).disponibles)  # 0
    print("\n")

    print("-----Devolver-----")
    print(devolver(raiz, 580))  # True: pasa de 1 a 2
    print(devolver(raiz, 999))  # False: catálogo sin cambios
    print(buscar(raiz, 580).disponibles)  # 2

    print("------Total disponibles------")
    print('Ejemplares disponibles:', total_disponibles(raiz))
    print('Códigos de bajo inventario:', bajo_inventario(raiz))


    print("\n")
    print("-----Procesar movimientos-----")
    raiz_lote = cargar_catalogo('catalogo_libros.txt')
    aceptados, rechazados = procesar_movimientos(raiz_lote, 'movimientos.txt')
    print('Aceptados:', aceptados, 'Rechazados:', rechazados)
    print('Existencias:', total_disponibles(raiz_lote))
    print('Bajo inventario:', bajo_inventario(raiz_lote))



    print("\n")
    print("PRUEBAS 2")
    print("Búsqueda en árbol vacío:", buscar(None, 410))
    print("Listado inorden del árbol vacío:", listado_inorden(None))
    print("Total de disponibles en el árbol vacío:", total_disponibles(None))
    print("Bajo inventario en el árbol vacío:", bajo_inventario(None))

    try:
        print("Insertando codigo repetido en el árbol:", insertar(raiz, 520, "Libro Duplicado", 1))

    except ValueError as e:
        print("Error al insertar código duplicado:", e)













