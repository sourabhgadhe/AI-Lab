// BFS algorithm in Java

import java.util.*;

@SuppressWarnings("unchecked")

class Graph 
{

    private LinkedList<Integer> adj_nodes[];
    boolean visited[] = new boolean[100];

    // Create a graph
    Graph(int v) 
    {
        adj_nodes = new LinkedList[v];
        for (int i = 0; i < adj_nodes.length; ++i)
            adj_nodes[i] = new LinkedList<Integer>();
    }

    // Add edges to the graph
    void addEdge(int v, int w) 
    {
        adj_nodes[v].add(w);
    }

    // BFS algorithm
    void BFS(int s) 
    {

        LinkedList<Integer> queue = new LinkedList<Integer>();
        visited[s] = true;
        queue.add(s);

        while (queue.size() != 0) {
            s = queue.poll();           // removes first element from queue
            System.out.print(s + " ");
            Iterator<Integer> i = adj_nodes[s].listIterator();
            
            while (i.hasNext()) 
            {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n); 
                }
            }
        }
    }
}


public class BFS
{
    public static void main(String args[]) 
    {
        Graph g = new Graph(8);

        g.addEdge(1, 3);
        g.addEdge(1, 4);
        g.addEdge(4, 7);
        g.addEdge(4, 2);
        g.addEdge(3, 5);
        g.addEdge(5, 6);
        
        System.out.println("Following is Breadth First Traversal: ");

        g.BFS(1);
    }
}



