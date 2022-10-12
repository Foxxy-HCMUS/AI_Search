###################### MAZE.PY #################################
''' 
Maze.py có các chức năng như:
1. Đọc mê cung từ file.txt trong thư mục input
2. Vẽ mê cung theo yêu cầu
3. In ra mê cung
'''

import os
import matplotlib.pyplot as plt
import MazeCreated as mc


class Maze:
    def __init__(self,  maze, bonus, start_point, end_point):
        self._bonus = bonus
        self._maze = maze  # Dùng để chứa mê cung, với mỗi 1 phần tử là 1 dòng của mê cung
        self._startpoint = start_point
        self._endpoint = end_point

    
    def bfs(self):
        start = self._startpoint
        queue = []
        visited = []  # Xác định vị trị đã đi qua
        list_visited = []

        # BFS
        queue.append(start)
        visited.append({"nextdir": start, "curdir": "start"})
        list_visited.append(start)

        while queue:
            directions = []
            pop_value = queue.pop(0)
            directions.append((pop_value[0], pop_value[1]-1))  # LEFT
            directions.append((pop_value[0]+1, pop_value[1]))  # DOWN
            directions.append((pop_value[0], pop_value[1]+1))  # RIGHT
            directions.append((pop_value[0]-1, pop_value[1]))  # UP

            for nextdir in directions:
                if self._maze[nextdir[0]][nextdir[1]] != "x" and nextdir not in list_visited:
                    visited.append({"nextdir": nextdir, "curdir": pop_value})
                    queue.append(nextdir)
                    list_visited.append(nextdir)
                    if self._endpoint == nextdir:
                        print("success")
                        # Lấy vị trí cuối cùng
                        self._route = []
                        self._route.append(self._endpoint)
                        before_current = visited[len(visited)-1]["curdir"]
                        while (True):
                            self._route.append(before_current)
                            before_current = [
                                i["curdir"] for i in visited if i["nextdir"] == before_current]
                            before_current = before_current[0]
                            if (before_current == self._startpoint):
                                self._route.append(self._startpoint)
                                self._route.reverse()
                                print(self._route)
                                return
                else:
                    pass

    def build_maze(self):
        # maze = [
        #   [] [] []
        # ]
        # => maze = row and maze[] = col
        # => xOy => maze <=> y and maze[] <=> x
        walls = [(i, j) for i in range(len(self._maze))
                 for j in range(len(self._maze[0])) if self._maze[i][j] == 'x']

        print(self._route)
        if self._route:
            direction = []
            for i in range(1, len(self._route)):
                if self._route[i][0]-self._route[i-1][0] > 0:
                    direction.append('v')  # ^
                elif self._route[i][0]-self._route[i-1][0] < 0:
                    direction.append('^')  # v
                elif self._route[i][1]-self._route[i-1][1] > 0:
                    direction.append('>')
                else:
                    direction.append('<')
            direction.pop(0)
        ax = plt.figure(dpi=100).add_subplot(111)
        for i in ['top', 'bottom', 'right', 'left']:
            ax.spines[i].set_visible(False)
        plt.scatter(
            [i[1] for i in walls], [-i[0] for i in walls],
            marker='X',
            s=100,
            color='black'
        )

        plt.scatter(
            [i[1] for i in self._bonus], [-i[0] for i in self._bonus],
            marker='P',
            s=100,
            color='green'
        )

        plt.scatter(
            self._startpoint[1], - (self._startpoint[0]),
            marker='*',
            s=100,
            color='gold'
        )
        if self._route:
            for i in range(len(self._route)-2):
                plt.scatter(self._route[i+1][1],-self._route[i+1][0],
                            marker=direction[i],color='silver')

        plt.text(self._endpoint[1], -(self._endpoint[0]), 'EXIT', color='red',
                 horizontalalignment='center',
                 verticalalignment='center')

        plt.xticks([])
        plt.yticks([])
        plt.show()



def get_data_from_file(file_name: str):
    directory = mc.get_dir(file_name)
    with open(directory, 'r') as f:
        n_bonus_points = int(next(f)[:-1])
        bonus_points = []
        for i in range(n_bonus_points):
            x, y, reward = map(int, next(f)[:-1].split(' '))
            bonus_points.append((x, y, reward))
        text = f.read()
        matrix = [list(i) for i in text.splitlines()]

        def find_start_end():
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 'S':
                        start = (i, j)
                    elif matrix[i][j] == ' ':
                        if (i == 0) or (i == len(matrix)-1) or (j == 0) or (j == len(matrix[0])-1):
                            end = (i, j)
                    else:
                        pass
            return start, end

        start_point, end_point = find_start_end()
    return bonus_points, matrix, start_point, end_point


# main
bonus, matrix, start_point, end_point = get_data_from_file("text1.txt")
maze = Maze(matrix, bonus, start_point, end_point)
maze.bfs()
maze.build_maze()
