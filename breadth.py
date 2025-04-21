from utils import successor, objective

"""
This function will take a maze, a start and goal position and return a list with the visited path using breadth-first search.
"""
def breadth_search(maze: list[list[int]], _start: tuple[int, int], _goal: tuple[int, int]) -> list[tuple[int, int]]:
    
    path: list[tuple[int, int]] = [_start] # This will be the whole path the search goes through
    to_search_from = [_start] #This will be a queue, to choose from where to search from

    row_len, col_len = len(maze), len(maze[0])

    while to_search_from:
        tmp_i_index, tmp_j_index = to_search_from.pop(0)


        # Checking the value of the neighbors
        up = maze[tmp_i_index - 1][tmp_j_index] if successor("top", i_index=tmp_i_index) else None
        down = maze[tmp_i_index + 1][tmp_j_index] if successor("down", i_index=tmp_i_index, row_len=row_len) else None
        right = maze[tmp_i_index][tmp_j_index + 1] if successor("right", j_index=tmp_j_index, col_len=col_len) else None
        left = maze[tmp_i_index][tmp_j_index - 1] if successor("left", j_index=tmp_j_index) else None

        # Checking if it's possible to move in any of the four directions
        if down in (1, 3) and (tmp_i_index + 1, tmp_j_index) not in path:
            to_search_from.append((tmp_i_index + 1, tmp_j_index))
            path.append((tmp_i_index + 1, tmp_j_index))
            if objective(tmp_i_index + 1, tmp_j_index, _goal):
                return path

        if left in (1, 3) and (tmp_i_index, tmp_j_index - 1) not in path:
            to_search_from.append((tmp_i_index, tmp_j_index - 1))
            path.append((tmp_i_index, tmp_j_index - 1))
            if objective(tmp_i_index, tmp_j_index - 1, _goal):
                return path

        if right in (1, 3) and (tmp_i_index, tmp_j_index + 1) not in path:
            to_search_from.append((tmp_i_index, tmp_j_index + 1))
            path.append((tmp_i_index, tmp_j_index + 1))
            if objective(tmp_i_index, tmp_j_index + 1, _goal):
                return path

        if up in (1, 3) and (tmp_i_index - 1, tmp_j_index) not in path:
            to_search_from.append((tmp_i_index - 1, tmp_j_index))
            path.append((tmp_i_index - 1, tmp_j_index))
            if objective(tmp_i_index - 1, tmp_j_index, _goal):
                return path
    return path


"""
This function receives the path returned by breadth_search and improves it.
Since breadth_search returns every position visited in order, but not necessarily the shortest path to the goal,
this function reconstructs the optimal path by walking backward from the goal using only valid neighbors.
"""
def improve_breadth_search_path(path: list[tuple[int, int]]) -> list[tuple[int, int]]:
    print(f"[BREADTH] Path: {path}\n")
    if not path:
        return []

    goal = path[-1]
    start = path[0]

    predecessors = {}
    for i, current in enumerate(path):
        for j in range(i - 1, -1, -1):
            prev = path[j]
            if abs(current[0] - prev[0]) + abs(current[1] - prev[1]) == 1:
                predecessors[current] = prev
                break

    current = goal
    improved = [current]
    while current != start:
        current = predecessors.get(current)
        if current is None:
            return []
        improved.append(current)

    improved.reverse()
    print(f"[BREADTH] Improved path: {improved}\n")
    return improved