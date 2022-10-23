import os
def get_dir(filename):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    directory = os.path.join(fileDir, 'input/{0}'.format(filename))
    return directory

def get_directory_file(filename):
    def open_file(directory):
        filehandle = open(directory, "w")
        filehandle.close()
    directory = get_dir(filename)
    open_file(directory)
    return directory

#main
def create_Map(name):
    with open(get_directory_file( name), 'w') as outfile:
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