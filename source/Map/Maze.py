###################### MAZE.PY #################################
''' 
Maze.py có các chức năng như:
1. Đọc mê cung từ file.txt trong thư mục input
2. Vẽ mê cung theo yêu cầu
3. In ra mê cung
'''

# Thư viện sử dụng
# import matplotlib.pyplot as plt
from numpy import square
import MazeCreated as mc
import pygame
import os
# Global Variable
width_square = 40
# mã màu
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Wall(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], width_square, width_square)


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
        self._visited = []

        # BFS
        queue.append(start)
        visited.append({"nextdir": start, "curdir": "start"})
        self._visited.append(start)

        while queue:
            directions = []
            pop_value = queue.pop(0)
            directions.append((pop_value[0], pop_value[1]-1))  # LEFT
            directions.append((pop_value[0]+1, pop_value[1]))  # DOWN
            directions.append((pop_value[0], pop_value[1]+1))  # RIGHT
            directions.append((pop_value[0]-1, pop_value[1]))  # UP

            for nextdir in directions:
                if self._maze[nextdir[0]][nextdir[1]] != "x" and nextdir not in self._visited:
                    visited.append({"nextdir": nextdir, "curdir": pop_value})
                    queue.append(nextdir)
                    self._visited.append(nextdir)
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
                                return
                else:
                    pass

    def dfs(self):
        start = self._startpoint
        stack = []
        visited = []  # Xác định vị trị đã đi qua
        self._visited = []

        # DFS
        stack.append(start)
        visited.append({"nextdir": start, "curdir": "start"})
        self._visited.append(start)

        while stack:
            directions = []
            pop_value = stack.pop(-1)
            self._visited.append(pop_value)
            directions.insert(0,(pop_value[0], pop_value[1]-1))  # LEFT
            directions.insert(1,(pop_value[0]+1, pop_value[1]))  # DOWN
            directions.insert(2,(pop_value[0], pop_value[1]+1))  # RIGHT
            directions.insert(3,(pop_value[0]-1, pop_value[1]))  # UP

            count=0
            for nextdir in directions:
                if self._maze[nextdir[0]][nextdir[1]] != "x" and nextdir not in self._visited:
                    visited.append({"nextdir": nextdir, "curdir": pop_value})
                    stack.insert(len(stack)-count, nextdir)
                    count+=1
                    if self._endpoint == nextdir:
                        print("success")
                        # Lấy vị trí cuối cùng
                        self._route = []
                        self._route.append(self._endpoint)
                        self._visited.append(self._endpoint)
                        before_current = visited[len(visited)-1]["curdir"]
                        while (True):
                            self._route.append(before_current)
                            before_current = [
                                i["curdir"] for i in visited if i["nextdir"] == before_current]
                            before_current = before_current[0]
                            if (before_current == self._startpoint):
                                self._route.append(self._startpoint)
                                self._route.reverse()
                                return
                else:
                    pass

    def ucs(self):
        start = self._startpoint
        visited = []  # Xác định vị trị đã đi qua
        self._visited = []



    def run_game(self):
        def get_display_resolution():
            width = len(self._maze[0])*width_square + 2*len(self._maze[0])
            height = len(self._maze)*width_square + 2*len(self._maze)
            return (width, height)

        pygame.display.set_caption("Miku")
        screen = pygame.display.set_mode(
            get_display_resolution(), pygame.RESIZABLE)

        x = y = 0
        walls = []
        for row in self._maze:
            for col in row:
                if col == "x":
                    walls.append(Wall((x, y)))
                if col == "S":
                    start_rect = pygame.Rect(x, y, 40, 40)
                if col == "+":
                    bonus_rect = pygame.Rect(x+10, y+10, 20, 20)
                x += 42
            y += 42
            x = 0
        end_rect = pygame.Rect(
            self._endpoint[1]*42, self._endpoint[0]*42, 40, 40)

        visited_rects = []
        for visit in self._visited:
            visited_rects.append(pygame.Rect(
                visit[1]*42, visit[0]*42, 40, 40))

        path_rects = []
        for route in self._route:
            path_rects.append(pygame.Rect(
                route[1]*42, route[0]*42, 40, 40))

        running = True
        clock = pygame.time.Clock()
        traversal = False
        finish = False
        while running:
            # clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    running = False
            screen.fill((0, 0, 0))
            for wall in walls:
                pygame.draw.rect(screen, white, wall.rect)
            pygame.draw.rect(screen, black, end_rect)
            pygame.draw.rect(screen, red, start_rect)
            pygame.draw.rect(screen, green, bonus_rect)
            if not traversal:
                pygame.display.flip()
                for visited_rect in visited_rects:
                    pygame.draw.rect(screen, red, visited_rect)
                    pygame.display.flip()
                    clock.tick(60)
                traversal = True
                if (not finish) and traversal:
                    for route in path_rects:
                        pygame.draw.rect(screen, blue, route)
                        pygame.display.flip()
                        clock.tick(30)
            # pygame.display.flip()
        pygame.quit()


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
maze.run_game()
