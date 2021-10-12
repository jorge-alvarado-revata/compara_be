import networkx as nx
import matplotlib.pyplot as plt
from  networkx.algorithms import matching
from networkx.algorithms import similarity
from .models import NodoCurso
from .models import EnlaceCurso
from .models import NodoModCurso
from .models import EnlaceModCurso
from .models import Guia
from .models import PlanEstudio


# Obtiene el maximo común subgrafo componente conectado
def getMCS(g1, g2):
    matching_graph = nx.Graph()
    for n1, n2 in g2.edges():
        if g1.has_edge(n1,n2):
            matching_graph.add_edge(n1,n2)
    components = nx.connected_components(matching_graph)
    largest_component = max(components, key=len)    
    #return nx.induced_subgraph(matching_graph, largest_component)
    return nx.subgraph(matching_graph, largest_component)

#Obtiene el grafo con los nodos y enlaces comunes a ambos g1, g2
def getCS(g1,g2):
    T = nx.Graph()
    for x,y in g2.edges():
        if g1.has_edge(x,y):
            T.add_edge(x,y)
    return T

# Obtiene la distancia considerando 
# los numeros del maximo comun subgrafo conectado
def distance(num_mcs, numg1, numg2):
        return 1 - (abs(num_mcs) / max(abs(numg1), abs(numg2)))



# Devuelve una lista de tuplas con diccionarios para agregar nodos a
# un nx.graph
def nodos_by_plan(id_plan):
    res = []
    data = NodoCurso.objects.filter(plan=int(id_plan))
    for e in data:
        dic_names = {}
        dic_names['nombre'] = e.name
        tupla = (int(e.id), dic_names)
        res.append(tupla)
    return res


# Devuelve una lista de tuplas de los enlaces 
# para agregar a nodos de un nx.graph

def enlaces_by_plan(id_plan):
    res = []
    data = EnlaceCurso.objects.filter(plan=int(id_plan))
    for e in data:
        tupla = (int(e.origen), int(e.destino))
        res.append(tupla)
    return res

# factory de creacion de un nodo 

def factory_graph(id_plan):
    G = nx.Graph()
    cursos = nodos_by_plan(id_plan)
    G.add_nodes_from(cursos)
    enlaces = enlaces_by_plan(id_plan)
    G.add_edges_from(enlaces)
    return G
