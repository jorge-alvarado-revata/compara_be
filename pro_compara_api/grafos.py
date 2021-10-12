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

import io

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

# devuelve una lista de tuplas de el id del nodo y nombres
def labels_by_plan(id_plan):
    res = {}
    data = NodoCurso.objects.filter(plan=int(id_plan))
    for e in data:
        res[int(e.id)] = int(e.id)
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

def factory_graph_plan(id_plan):
    H = nx.Graph()
    cursos = nodos_by_plan(id_plan)
    H.add_nodes_from(cursos)
    enlaces = enlaces_by_plan(id_plan)
    H.add_edges_from(enlaces)
    return H

# Devuelve una lista de tuplas con diccionarios para agregar nodos a
# un nx.graph
def nodos_by_guia(id_guia):
    res = []
    data = NodoModCurso.objects.filter(guia=int(id_guia))
    for e in data:
        dic_names = {}
        dic_names['nombre'] = e.name
        tupla = (int(e.id), dic_names)
        res.append(tupla)
    return res

# devuelve una lista de tuplas de el id del nodo y nombres
def labels_by_guia(id_guia):
    res = {}
    data = NodoModCurso.objects.filter(guia=int(id_guia))
    for e in data:
        res[int(e.id)] = int(e.id)
    return res


# Devuelve una lista de tuplas de los enlaces 
# para agregar a nodos de un nx.graph

def enlaces_by_guia(id_guia):
    res = []
    data = EnlaceModCurso.objects.filter(guia=int(id_guia))
    for e in data:
        tupla = (int(e.origen), int(e.destino))
        res.append(tupla)
    return res

# factory de creacion de un nodo 

def factory_graph_guia(id_guia):
    G = nx.Graph()
    cursos = nodos_by_guia(id_guia)
    G.add_nodes_from(cursos)
    enlaces = enlaces_by_guia(id_guia)
    G.add_edges_from(enlaces)
    return G

# Devuelve un grafico con el resultado de la comparacion
def draw_mix_graph(H, id_plan, mcs=None, G=None):
    pos = nx.shell_layout(H)
    #pos = nx.spring_layout(H)
    d_labels = labels_by_plan(id_plan)
    nx.draw_networkx_labels(H, pos, labels=d_labels)
    nx.draw_networkx_nodes(H, pos, node_color='yellow')
    if mcs: nx.draw_networkx_nodes(H,pos, mcs.nodes, node_color='green')
    nx.draw_networkx_edges(H, pos, edge_color='blue', width=0.5)
    if G: 
        listaenlace = [(x,y) for x,y in H.edges() if G.has_edge(x,y)]
        nx.draw_networkx_edges(H, pos, edgelist=listaenlace, edge_color='orange', width=1)
    if mcs: nx.draw_networkx_edges(H, pos, edgelist=mcs.edges, edge_color='red', width=2)
    byte_image = io.BytesIO()
    plt.savefig(byte_image, format='png')
    plt.clf()
    byte_image.seek(0)
    return byte_image