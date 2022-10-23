import os


def get_dir(filename):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    directory = os.path.join(fileDir, f'../input/{filename}')
    return directory


def get_directory_file(filename):
    def open_file(directory):
        filehandle = open(directory, "w")
        filehandle.close()
    directory = get_dir(filename)
    open_file(directory)
    return directory


def output(filename):
    try:
        os.mkdir("../output")
    except:
        pass
    os.makedirs("../output/" + f"{filename}")


# main
def create_Map_Lv1():
    try:
        os.makedirs("../input/level_1")
    except:
        pass
    path = "level_1/"
    with open(get_directory_file(path + "input1.txt"), 'w') as outfile:
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
        outfile.write('x         x      xxxxxxxx         x\n')
        outfile.write('xxxx              xxxxxxxxxxxxxxxxx\n')
        outfile.write('xxxxxxxxxxxx        xxxxxxxxxxxxxxx\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')

    with open(get_directory_file(path + "input2.txt"), 'w') as outfile:
        outfile.write('0\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x            xxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('xxxxxxx                 xxxxxxxxxxx\n')
        outfile.write('xxxxxxxxxxxxxx               S xxxx\n')
        outfile.write('xxxx              xxxxxxxxxxxxxxxxx\n')
        outfile.write('xxx                        xxxxxxxx\n')
        outfile.write('xxxxxx                            x\n')
        outfile.write('xxxxxxx                        xxxx\n')
        outfile.write('xxxxx                           xxx\n')
        outfile.write('xxxxxxx         xxx             xxx\n')
        outfile.write('xxxxxxx     xxxxxxxxxxxxx       xxx\n')
        outfile.write('xxxxxxx     xxxxxxxxxxxxx       xxx\n')
        outfile.write('xxxxxxxx                       xxxx\n')
        outfile.write('xxxxxxx       xxxx                x\n')
        outfile.write('xxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxx\n')

    with open(get_directory_file(path + "input3.txt"), 'w') as outfile:
        outfile.write('0\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x                             S   x\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('x                          xxxxx xx\n')
        outfile.write('x xxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('x xxxxx                        xxxx\n')
        outfile.write('x xxxx                          xxx\n')
        outfile.write('x     xxxxxxxx       xxxxxxxxxxxxxx\n')
        outfile.write('x xxxxx         xxx             xxx\n')
        outfile.write('x xxxxx     xxxxxxxxxxxxx       xxx\n')
        outfile.write('xxxxxxxx         xxx           xxxx\n')
        outfile.write('xxxxxxx       xxxxxxx             x\n')
        outfile.write('xxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxx\n')

    with open(get_directory_file(path + "input4.txt"), 'w') as outfile:
        outfile.write('0\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x   S                             x\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('x                          xxxxx xx\n')
        outfile.write('x xxxx               xx         xxx\n')
        outfile.write('x xxxxx              xx        xxxx\n')
        outfile.write('xxxxxxxxxxxxxx   xx  xxxxxxxxxxxxxx\n')
        outfile.write('x xxxxx         xxx             xxx\n')
        outfile.write('x xxxxx     xxxxxxxxxxxxx       xxx\n')
        outfile.write('xxxxxxxx    x  xxxxxxxxxxxxx   xxxx\n')
        outfile.write('xxxxxxx     x                     x\n')
        outfile.write('xxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxx\n')

    with open(get_directory_file(path + "input5.txt"), 'w') as outfile:
        outfile.write('0\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x                          S      x\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('xx                    xxxxxxxxxx xx\n')
        outfile.write('xxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xx\n')
        outfile.write('x                          xxxxx xx\n')
        outfile.write('x xxxxxxxxxxxx xxxx xxxxxxxxx    xx\n')
        outfile.write('x xxxxx              xx        xxxx\n')
        outfile.write('x xxxx               xx         xxx\n')
        outfile.write('xxxxxxxxxxxxxx   xx  xxxxxxxxxxxxxx\n')
        outfile.write('x                xx             xxx\n')
        outfile.write('x xxx x     xxxxxxxxxxxxx       xxx\n')
        outfile.write('xxxxx xxxxx x  xxxxxxxxxxxxx   xxxx\n')
        outfile.write('x     x            x              x\n')
        outfile.write('x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')

    with open(get_directory_file(path + "input6.txt"), 'w') as outfile:
        outfile.write('0\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x                            xxxxx\n')
        outfile.write('x                            xxxxx\n')
        outfile.write('x                                 \n')
        outfile.write('x     xxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x                           xxxxxx\n')
        outfile.write('x                           xxxxxx\n')
        outfile.write('x                           xxxxxx\n')
        outfile.write('x                           xxxxxx\n')
        outfile.write('x                           xxxxxx\n')
        outfile.write('x                           xxxxxx\n')
        outfile.write('x                           xxxxxx\n')
        outfile.write('x         xxxxxxxxxxxxxxxxxxxxxxxx\n')
        outfile.write('x S                              x\n')
        outfile.write('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
