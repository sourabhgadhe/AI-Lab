result ={}

class Graph:
    
    def __init__(self,edges,n):
        self.adj_list = [[]for _ in range(n)]
        for(src,dest) in edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)

    
def colorGraph(graph,n):
    
    for u in range (n):
        assigned = set([result.get(i) for i in graph.adj_list[u]])
        color =0

        for c in assigned:
            if (color!=c):
                break
            color=color+1

        result[u] = color

if __name__ == "__main__":
    colors = ['Blue','Green','Red','Yellow','Orange','Pink','Black','Brown','White','Purple','Violet']
    edges = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6)]
    n=7
    graph=Graph(edges,n)
    colorGraph(graph,n)

    for v in range(n):
        print(f'Colour assigned to vertex {v} is {colors[result[v]]}')  

