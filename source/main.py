import Maze
import MazeCreated as MC
import os

def count_map_in(level):
    path, dirs, files = next(os.walk(f"input/{level}"))
    file_count = len(files)

    return file_count


_map = "input5.txt"
_level = "level_1"
MC.create_Map_Lv1()
try:
    MC.output()
except:
    pass
count = count_map_in(_level)
for i in range(1,count+1,1):
    _map  = f"input{i}.txt"
    bonus, matrix, start_point, end_point = Maze.get_data_from_file(f"{_level}/{_map}")
    maze = Maze.Maze(matrix, bonus, start_point, end_point)
    maze.ucs()
    maze.run_game([_level, _map])
    maze.dfs()
    maze.run_game([_level, _map])
    maze.bfs()
    maze.run_game([_level, _map])
    maze.gbfs()
    maze.run_game([_level, _map])
    maze.astar()
    maze.run_game([_level, _map])
