#DLS Function
def dls(grid, start, goal, depth_limit):

    # Define the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Set to keep track of visited nodes
    visited = set()  
    # List to store the path from start to goal
    path = []  
    # Counter for the number of nodes expanded
    nodes_expanded = 0  
    # List to store the order in which nodes are traversed
    traversal_order = []

    def dfs(row, col, depth):
        nonlocal nodes_expanded

        #Check if position is out of bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        #Check if position is an obstacle 
        if grid[row][col] == 1:
            return False

        #Check if position has already been visited
        if (row, col) in visited:
            return False

        #Count this node as expanded
        nodes_expanded += 1
        traversal_order.append(("visit", (row, col)))

        #Add this cell to visited
        visited.add((row, col))
        path.append((row, col))

        #Check if we have reached the goal
        if (row, col) == goal:
            return True

        #Stop if we reached the depth limit
        if depth == depth_limit:
            #Add the current path to the traversal order as abandoned
            traversal_order.append(("abandoned", tuple(path)))
            # Remove the current cell from the path
            path.pop()  
            return False

        #Explore neighbors in the order: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #Up, Down, Left, Right
        #Flag to indicate if we have abandoned a branch
        branch_abandoned = False
        #Iterate through each direction to explore neighbors
        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc
            #Check if the next position is valid for exploration
            if not (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and grid[next_row][next_col] != 1
                and (next_row, next_col) not in visited
            ):
                continue
            #If we have abandoned a branch, record the current path as starting over
            if branch_abandoned:
                traversal_order.append(("starting_over", tuple(path)))
            #Recursively call dfs for the next position, increasing the depth by 1
            if dfs(row + dr, col + dc, depth + 1):
                return True

            branch_abandoned = True

        #Backtrack if no path is found from this cell
        traversal_order.append(("abandoned", tuple(path)))
        path.pop()  # Remove the current cell from the path
        return False
    
    #Start the depth-limited search from the starting position
    found = dfs(start[0], start[1], 0)

    #Return the results based on whether the goal was found
    if found:
        return path, nodes_expanded, traversal_order
    else:
        return None, nodes_expanded, traversal_order