import Maze
import MazeCreated as MC
import os
import time
def count_map_in(level):
    path, dirs, files = next(os.walk(f"input/{level}"))
    file_count = len(files)

    return file_count

heuristic = ["Manhanttan", "Euclidean","Chebyshev","Octile"]
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
    start = time.time()
    maze.ucs()
    end = time.time()
    print(end-start)
    maze.run_game([_level, _map])

    start = time.time()
    maze.dfs()
    end = time.time()
    print(end-start)
    maze.run_game([_level, _map])

    start = time.time()
    maze.bfs()
    end = time.time()
    print(end-start)
    maze.run_game([_level, _map])
    
    for i in range(len(heuristic)):
        start = time.time()
        maze.gbfs(heuristic[i])
        end = time.time()
        print(end-start)
        maze.run_game([_level, _map], i+1)

        start = time.time()
        maze.astar(heuristic[i])
        end = time.time()
        print(end-start)
        maze.run_game([_level, _map], i+1)
