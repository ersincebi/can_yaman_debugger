import os
import sys
from time import sleep

def get_folder():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return '.'

def get_files(folder):
    files = []

    for r, d, f in os.walk(folder):
        for file in f:
            files.append(os.path.join(r, file))

    return files

def main(files):
    while True:
        for f in files:
            with open(f, 'r', encoding="ISO-8859-1") as file:
                data = file.read()
                print(data)
                sleep(0.2)


if __name__ == '__main__':
    folder = get_folder()
    files = get_files(folder)

    main(files)
