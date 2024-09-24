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
            G.add_edge(padre, simbolo)

        if simbolo in gramatica:
            for expansion in gramatica[simbolo]:
                for simbolo_hijo in expansion:
                    expandir_simbolo(simbolo_hijo, simbolo)

    expandir_simbolo(simbolo_inicial)
    return G

def visualizar_arbol(G):
    pos = nx.spring_layout(G)  # Layout para organizar el gráfico
    plt.figure(figsize=(10, 8))
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
