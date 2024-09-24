
# Generador de Árboles para Gramáticas

Este proyecto genera un árbol de derivación a partir de una gramática libre de contexto, usando el símbolo inicial y mostrando las reglas de producción aplicadas. La implementación se realiza en Python y utiliza `networkx` para la creación del gráfico del árbol y `matplotlib` para su visualización.

## Archivos

### 1. `arbol_gramatica.py`
Este archivo contiene el código principal que:

- Lee las reglas de producción de una gramática desde un archivo de texto.
- Genera un árbol dirigido basado en las reglas de producción, comenzando desde el símbolo inicial.
- Visualiza el árbol utilizando `networkx` y `matplotlib`.

#### Funciones principales:
- `leer_gramatica(archivo_gramatica)`: Lee las reglas de la gramática desde un archivo de texto y las almacena en un diccionario.
- `generar_arbol(gramatica, simbolo_inicial)`: Genera un árbol de derivación a partir de las reglas de la gramática.
- `visualizar_arbol(G)`: Visualiza el árbol generado usando `matplotlib`.

### 2. `gramatica.txt`
Este archivo contiene la definición de la gramática en formato de texto. Cada regla de producción está en una línea separada con el formato `A -> B C`, donde `A` es un no terminal y `B C` pueden ser terminales o no terminales.

#### Ejemplo de gramática:
```plaintext
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'el'
N -> 'gato'
V -> 'come'
