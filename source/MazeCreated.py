import os
def get_dir(filename):
    print(filename)
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    directory = os.path.join(fileDir, f'input/{filename}')
    return directory

def get_directory_file(filename):
    def open_file(directory):
        filehandle = open(directory, "w")
        filehandle.close()
    directory = get_dir(filename)
    open_file(directory)
    return directory

def output():
    os.mkdir("output")
    os.makedirs("output/bfs/level_1")
    os.makedirs("output/dfs/level_1")
    os.makedirs("output/ucs/level_1")
    os.makedirs("output/gbfs/level_1")
    os.makedirs("output/astar/level_1")


#main
def create_Map_Lv1():
    try:
        os.makedirs("input/level_1")
    except:
        pass
    path = "level_1/"
    with open(get_directory_file(path + "text1.txt"), 'w') as outfile:
        outfile.write('0\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x    S                            x\n')
        outfile.write('x                  xxxxxxxxxxxxxxxx\n')
        outfile.write('xxxxxxxxxxxx                      x\n')
        outfile.write('x                  x              x\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxx      x\n')
        outfile.write('                                  x\n')
        outfile.write('xxxxxxxxxxx        xxxxxx         x\n')
        outfile.write('x         x             x         x\n')
        outfile.write('x                       xx        x\n')
        outfile.write('x         x      xxxxxxxx         x\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')