import os

path, dirs, files = next(os.walk("input/level_1"))
file_count = len(files)

print(file_count)