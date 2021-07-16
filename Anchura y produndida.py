"""
                            arbol
                            40
                           /   \
                        10      50
                       /   \    / \
                    20     30 60   70
[
    0,1,0,0,0,0,0
    1,0,1,1,0,0,0
    0,1,0,0,0,0,0
    0,1,0,0,1,0,0
    0,0,0,1,0,1,1
    0,0,0,0,1,0,0
    0,0,0,0,1,0,0
]
"""

# puse la matriz dentro de un diccionaro 
# para simular una mastriz de adyacencia vertical
# de modo que pueda las claves del diccionaro sean los nodos
matriz = {
    10: [0,1,0,0,0,0,0],
    20: [1,0,1,1,0,0,0],
    30: [0,1,0,0,0,0,0],
    40: [0,1,0,0,1,0,0],
    50: [0,0,0,1,0,1,1],
    60: [0,0,0,0,1,0,0],
    70: [0,0,0,0,1,0,0]
}
# Clase que almanacena los nodos 
# permite crea un bosque
class Nodo:
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato
# permite ingresa los nodos al arbol tomando 
# en cuenta la raiz del arbol
def insertar(raiz, nodo):
    if raiz is None:
        # si no existe una raiz crea un arbol
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)


# funcion creada para trabar con la funcion anchura()
# permite evaluar un nivel asignado del arbol
# evalua el lado derecho
def leafsDE(raiz):
    if raiz is not None:
        print(raiz.dato)


# funcion creada para trabar con la funcion anchura()
# evalua el lado izquierdo y manda al derecho
def leafsIZ(raiz):
    if raiz is not None:
        print(raiz.dato)



# inicia la evaluacion del la anchura del arbol
# toma en cuenta la raiz del arbol y el nvl 
def anchura(raiz,nvl):
    if raiz is not None:
        nvl += 1
        if nvl <= 1:
            print(raiz.dato)
        leafsIZ(raiz.izquierda)
        leafsDE(raiz.derecha)
        anchura(raiz.izquierda, nvl)
        anchura(raiz.derecha, nvl)



# debido a que se utilizo un diccionario 
# primero se debia extraer y evaluar los nodos
def IdentificaNodes():
    nodes = []
    for kei in matriz:
        if 1 in matriz.get(kei):
            # evalua si existe una arista entre nodos 
            # de ixstir una permite crear un nodo 
            # para el futuro arbol
            nodes.append(kei)
            if kei == 70:
                break
    return nodes

# permite buscar el punto medio de los nodos 
# de modo que se tome la raiz del futuro arbol
def BuscarRaiz():
    nodes = IdentificaNodes()
    return nodes[round(len(nodes)/2)-1]
        
# evlua el arobl en profundidad
def profundidad(raiz):
    if raiz is not None:
        print(raiz.dato)
        profundidad(raiz.izquierda)
        profundidad(raiz.derecha)


raiz = Nodo(BuscarRaiz())

TreeNode = IdentificaNodes()

for i in TreeNode:
    if i != 40:
        insertar(raiz, Nodo(i))


print("busqueda en anchura")
anchura(raiz, 0)
print("busqueda en profundidad")
profundidad(raiz)

