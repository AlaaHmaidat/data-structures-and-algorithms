# Graph Breadth First

Graph Breadth First is an algorithm that systematically explores all vertices in a graph, moving in breadthward motion.

## Whiteboard Process
![WhiteboardWorkflow01](../img/Graph%20Breadth%20First.jpg)

## Approach & Efficiency
### Approach
1. Create a Queue: Initialize an empty queue data structure. This queue will be used to keep track of the vertices to be visited.

2. Enqueue the Starting Node: Add the starting vertex (node) to the queue. This will be the first vertex to be visited.

3. Mark the Starting Node as Visited: To avoid revisiting the same vertex, mark the starting node as visited. You can use a separate list or set to keep track of visited nodes.

4. While the Queue is Not Empty:

    - Dequeue a vertex from the front of the queue. This vertex will be the current node to be processed.
    - Visit the dequeued vertex and perform any desired operations or collect information from it.

5. Enqueue Unvisited Neighbors:

    - Look at all the neighboring vertices of the current node.
    - If a neighbor has not been visited yet, add it to the queue, and mark it as visited.
6. Repeat Steps 4 and 5:

    - Continue the process until the queue becomes empty. This ensures all reachable vertices are visited.

7. Termination:

- The algorithm terminates when all vertices that can be reached from the starting node have been visited.

### Big O
- Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. The algorithm needs to visit each node and traverse each edge at most once.

- Space Complexity: O(V), where V is the number of vertices. In the worst case, all nodes are visited and added to the visited list.

## Solution

Click [here](./graph_breadth_first.py) to see the code 

Click [here](./test_graph_breadth_first.py) to see the code 
