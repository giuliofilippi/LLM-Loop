# imports
import networkx as nx
import matplotlib.pyplot as plt

# function to draw the graph
def draw_graph(graph):
    '''
    graph: graph as dictionnary
    '''
    # Create a directed graph from the adjacency dictionary
    G = nx.DiGraph(graph)

    # Create a plot
    pos = nx.spring_layout(G)  # Layout algorithm for graph visualization
    nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue',
                    arrowstyle='->', arrowsize=10, font_size=12, font_color='black')

    # Show the plot
    plt.show()

# function to get neighbours of a vertex
def neighbours(v, graph):
    '''
    v: vertex
    graph: graph as dictionnary
    '''
    return list(graph[v])

# function to get the degree of a vertex
def degree(v, graph):
    '''
    v: vertex
    graph: graph as dictionnary
    '''
    return len(neighbours(v, graph))

