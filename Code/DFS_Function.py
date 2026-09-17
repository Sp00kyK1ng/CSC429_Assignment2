#DFS Function
def dfs(start, goal, search_space):

    #Helper function to get neighbors of a node
    def get_neighbors(position):
        if isinstance(search_space, dict):
            return search_space[position]

        row, col = position
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for row_change, col_change in movements:
            new_row = row + row_change
            new_col = col + col_change

            if (
                0 <= new_row < len(search_space)
                and 0 <= new_col < len(search_space[0])
                and search_space[new_row][new_col] != 1
            ):
                neighbors.append((new_row, new_col))

        return neighbors

    # Set up a stack and add the starting node
    frontier = [start]

    # Keep track of explored nodes
    explored = set()

    # Keep track of parent nodes
    parent = {start: None}

    # Keep track of the traversal order
    traversal_order = []

    # Continue searching while there are nodes in the stack
    while frontier:

        # Remove the last node added to the stack
        current = frontier.pop()

        # Record the traversal order
        traversal_order.append(current)

        # If we reach the goal, stop searching
        if current == goal:
            break

        # Mark the current node as explored
        explored.add(current)

        # Get the neighbors of the current node
        for neighbor in get_neighbors(current):

            # Only add nodes to queue if they are not already explored
            if neighbor not in explored and neighbor not in frontier:

                # Remember parent nodes
                parent[neighbor] = current

                # Add the node to the stack
                frontier.append(neighbor)

    # If the goal wasn't found, return no path
    if goal not in parent:
        return None, traversal_order

    # Reconstruct the path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    # Reverse the path to get start -> goal
    path.reverse()

    return path, traversal_order