###################### MAZE.PY #################################
''' 
Maze.py có các chức năng như:
1. Đọc mê cung từ file.txt trong thư mục input
2. Vẽ mê cung theo yêu cầu
3. In ra mê cung
'''

# Thư viện sử dụng
# import matplotlib.pyplot as plt
from math import floor, sqrt
from queue import PriorityQueue
#from turtle import backward
from numpy import square
import MazeCreated as mc
import pygame
import os
from operator import itemgetter
#import pyautogui
# Global Variable
width_square = 40
# mã màu
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


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
        self._name = "bfs"
        start = self._startpoint
        queue = []
        visited = []  # Xác định vị trị đã đi qua
        self._visited = []
        go = []

        # BFS
        queue.append({"nextdir": start, "curdir": start})
        visited.append({"nextdir": start, "curdir": "start"})
        while queue:
            directions = []
            while (True):
                pop_value = queue.pop(0)
                if pop_value["nextdir"] not in self._visited:
                    self._visited.append(pop_value["nextdir"])
                    go.append(
                        {"nextdir": pop_value["nextdir"], "curdir": pop_value["curdir"]})
                    break
                else:
                    pop_value = None

            directions.append(
                (pop_value["nextdir"][0], pop_value["nextdir"][1]-1))  # LEFT
            directions.append(
                (pop_value["nextdir"][0]+1, pop_value["nextdir"][1]))  # DOWN
            directions.append(
                (pop_value["nextdir"][0], pop_value["nextdir"][1]+1))  # RIGHT
            directions.append(
                (pop_value["nextdir"][0]-1, pop_value["nextdir"][1]))  # UP

            for nextdir in directions:
                if self._maze[nextdir[0]][nextdir[1]] != "x" and nextdir not in self._visited:
                    queue.append(
                        {"nextdir": nextdir, "curdir": pop_value["nextdir"]})
                    visited.append(
                        {"nextdir": nextdir, "curdir": pop_value["nextdir"]})
                    # self._visited.append(nextdir)
                    if self._endpoint == nextdir:
                        print("success")
                        # Lấy vị trí cuối cùng
                        self._route = []
                        self._route.append(self._endpoint)
                        self._visited.append(self._endpoint)
                        before_current = go[len(go)-1]["nextdir"]
                        while (True):
                            self._route.append(before_current)
                            before_current = [
                                i["curdir"] for i in go if i["nextdir"] == before_current]
                            before_current = before_current[0]
                            if (before_current == self._startpoint):
                                self._route.append(self._startpoint)
                                self._route.reverse()
                                return
                else:
                    pass

    def dfs(self):
        self._name = "dfs"
        start = self._startpoint
        stack = []
        visited = []  # Xác định vị trị đã đi qua
        self._visited = []

        # DFS
        stack.append({"nextdir": start, "curdir": start})
        visited.append({"nextdir": start, "curdir": "start"})
        go = []
        while stack:
            directions = []
            while (True):
                pop_value = stack.pop(-1)
                if pop_value["nextdir"] not in self._visited:
                    self._visited.append(pop_value["nextdir"])
                    go.append(
                        {"nextdir": pop_value["nextdir"], "curdir": pop_value["curdir"]})
                    break
                else:
                    pop_value = None
            directions.insert(
                0, (pop_value["nextdir"][0], pop_value["nextdir"][1]-1))  # LEFT
            directions.insert(
                1, (pop_value["nextdir"][0]+1, pop_value["nextdir"][1]))  # DOWN
            directions.insert(
                2, (pop_value["nextdir"][0], pop_value["nextdir"][1]+1))  # RIGHT
            directions.insert(
                3, (pop_value["nextdir"][0]-1, pop_value["nextdir"][1]))  # UP

            count = 0
            for nextdir in directions:
                if self._maze[nextdir[0]][nextdir[1]] != "x" and nextdir not in self._visited:
                    stack.insert(
                        len(stack)-count, {"nextdir": nextdir, "curdir": pop_value["nextdir"]})
                    visited.append(
                        {"nextdir": nextdir, "curdir": pop_value["nextdir"]})
                    count += 1
                    if self._endpoint == nextdir:
                        print("success")
                        # Lấy vị trí cuối cùng
                        self._route = []
                        self._route.append(self._endpoint)
                        self._visited.append(self._endpoint)
                        before_current = go[len(go)-1]["nextdir"]
                        while (True):
                            self._route.append(before_current)
                            before_current = [
                                i["curdir"] for i in go if i["nextdir"] == before_current]
                            before_current = before_current[0]
                            if (before_current == self._startpoint):
                                self._route.append(self._startpoint)
                                self._route.reverse()
                                return
                else:
                    pass

    def ucs(self):
        self._name = "ucs"
        start = self._startpoint
        visited = []  # Xác định vị trị đã đi qua
        self._visited = []
        queue = []
        bonusdir = [i["dir"] for i in self._bonus]
        bonusreward = [i["reward"] for i in self._bonus]
        queue.append({"nextdir": start, "curdir": start, "cost": 0}),
        cost = 0
        go = []
        while (True):
            directions = []
            queue = sorted(queue, key=itemgetter('cost'))
            while (True):
                pop_value = queue.pop(0)
                if pop_value["nextdir"] not in self._visited:
                    self._visited.append(pop_value["nextdir"])
                    go.append(
                        {"nextdir": pop_value["nextdir"], "curdir": pop_value["curdir"]})
                    break
                else:
                    pop_value = None

            directions.append(
                (pop_value["nextdir"][0], pop_value["nextdir"][1]-1))  # LEFT
            directions.append(
                (pop_value["nextdir"][0]+1, pop_value["nextdir"][1]))  # DOWN
            directions.append(
                (pop_value["nextdir"][0], pop_value["nextdir"][1]+1))  # RIGHT
            directions.append(
                (pop_value["nextdir"][0]-1, pop_value["nextdir"][1]))  # UP

            for nextdir in directions:
                if self._maze[nextdir[0]][nextdir[1]] != "x" and nextdir not in self._visited:
                    cost = pop_value["cost"]
                    if nextdir in bonusdir:
                        i = bonusdir.index(nextdir)
                        cost += bonusreward[i]
                    else:
                        cost += 1
                    visited.append(
                        {"nextdir": nextdir, "curdir": pop_value["nextdir"], "cost": cost})
                    queue.append(
                        {"nextdir": nextdir, "curdir": pop_value["nextdir"], "cost": cost})
                    if self._endpoint == nextdir:
                        print("success")
                        # Lấy vị trí cuối cùng
                        self._route = []
                        self._route.append(self._endpoint)
                        self._visited.append(self._endpoint)
                        before_current = go[len(go)-1]["nextdir"]
                        while (True):
                            self._route.append(before_current)
                            before_current = [
                                i["curdir"] for i in go if i["nextdir"] == before_current]
                            before_current = before_current[0]
                            if (before_current == self._startpoint):
                                self._route.append(self._startpoint)
                                self._route.reverse()
                                return
                else:
                    pass

    def isValid(self, row: int, col: int):
        return (row >= 0) and (row < len(self._maze)) and (col >= 0) and (col < len(self._maze[0])) and self._maze[row][col] == ' '

    def heuristics(self, point, name: str) -> float:
        if name == "Manhanttan":  # Khoảng cách Manhanttan
            dx = abs(point[0] - self._endpoint[0])
            dy = abs(point[1] - self._endpoint[1])
            # chọn D = 1 là chi phí tối thiểu để di chuyển sang một ô liền kề
            return 1*(dx+dy)
        elif name == "Euclidean":
            dx = abs(point[0] - self._endpoint[0])
            dy = abs(point[1] - self._endpoint[1])
            return floor(1 * sqrt(dx * dx + dy * dy))
        elif name == "Chebyshev":
            D, D2 = 1, 1  # D2 = 1 -> Chebyshev , D2 = sqrt(2) -> Octile
            dx = abs(point[0] - self._endpoint[0])
            dy = abs(point[1] - self._endpoint[1])
            return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
        elif name == "Octile":
            D, D2 = 1, sqrt(2)  # D2 = 1 -> Chebyshev , D2 = sqrt(2) -> Octile
            dx = abs(point[0] - self._endpoint[0])
            dy = abs(point[1] - self._endpoint[1])
            return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def backward(self):
        route = []
        curr = self._endpoint
        self._route = []
        while curr != self._startpoint:
            route.append(curr)
            curr = self._visited[curr]
        route.append(self._startpoint)
        route.reverse()
        return route

    def gbfs(self):
        self._name = "gbfs"

        pQ = PriorityQueue()
        self._visited = {}
        self._route = []
        #self._visited[self._startpoint] = (self._startpoint)
        self._visited[(self._startpoint)] = (self._startpoint)
        pQ.put((0, self._startpoint))
        while not pQ.empty():
            curr = pQ.get()[1]
            # self._route.append(curr)

            if curr == self._endpoint:
                break

            #pQ = PriorityQueue()
            for i in range(4):
                row = curr[0] + rowNum[i]
                col = curr[1] + colNum[i]

                point = (row, col)
                if (self.isValid(row, col) and point not in self._visited):
                    #self._visited[(point)] = (self.heuristics((curr[0],curr[1]),"Octile"),(curr[0],curr[1]))
                    priority = self.heuristics((row, col), "Manhanttan")
                    self._visited[point] = (curr[0], curr[1])
                    pQ.put((priority, point))
        self._route = self.backward()
        # print(self._route)

    def astar(self):
        self._name = "astar"
        pQ = PriorityQueue()
        pQ.put((0, self._startpoint))

        self._visited = {}
        self._visited[(self._startpoint)] = None

        self._route = []
        cost_so_far = {}
        cost_so_far[self._startpoint] = 0

        closed = []
        # self._startpoint.g = 0
        # self._startpoint.h = 0
        #self._visited[(self._startpoint)] = self._startpoint

        while not pQ.empty():
            curr = pQ.get()[1]

            closed.append(curr)
            a = curr[0]
            b = curr[1]
            if curr == self._endpoint:
                break
            for i in range(4):
                row = curr[0] + rowNum[i]
                col = curr[1] + colNum[i]

                cost = cost_so_far[curr] + 1
                if self.isValid(row, col) and ((row, col) not in cost_so_far or cost < cost_so_far[row, col]):
                    cost_so_far[(row, col)] = cost
                    priority = cost + self.heuristics((row, col), "Manhanttan")
                    pQ.put((priority, (row, col)))
                    self._visited[(row, col)] = (curr[0], curr[1])
        self._route = self.backward()

    def run_game(self, name):
        def get_display_resolution():
            width = len(self._maze[0])*width_square + 2*len(self._maze[0])
            height = len(self._maze)*width_square + 2*len(self._maze)
            return (width, height)

        pygame.display.set_caption("Miku")
        screen = pygame.display.set_mode(
            get_display_resolution(), pygame.RESIZABLE)

        pygame.init()
        font = pygame.font.SysFont('timesnewroman', 32)
        text = font.render('Exit', True, green)
        x = y = 0
        walls = []
        bonus_rect = []
        for row in self._maze:
            for col in row:
                if col == "x":
                    walls.append(Wall((x, y)))
                if col == "S":
                    start_rect = pygame.Rect(x, y, 40, 40)
                if col == "+":
                    bonus_rect.append(pygame.Rect(x+10, y+10, 20, 20))
                x += 42
            y += 42
            x = 0
        end_rect = pygame.Rect(
            self._endpoint[1]*42, self._endpoint[0]*42, 40, 40)

        visited_rects = []
        for visit in self._visited:
            visited_rects.append(pygame.Rect(
                visit[1]*42, visit[0]*42, 40, 40))  # here  # here

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
            pygame.draw.rect(screen, yellow, start_rect)
            if bonus_rect != None:
                for bonus in bonus_rect:
                    pygame.draw.rect(screen, green, bonus)
            screen.blit(text, (self._endpoint[1]*42+5, self._endpoint[0]*42+5))
            if not traversal:
                pygame.display.flip()
                for visited_rect in visited_rects[1:]:
                    pygame.draw.rect(screen, red, visited_rect)
                    pygame.display.flip()
                    clock.tick(50)
                traversal = True
                if (not finish) and traversal:
                    for route in path_rects[1:]:
                        pygame.draw.rect(screen, blue, route)
                        pygame.display.flip()
                        clock.tick(60)
                    screen.blit(
                        text, (self._endpoint[1]*42+5, self._endpoint[0]*42+5))
                    for route in range(len(self._route)-1):
                        pygame.draw.line(screen, black, (self._route[route][1]*42+10, self._route[route][0]*42+10), (
                            self._route[route+1][1]*42+10, self._route[route+1][0]*42+10), 5)
                        pygame.display.update()
                try:
                    os.makedirs(f"output/{name[0]}/{name[1][:-4]}/{self._name}")
                except:
                    pass
                pygame.image.save(screen, f"output/{name[0]}/{name[1][:-4]}/{self._name}/" + f"{self._name}.jpg")
                with open (f"output/{name[0]}/{name[1][:-4]}/{self._name}/"+ f"{self._name}.txt", "w") as fwrite:
                    fwrite.write(str(len(self._route)))
                break
            # pygame.display.flip()
        # myScreenshot = pyautogui.screenshot()
        # myScreenshot.save("output/" + self._name + f"{self._name}_{name}.jpg")

        pygame.quit()


def get_data_from_file(file_name):
    directory = mc.get_dir(file_name)
    with open(directory, 'r') as f:
        n_bonus_points = int(next(f)[:-1])
        bonus_points = []
        if n_bonus_points != 0:
            for i in range(n_bonus_points):
                x, y, reward = map(int, next(f)[:-1].split(' '))
                bonus_points.append({"dir": (x, y), "reward": reward})
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
