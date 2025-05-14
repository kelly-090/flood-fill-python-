from enum import Enum
class Direction(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

class Mice:
    __slots__ = ['cur_loc', 'pro_dir']
    def __init__(self, dir, cur_loc = None ):
        self.pro_dir = dir  # 
        if cur_loc is None :
            self.cur_loc = [0,0]
        else :
            self.cur_loc = cur_loc
    
    def make_move(self, r_increment, c_increment, maze):
        self.cur_loc[0] += r_increment
        self.cur_loc[1] += c_increment
        maze.mice_loc = self.cur_loc[:]  # Sync with Maze
        
    def get_cur_loc(self):
        return self.cur_loc
    
    def get_cur_dir(self):
        return self.pro_dir
    
    def __repr__(self):
        return f"Mice(cur_loc={self.cur_loc}, processing_direction={self.pro_dir})"
    
    def __str__(self):
        return f"Mice(cur_loc={self.cur_loc}, processing_direction={self.pro_dir})"

# class Wall :
#     __slots__ = []

class Cell :
    __slots__ = ['wall', 'visited', 'distance']
   
        
    def __init__(self, wall_d='', visited=False, distance=0):
        self.wall = [wall_d]
        self.visited = visited
        self.distance = distance
#The second __init__() method overrides the first one.

#Python only considers the last-defined method, so the first one is ignored.
        
        # wall enum : Right, Left, Top, Bottom
    def is_visited(self):
        return self.visited
    def has_wall(self) :
        return self.wall[0] is ''
    
    def get_wall(self):
        return self.wall
    
    def get_dist(self):
        return self.distance
    
    def assign_wall(self, wall_d):
        if (self.wall[0] == ''):
            self.wall[0] = wall_d
        else :
            self.wall.append(wall_d)        
        
    def set_distance(self, distance): # What is this?
        self.distance = distance    
    
    def __str__(self):
        return f"Wall: {self.wall}, Visited: {self.visited}, Distance: {self.distance}" 
    # self.wall is a str, but self.visited is a bool, and self.distance is an int.
    # You cannot use + between different data types.
    
    def __repr__(self):
        return f"Cell('{self.wall}', {self.visited}, {self.distance})"
        
import random
  
class Maze :
    __slots__ = ['table', 'mice_loc']
    
    def __init__(self, start_p=[0,0]):
        self.table = [ [None for _ in range(16)] for _ in range(16)]
        self.mice_loc = start_p
    # should I make a dictionary?
    
    def get_cur_cell(self):
        return self.table[self.mice_loc[0]][self.mice_loc[1]]
    
    def get_cur_cell_dist(self):
        return self.table[self.mice_loc[0]][self.mice_loc[1]].get_dist()
    
    def get_cur_r_cell_dist(self):
        if self.mice_loc[1] ==15:
            print("There is no more right cell.")
            return float('inf') 
            
        else :
            return self.table[self.mice_loc[0]][self.mice_loc[1]+1].get_dist()
    
    def get_cur_b_cell_dist(self):
        if (self.mice_loc[0] ==15): 
            print("There is no more bottom cell.")
            return float('inf') 
        else :
            return self.table[self.mice_loc[0]+1][self.mice_loc[1]].get_dist()
    
    def get_cur_l_cell_dist(self):
        if (self.mice_loc[1] == 0): 
            print("There is no more left cell.")
            return float('inf') 
        else :
            return self.table[self.mice_loc[0]][self.mice_loc[1]-1].get_dist()
    
    def get_cur_t_cell_dist(self):
        if (self.mice_loc[0] == 0): 
            print("There is no more top cell.")
            return float('inf') 
        else :
            return self.table[self.mice_loc[0]-1][self.mice_loc[1]].get_dist()
    
    def get_mice_loc(self):
        return self.mice_loc 
    
    def assign(self):
        for i in range(16) :
            for j in range(16):
                self.table[i][j] = Cell()
                
    def get_cell(self, r, c):
        return self.table[r][c]
                
    def basic_distance_set(self):
        self.table[7][7].assign_wall(Direction.LEFT)
        self.table[7][7].assign_wall(Direction.TOP)
        self.table[7][8].assign_wall(Direction.TOP)
        self.table[7][8].assign_wall(Direction.RIGHT)
        self.table[8][7].assign_wall(Direction.BOTTOM)
        self.table[8][8].assign_wall(Direction.RIGHT)
        self.table[8][8].assign_wall(Direction.BOTTOM)
        
        self.table[15][0].assign_wall(Direction.LEFT)
        self.table[15][0].assign_wall(Direction.RIGHT)
        self.table[15][0].assign_wall(Direction.BOTTOM)
        
        time = random.randint(0,900)
        num1 = random.randint(0, 16)
        num2 = random.randint(0, 16)
        
        
        for i in range(time) :
            num1 = random.randint(0, 16)
            num2 = random.randint(0, 16)
            if self.table[num1][num2].has_wall() :
                continue
            else :
                num3 = random.randint(1, 5)
                self.table[num1][num2].assign_wall(Direction(num3))
        
        for i in range(7) :
            for j in range(9) :
                cell = self.table[8-j][6-i]
                cell.update_distance(i+j+1)
                
        for i in range(7):
            for j in range(8, 16) :
                cell = self.table[j][6-i]
                cell.update_distance(i+j-6)
                
        for i in range(7, 16):
            for j in range(6):
                cell = self.table[6-j][i]
                cell.update_distance(i+j-9)
        
        for i in range(9, 16):
            cell = self.table[7][i]
            cell.update_distance(i-2)
        
        for i in range(9, 16):
            cell = self.table[8][i]
            cell.update_distance(i-3)
            
        for i in range(7, 16):
            for j in range(9, 16):
                cell = self.table[j][i]
                cell.update_distance(i+j-13)
            #cell.update_distance(i-2)
        # row & col
                
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.table])
    
    def update_distance(self):
        return None 

#    def __str__():
#       return 
        
# array visited = []
# visited.append()
            
    # def is_valid() :
    
def main() :
    maze = Maze()
    maze.assign()
    maze.basic_distance_set()
    print(maze)
    mice = Mice(Direction.TOP, [15,0])
    print(mice)
    
    # print(Direction(2)) = Direction.RIGHT
    # 

main()