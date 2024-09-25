import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica(archivo_gramatica):
    reglas = {}
    with open(archivo_gramatica, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if '->' in linea:
                lado_izq, lado_der = linea.split('->')
                lado_izq = lado_izq.strip()
                lado_der = [x.strip().replace("'", "") for x in lado_der.split()]
                if lado_izq in reglas:
                    reglas[lado_izq].append(lado_der)
                else:
                    reglas[lado_izq] = [lado_der]
    return reglas

def generar_arbol(gramatica, simbolo_inicial):
    G = nx.DiGraph()  # Crear un gráfico dirigido
    nodos_visitados = set()

    def expandir_simbolo(simbolo, padre=None):
        if simbolo in nodos_visitados:  # Evitar ciclos
            return
        nodos_visitados.add(simbolo)

        if padre:
            G.add_edge(padre, simbolo)  # Agregar una arista entre el padre y el símbolo actual

        # Solo expandir si el símbolo no es terminal
        if simbolo in gramatica:
            for expansion in gramatica[simbolo]:
                for simbolo_hijo in expansion:
                    expandir_simbolo(simbolo_hijo, simbolo)

    expandir_simbolo(simbolo_inicial)
    return G

def layout_jerarquico(G, nivel=None, ancho=1., vert_gap=0.2, vert_loc=0, pos=None, padre=None, izquierda=0.5):
    """
    Genera un layout jerárquico personalizado para dibujar un árbol.
    """
    if pos is None:
        pos = {}
    if nivel is None:
        nivel = {nodo: 0 for nodo in G.nodes()}
    
    # Ubicar el nodo padre en el nivel actual
    pos[padre] = (izquierda, vert_loc)

    # Obtener los hijos del nodo actual
    vecinos = list(G.neighbors(padre))
    
    # Ajustar el ancho para los subárboles de los hijos
    if len(vecinos) != 0:
        dx = ancho / len(vecinos) 
        nextx = izquierda - ancho / 2 - dx / 2
        for vecino in vecinos:
            nextx += dx
            pos = layout_jerarquico(G, nivel, ancho=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, pos=pos, padre=vecino, izquierda=nextx)
    
    return pos

def visualizar_arbol(G):
    plt.figure(figsize=(10, 8))
    pos = layout_jerarquico(G, ancho=1.5, vert_gap=0.2, vert_loc=0, padre='S')  # Layout jerárquico personalizado
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True, arrowstyle='-|>', arrowsize=20)
    plt.show()

# Ruta al archivo de gramática
archivo_gramatica = 'gramatica.txt'
gramatica = leer_gramatica(archivo_gramatica)

# Generar el árbol a partir del símbolo inicial 'S'
simbolo_inicial = 'S'
arbol = generar_arbol(gramatica, simbolo_inicial)

# Visualizar el árbol generado
visualizar_arbol(arbol)
