import os
def get_dir(filename):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    directory = os.path.join(fileDir, 'input/level_1/{0}'.format(filename))
    return directory

def get_directory_file(filename):
    def open_file(directory):
        filehandle = open(directory, "w")
        filehandle.close()
    directory = get_dir(filename)
    open_file(directory)
    return directory

#main
with open(get_directory_file("text1.txt"), 'w') as outfile:
  outfile.write('2\n')
  outfile.write('3 6 -3\n')
  outfile.write('5 14 -20\n')
  outfile.write('xxxxxxxxxxxxxxxxxxxxxx\n')
  outfile.write('x   x   xx xx        x\n')
  outfile.write('x     x     xxxxxxxxxx\n')
  outfile.write('x x   +xx  xxxx xxx xx\n')
  outfile.write('  x   x x xx   xxxx  x\n')
  outfile.write('x          xx +xx  x x\n')
  outfile.write('xxxxxxx x      xx  x x\n')
  outfile.write('xxxxxxxxx  x x  xx   x\n')
  outfile.write('x          x x Sx x  x\n')
  outfile.write('xxxxx x  x x x     x x\n')
  outfile.write('xxxxxxxxxxxxxxxxxxxxxx')