import Maze
import MazeCreated as MC
MC.create_Map_Lv1()
try:
    MC.output()
except:
    pass
bonus, matrix, start_point, end_point = Maze.get_data_from_file(
    "level_1/text1.txt")
maze = Maze.Maze(matrix, bonus, start_point, end_point)
maze.ucs()
maze.run_game(["level_1","text1"])
