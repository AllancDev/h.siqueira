import networkx as nx
import matplotlib.pyplot as plt

with open("example.txt", "r") as example:
    data = example.read()

graph = data.split('\n')

G = nx.Graph()


for x in graph: 
    a = x.split(' ')
    G.add_edge(str(a[0]), str(a[1]), weight=int(a[2]))


origem = input("Por favor digite a origem: ")
destino = input("Por favor digite a destino: ")

path = nx.shortest_path(G, source=origem, target=destino)
nx.draw(G, with_labels=True, nodelist=path, node_color='r')

plt.show()