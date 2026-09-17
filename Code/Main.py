#Generic BFS, DFS, and DLS implementations for both graph and grid search problems
from BFS_Function import bfs
from DFS_Function import dfs
from DLS_Function import dls

def main():
    #Define the graph as pairs of connected edges
    graph = {
        'A':['B'],
        'B':['C', 'D'],
        'C':['E'],
        'D':['F'],
        'E':[],
        'F':[]
    }

    #Define the grid as a 2D list
    #0 = Traversable, 1 = Obstacle
    #A = Start, B = Goal
    grid = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 'B', 1, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    ['A', 0, 0, 1, 1, 1],
]

    # Start and goal positions for the graph
    graph_start = 'A'
    graph_goal = 'E'

    # Start and goal positions for the grid 
    grid_start = (6, 0)
    grid_goal = (3, 3)

    #Problem 1a and 1b: Graph BFS and DFS
    print("Problem 1a: Graph BFS")
    graph_bfs_path, graph_bfs_order = bfs(graph_start, graph_goal, graph)
    print("BFS Path:", graph_bfs_path)
    print("BFS Traversal Order:", graph_bfs_order)

    print("\nProblem 1b: Graph DFS")
    graph_dfs_path, graph_dfs_order = dfs(graph_start, graph_goal, graph)
    print("DFS Path:", graph_dfs_path)
    print("DFS Traversal Order:", graph_dfs_order)

   

    #Problem 1c and 1d: Grid BFS and DFS
    print("\nProblem 1c: Grid BFS")
    grid_bfs_path, grid_bfs_order = bfs(grid_start, grid_goal, grid)
    print("BFS Path:", grid_bfs_path)
    print("BFS Traversal Order:", grid_bfs_order)

    print("\nProblem 1d: Grid DFS")
    grid_dfs_path, grid_dfs_order = dfs(grid_start, grid_goal, grid)
    print("DFS Path:", grid_dfs_path)
    print("DFS Traversal Order:", grid_dfs_order)

    #Problem 2: Depth-Limited Search (DLS)
    print("\nProblem 2: Depth-Limited Search (DLS)")
    for depth_limit in (6, 10):
        print(f"\nDLS with depth limit {depth_limit}")
        dls_path, nodes_expanded, dls_order = dls(
            grid, grid_start, grid_goal, depth_limit
        )
        if dls_path:
            print("DLS Path:", dls_path)
        else:
            print("No path found within depth limit.")
        print("Nodes Expanded:", nodes_expanded)
        print("DLS Traversal Order:")
        for event, details in dls_order:
            if event == "visit":
                print("  Visited:", details)
            elif event == "abandoned":
                print("  Abandoned path:", list(details))
            elif event == "starting_over":
                print("  Starting over from:", list(details))

if __name__ == "__main__":
    main()






