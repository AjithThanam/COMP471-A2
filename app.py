import networkx as nx

def main():
    # val = input("Enter your value: ")
    val = '((6; 1; 2); (7; 8; 3); (5; 4; 9))'
    graph = getGraph(getTuple(val))
    temp = graph
    graph.remove_node(6)
    print(graph.nodes)
    graph.add_node(6)
    print(graph.nodes)
   


def getTuple(inputStr):
    inputStr = inputStr.replace('(','')
    inputStr = inputStr.replace(')','')
    inputStr = inputStr.replace(';',',') 
    return eval(inputStr)

def getGraph(tup):
    graph = {tup[0]: [tup[1], tup[3]],
             tup[1]: [tup[0], tup[2], tup[4]],
             tup[2]: [tup[1], tup[5]],
             tup[3]: [tup[0], tup[4], tup[6]],
             tup[4]: [tup[1], tup[3], tup[5], tup[7]],
             tup[5]: [tup[2], tup[4], tup[8]],
             tup[6]: [tup[3], tup[7]],
             tup[7]: [tup[6], tup[4], tup[8]],
             tup[8]: [tup[7], tup[5]]}
    return nx.Graph(graph)

# def getNodes(graph):
#     nodes = []
#     for node in graph:
#         nodes.append(node)
#     print(nodes)

if __name__ == '__main__':
    main()
     