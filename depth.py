from utils import successor, objective

"""
The depth_search takes the maze, the start and goal and then returns the path used to go from the start to the goal coordinates.
"""
def depth_search(maze: list[list[int]], _start: tuple[int, int], _goal: tuple[int, int]) -> list[tuple[int, int]]:
    """
    This will be the path returned from the function.
    """
    visited_places: list[tuple[int, int]] = []
    
    """
    This will be used to go back to a node if it has reached a dead end.
    It basically saves the coordinate if the square can go to more than one square in a given position.
    """
    checkpoints: list[tuple[int, int]] = [] 

    row_len, col_len = len(maze), len(maze[0])
    i_index, j_index = _start    
    
    while True:
        if objective(i_index, j_index, _goal):
            visited_places.append(_goal)
            return visited_places
        
        """
        This is just getting the value of the squares in all four directions, while also using the lambda functions mentioned above.
        """
        up: int | None = maze[i_index - 1][j_index] if successor("top", i_index=i_index) else None
        down: int | None = maze[i_index + 1][j_index] if successor("down", i_index=i_index, row_len=row_len) else None 
        right: int | None = maze[i_index][j_index+1] if successor("right", j_index=j_index, col_len=col_len) else None
        left: int | None = maze[i_index][j_index-1] if successor("left", j_index=j_index) else None
        
        """
        This is a temporary variable that's reset in every movement. It's used to check if there's more than one possible square to go and then the
        checkpoints variable will save the point.
        """
        _checkpoints = []
        hasVisitedSomething: bool = False
        tmp_i_index, tmp_j_index = i_index, j_index
        
        
        """
        The next four if statments will check if we can move to the down, left, right or up, and then append the point to visited_places. 
        Notice that the hasVisitedSomething variable will make sure only one move per iteration is allowed.
        """
        if down in (1, 3) and successor("down", i_index=i_index, row_len=row_len) and (i_index + 1, j_index) not in visited_places:
            visited_places.append((i_index, j_index))
            i_index, j_index = i_index + 1, j_index
            hasVisitedSomething = True
            
        if left in (1, 3) and successor("left", j_index=j_index) and (i_index, j_index - 1) not in visited_places:
            if not hasVisitedSomething:
                visited_places.append((i_index, j_index))
                i_index, j_index = i_index, j_index - 1
                hasVisitedSomething = True
            
        if right in (1, 3) and successor("right", j_index=j_index, col_len=col_len) and (i_index, j_index + 1) not in visited_places:
            if not hasVisitedSomething:
                visited_places.append((i_index, j_index))
                i_index, j_index = i_index, j_index + 1
                hasVisitedSomething = True
        
        if up in (1, 3) and successor("top", i_index=i_index) and (i_index - 1, j_index) not in visited_places:
            if not hasVisitedSomething:
                visited_places.append((i_index, j_index))
                i_index, j_index = i_index - 1, j_index
                hasVisitedSomething = True
        
        
        """
        The purpouse of these four if statments is to check if there are more available nodes so we can save it in the checkpoints variable later.
        """
        if down in (1, 3) and successor("down", i_index=tmp_i_index, row_len=row_len) and (tmp_i_index + 1, tmp_j_index) not in visited_places:
            _checkpoints.append((tmp_i_index, tmp_j_index))
            
        if left in (1, 3) and successor("left", j_index=tmp_j_index) and (tmp_i_index, tmp_j_index - 1) not in visited_places:
            _checkpoints.append((tmp_i_index, tmp_j_index))
            
        if right in (1, 3) and successor("right", j_index=tmp_j_index, col_len=col_len) and (tmp_i_index, tmp_j_index + 1) not in visited_places:
            _checkpoints.append((tmp_i_index, tmp_j_index))
        
        if up in (1, 3) and successor("top", i_index=tmp_i_index) and (tmp_i_index - 1, tmp_j_index) not in visited_places:
            _checkpoints.append((tmp_i_index, tmp_j_index))
        
        
        """
        If we couldn't move, then we're coming back to our last checkpoint.
        """
        if hasVisitedSomething == False:
            visited_places.append((i_index, j_index))
            i_index, j_index = checkpoints[-1]
            checkpoints.pop()
            
        if len(_checkpoints) > 1:
            checkpoints.append(_checkpoints[0])     
            
            
"""
This function will take the path returned by the depth_search and then it will remove elements that are useless to the original path.

Just to simplify the explanation, suppose the coordinates are represented by single numbers.
Then, if the original path contains the elements [1, 8, 5, 9, 10, 3, 8, 12, 13], this function will basically delete the 
elements [5, 9, 10, 3, 8], since they are useless to the sequence, leaving only the elements [1, 8, 12, 13] 
"""            
def improve_depth_search_path(path: list[tuple[int, int]]):
    print(f"[DEPTH] Path: {path}\n")
    repeated_indices = []
    seen = {}
    for index, pos in enumerate(path):
        if pos in seen:
            repeated_indices.append((seen[pos], index))
        else:
            seen[pos] = index
    
    for start, end in sorted(repeated_indices, reverse=True):
        del path[start+1:end+1]
    
    print(f"[DEPTH] Improved path: {path}\n")
    return path