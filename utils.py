"""
This function will receive a maze as a parameter.
It will then iterate over its element to find the numbers '2' and '3' so that it can setup the start and goal coordinates.
The return tipe is a tuple containing the start and goal, which are also a tuple.
"""
def maze_setup(maze: list[list[int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = (-1, -1)
    goal = (-1, -1)
    for i_index, row_val in enumerate(maze):
        for j_index, col_val in enumerate(maze[i_index]):
            if col_val == 2:
                start = (i_index, j_index)
            if col_val == 3:
                goal = (i_index, j_index)

    return start, goal

"""
These four lambda functions are just checking if the next movement is allowed.
For example, if the in the next movement the square should go to the top, it checks if exists a top square to go.
"""
is_under_top_wall = lambda i_index: True if i_index - 1 >= 0 else False
is_under_bottom_wall = lambda i_index, row_len: True if i_index + 1 < row_len else False
is_under_right_wall = lambda j_index, col_len: True if j_index + 1 < col_len else False
is_under_left_wall = lambda j_index: True if j_index - 1 >= 0 else False


def successor(direction: str, i_index = None, j_index = None, row_len = None, col_len = None) -> bool:
    match direction:
        case "top":                
            return is_under_top_wall(i_index)
        case "down":
            return is_under_bottom_wall(i_index, row_len)
        case "right":
            return is_under_right_wall(j_index, col_len)
        case "left":
            return is_under_left_wall(j_index)
        
        case _:
            return False
        
"""
Test if we have reached the goal
"""
def objective(i_index: int, j_index: int, _goal: tuple[int, int]) -> bool:
    return True if (i_index, j_index) == _goal else False