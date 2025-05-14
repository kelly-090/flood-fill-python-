from Maze_setup import *

# Find the lowest surrounding cell distance & its direction
def lowest_sur_cell(maze):
    directions = {
        Direction.RIGHT: (maze.get_cur_r_cell_dist(), Direction.RIGHT),
        Direction.BOTTOM: (maze.get_cur_b_cell_dist(), Direction.BOTTOM),
        Direction.LEFT: (maze.get_cur_l_cell_dist(), Direction.LEFT),
        Direction.TOP: (maze.get_cur_t_cell_dist(), Direction.TOP)
    }

    valid_moves = {
        dir: dist for dir, (dist, dir_enum) in directions.items()
        if dir_enum not in maze.get_cur_cell().get_wall()  # Ignore walls
    }



    if not valid_moves:
        print("Mouse is trapped!")  
        return None, float('inf')

    best_direction = min(valid_moves, key=valid_moves.get)
    return best_direction, valid_moves[best_direction]


# Get the direction with the lowest distance
# Flood Fill Algorithm to Solve the Maze
def flood_fill(maze, mice):
    while True:
        cur_loc = mice.get_cur_loc()
        c_r, c_c = cur_loc[0], cur_loc[1]

        print(f"Mice is at: {cur_loc}")

        # Check if we reached the center (goal)
        if maze.get_cur_cell_dist() == 0:
            print("Mice reached the goal!")
            break

        # Get lowest distance direction
        best_direction, _ = lowest_sur_cell(maze)

        # Move the mouse based on the best direction
        if best_direction == Direction.RIGHT:
            mice.make_move(0, 1, maze)
        elif best_direction == Direction.BOTTOM:
            mice.make_move(1, 0, maze)
        elif best_direction == Direction.LEFT:
            mice.make_move(0, -1, maze)
        elif best_direction == Direction.TOP:
            mice.make_move(-1, 0, maze)

        # Update direction of the mice
        mice.pro_dir = best_direction

def main():
    maze = Maze()
    maze.assign()
    maze.basic_distance_set()
    print(maze)

    # Place Mice at starting point
    mice = Mice(Direction.TOP, [15, 0])  
    print(mice)

    # Solve maze using flood fill
    flood_fill(maze, mice)

main()

        
# if(cell.is_visited()) :
#     for i in range(4):
#         cell.wall[i]
