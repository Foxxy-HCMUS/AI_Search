import Maze

path = "input/level_1/"
namefile = "text1"
bonus, matrix, start_point, end_point = Maze.get_data_from_file(
    "input/level_1/text1.txt")
maze = Maze.Maze(matrix, bonus, start_point, end_point)
maze.ucs()
maze.run_game(namefile+"ucs")
