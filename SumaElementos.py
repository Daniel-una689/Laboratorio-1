#Marcos Alvarado


#Ejercicio 1 cuenta regresiva RECURSIVIDA 

def cuenta_regresiva(n):
    if n==0:
        return
    print(n)
    cuenta_regresiva(n-1) #llamada recursiva, se va restando 1 hasta llegar a 0, en ese momento retornamos y se va imprimiendo el valor de n en cada llamada recursiva hasta llegar a la primera llamada recursiva donde n es igual a 5, por lo tanto imprimimos 5,4,3,2,1


#suma de numeros hasta n, metodo recursivo

def suma(n):
    if n==0:
        return 1
    return n + suma(n-1) #llamada recursiva, se va restando 1 hasta llegar a 0, en ese momento retornamos 1 y se va sumando el valor de n



def suma(n):
    if n ==0:
        return 1
    return n + suma(n-1)
#facotorial

def factorial(n):
    if n ==0:
        return 1
    return n * factorial(n-1) #llamada recursiva, se va restando 1 hasta llegar a 0, en ese momento retornamos 1 y se va multiplicando el valor de n


#imrpimir una lista recursivamente


def recorrer(lista, posicion):
    if posicion == len(lista):
        return
    print(lista[posicion])
    recorrer(lista, posicion + 1) #llamada recursiva, se va sumando 1 a la posicion hasta llegar a la longitud de la lista, en ese momento retornamos y se va imprimiendo el valor de la lista en cada llamada recursiva hasta llegar a la primera llamada recursiva donde posicion es igual a 0, por lo tanto imprimimos el valor de la lista en la posicion 0,1,2,3,4,5

#recorrer una lista de derecha a iquierda

def recorridoderecha(lista, posicion):
    if posicion < 0:
        return
    print(lista[posicion])
    recorridoderecha(lista, posicion - 1) #llamada recursiva, se va restando 1 a la posicion hasta llegar a -1, en ese momento retornamos y se va imprimiendo el valor de la lista en cada llamada recursiva hasta llegar a la primera llamada recursiva donde posicion es igual a len(lista)-1, por lo tanto imprimimos el valor de la lista en la posicion len(lista)-1,len(lista)-2,...,0


#buscar un elemento recursivamente

def busqueda(lista, posicion, valor):
    if posicion == len(lista):
        return False

    if lista[posicion] == valor:
        return True
    return busqueda(lista, posicion + 1, valor) #llamada recursiva





def bsuqueda(lista, pos, valor):
    if pos == len(lista):
        return False

    if lista[pos] == valor:
        return True
    return busqueda(lista, pos+1, valor)

#contar aparaciocnes de un elemento

def apariciones(lista, pos, valor):

    if pos  == len(lista):
        return 0

    if lista[pos] == valor:
        return 1 + apariciones(lista, pos + 1, valor) #llamada recursiva
    return apariciones(lista, pos + 1, valor) #llamada recursiva


def apariciones(lista, pos, valor):
    if pos == len(lista):
        return 0

    if lista[pos] == valor:
        return 1 + apariciones(lista, pos + 1, valor) #llamada recursiva

    return apariciones(lista, pos + 1, valor) #llamada recursiva








#invertir una palabra

def invertir(palabra):

    if len(palabra) <= 1:
        return palabra
    return invertir(palabra[1:]) + palabra[0] #llamada recursiva, se va cortando la palabra hasta llegar a una longitud de 1, en ese momento retornamos la palabra y se va concatenando el valor de la primera letra en cada llamada recursiva hasta llegar a la primera llamada recursiva donde la palabra es igual a "RECURSION", por lo tanto retornamos "NOISURCER"





def invertir(palabra):
    if len(palabra) <= 1:
        return palabra

    return invertir(palabra[1:]) + palabra[0] #llamada recursiva, se va cortando la palabra hasta llegar a una longitud de 1, en ese momento retornamos la palabra y se va concatenando el valor de la primera letra en cada llamada recursiva hasta llegar a la primera llamada recursiva donde la palabra es igual a "RECURSION", por lo tanto retornamos "NOISURCER"

#determinar el numero mayor de una lista


def mayor(lista, pos):

    if pos == len(lista) - 1:
        return lista[pos]

    mayor_siguiente = mayor(lista, pos + 1) #llamada recursiva, se va sumando 1 a la posicion hasta llegar a la longitud de la lista - 1, en ese momento retornamos el valor de la lista en la posicion pos y se va comparando el valor de la lista en cada llamada recursiva hasta llegar a la primera llamada recursiva donde posicion es igual a 0, por lo tanto retornamos el valor mayor de la lista
    if lista[pos] > mayor_siguiente:
        return lista[pos]
    return mayor_siguiente





def menor(lista, pos):

    if pos == len(lista) -1:
        return lista[pos]


    menor_siguiente = menor(lista, pos + 1) #llamada recursiva, se va sumando 1 a la posicion hasta llegar a la longitud de la lista - 1, en ese momento retornamos el valor de la lista en la posicion pos y se va comparando el valor de la lista en cada llamada recursiva hasta llegar a la primera llamada recursiva donde posicion es igual a 0, por lo tanto retornamos el valor menor de la lista
    if lista[pos] < menor_siguiente:
        return lista[pos]
    return menor_siguiente

#fobinnaci

def fibonnaci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2) #llamada recursiva, se va restando 1 y 2 a n hasta llegar a 0 y 1, en ese momento retornamos 0 y 1 y se va sumando el valor de n en cada llamada recursiva hasta llegar a la primera llamada recursiva donde n es igual a 5, por lo tanto retornamos 5 + 3 + 2 + 1 + 0 = 11



#sumar elementos de una lista

def sumarlusta(lista, pos):
    if pos == len(lista):
        return 0
    return lista[pos] + sumarlusta(lista, pos + 1) #llamada recursiva, se va sumando 1 a la posicion hasta llegar a la longitud de la lista, en ese momento retornamos 0 y se va sumando el valor de la lista en cada llamada recursiva hasta llegar a la primera llamada recursiva donde posicion es igual a 0, por lo tanto retornamos el valor de la lista en la posicion 0,1,2,3,4,5



#determinar si una palabra es palindroma

def palindroma(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] == palabra[-1]:
        return palindroma(palabra[1:-1]) #llamada recursiva, se va cortando la palabra hasta llegar a una longitud de 1, en ese momento retornamos True y se va comparando el valor de la primera y ultima letra en cada llamada recursiva hasta llegar a la primera llamada recursiva donde la palabra es igual a "RECURSION", por lo tanto retornamos False
    return False




def palindroma(palabra):
    if len(palabra) <= 1:
        return True


    if palabra[0] == palabra[-1]:
        return palindroma(palabra[1:-1]) #llamada recursiva, se va cortando la palabra hasta llegar a una longitud de 1, en ese momento retornamos True y se va comparando el valor de la primera y ultima letra en cada llamada recursiva hasta llegar a la primera llamada recursiva donde la palabra es igual a "RECURSION", por lo tanto retornamos False


    #en caso de que no se cumpla la condicion de que la primera y ultima letra sean iguales, retornamos False
    return False
    




#Ejercicio 13
def sumar_lista(lista, posicion): 
    #entra una lista de datos y su posicion, verificamos que la posicion 
    #sea menor que la longitud de la lista, si es asi
    #el metodo len verifica la longitud de la lista y si la posicion es igual a la longitud de la lista, retornamos 0
    if posicion == len(lista):
        return 0
    return lista[posicion] + sumar_lista(lista, posicion + 1)




def restar_lista(lista, pos):


    if pos == len(lista):

        return 0

    return lista[pos] - restar_lista(lista, pos + 1) #llamada recursiva, se va sumando 1 a la posicion hasta llegar a la longitud de la lista, en ese momento retornamos 0 y se va restando el valor de la lista en cada llamada recursiva hasta llegar a la primera llamada recursiva donde posicion es igual a 0, por lo tanto retornamos el valor de la lista en la posicion 0,1,2,3,4,5





#en caso de que la posicion sea menor que la longitud
#retornamos el valor de la lista en la posicion actual y sumamos el valor de la lista
#en la siguiente posicion, hasta que la posicion sea igual a la longitud de la lista

#recorrido recursivo 
#verificamos que la posicion sea menor, en este caso es cero por lo tanto pasa
#en la llamada recursiva tenemos, 10 + el siguiente elemento que es 20


#2 llamada recursiva
#verificamos que la posicion sea menor, en este caso es 1, por lo tanto pasa
#retornamos 20 + el siguiente elemento que es 30

#3 llamada recursiva
#verificamos que la posicion sea menor, en este caso es 2, por lo tanto pasa
#retornamos 30 + el siguiente elemento que es 40   

#4 llamada recursiva
#verificamos que la posicion sea menor, en este caso es 3, por lo tanto pasa
#retornamos 40 + el siguiente elemento que es 50


#5 llamada recursiva
#verificamos que la posicion sea menor, en este caso es 4, por lo tanto pasa
#retornamos 50 + 0 (ya que no hay más elementos)



#recorrido recursivo
#50 + 0 = 50
#40 + 50 = 90
#30 + 90 = 120
#20 + 120 = 140
#10 + 140 = 150




#metodo recursivo para sumar numeros de 1 hasta n
#Ejercicio 2
def suma_numeros(n):
    if n == 0:
        return 0
    return n + suma_numeros(n - 1) #n-1 dado que queremos que el metodo recursivo vaya restando 1 hasta llegar a 0, en ese momento retornamos 0 y se va sumando el valor de n en cada llamada recursiva hasta llegar a la primera llamada recursiva donde n es igual a 5, por lo tanto retornamos 5 + 4 + 3 + 2 + 1 + 0 = 15

def fibonnaci(n):
    if n <= 1:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2) #n-1 y n-2 dado que queremos que el metodo recursivo vaya restando 1 y 2 hasta llegar a 0, en ese momento retornamos 0 y se va sumando el valor de n en cada llamada recursiva hasta llegar a la primera llamada recursiva donde n es igual a 5, por lo tanto retornamos 5 + 3 + 2 + 1 + 0 = 11



#metodo recursivo factorial
#Ejercicio 3 
def factorial(n): 
    if n == 0:
        return 1
    return n * factorial(n - 1) #n-1 dado que queremos que el metodo recursivo vaya restando 1 hasta llegar a 0, en ese momento retornamos 1 y se va multiplicando el valor de n en cada llamada recursiva hasta llegar a la primera llamada recursiva donde n es igual a 5, por lo tanto retornamos 5 * 4 * 3 * 2 * 1 * 1 = 120


#Ejercicio 6
def queHace(lista, posicion, valor):
    if posicion == len(lista): #la possicion debe ser menor que la longitud de la lista
        return False
    if lista[posicion] == valor: #la posicion de la lista es igual al valor que estamos buscando, retornamos True
        return True
    return queHace(lista, posicion + 1, valor) #retornamos la llamda recursiva
#que busca un valor en una lista, si lo encuentra retorna true, de caso contrario false


#Ejercicio 7
def apariciones(lista, pos, valor):
    if pos == len(lista):
        return 0
    if lista[pos] == valor:
        return 1 + apariciones(lista, pos + 1, valor)
    return apariciones(lista, pos + 1, valor)

#Ejercicio 8
def invertir(palabra):
    if len(palabra) <= 1:
        return palabra
    return invertir(palabra[1:]) + palabra[0]

#Ejercicio 9
def queHace(palabra):
    if len(palabra) <= 1: #en caso de que la long de la palabra sea menor o igual a 1, retornamos la palabra
        return palabra
    return queHace(palabra[1:]) + palabra[0] #retornamos la llamada recursiva
#toma la palabra y apartir de la segunda letra, va concatenando la primera letra al final, hasta que la palabra sea de longitud 1, en ese momento retornamos la palabra y se va concatenando la primera letra al final de la palabra hasta llegar a la primera llamada recursiva donde la palabra es igual a "RECURSION", por lo tanto retornamos "NOISURCER"





def doble_recorrido(lista, pos):
    if pos == len(lista):
        return

    print(lista[pos])
    doble_recorrido(lista, pos + 1)
    print(lista[pos]) #llamada recursiva, se va sumando 1 a la posicion hasta llegar a la longitud de la lista, en ese momento retornamos y se va imprimiendo el valor de la lista en cada llamada recursiva hasta llegar a la primera llamada recursiva donde posicion es igual a 0, por lo tanto imprimimos el valor de la lista en la posicion 0,1,2,3,4,5 y luego imprimimos el valor de la lista en la posicion 5,4,3,2,1,0





#Ejercicio 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def recorrer_recursivo(self, nodo):
        if nodo is None:
            return
        print(nodo.valor)
        self.recorrer_recursivo(nodo.siguiente)

lista = ListaSimple()
for valor in ['A', 'B', 'C', 'D', 'E']:
    lista.insertar_final(valor)
lista.recorrer_recursivo(lista.cabeza)


#palabra palindroma


def palindroma(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return palindroma(palabra[1:-1]) #en el caso de que la primera letra sea igual a la ultima
    #
    return False



print(queHace('RECURSION'))

datos = [15, 8, 23, 10, 50, 37]
print(queHace(datos, 0, 50))


numeros = [10,20,30,40,50]
print(sumar_lista(numeros, 0))
print(suma_numeros(5))


