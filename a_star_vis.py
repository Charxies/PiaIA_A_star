import networkx as nx
import matplotlib.pyplot as plt
import time
start = time.process_time()

#naturaleza de distribucion y algoritmo heuristico
def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

#generamos graph de dimensiones cuadradas
G = nx.grid_graph(dim=[6, 6])
#todos conectados
nx.set_edge_attributes(G, {e: e[1][0] * 2 for e in G.edges()}, "cost")
#se consigue la ruta y la distancia
path = nx.astar_path(G, (0, 0), (3, 5), heuristic=dist, weight="cost")
length = nx.astar_path_length(G, (0, 0), (3, 5),heuristic=dist, weight="cost")
#se imprimen
print("camino: ", path)
print("distancia de camino: ", length)

# ponemos labels y ensenamos
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="#f86e00")
edge_labels = nx.get_edge_attributes(G, "cost")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
print(time.process_time() - start)
plt.show()
