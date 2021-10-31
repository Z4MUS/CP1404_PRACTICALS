import os
import shutil


def main():
    os.chdir('FilesToSort')
    file_types = []
    for name in os.listdir('.'):
        type = (os.path.splitext(name))[-1]
        if type not in file_types:
            file_types.append(type)
    for listed_file_type in file_types:
        try:
            os.mkdir(listed_file_type)
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass
    for file_name in os.listdir('.'):
        file_type = (os.path.splitext(file_name))[-1]
        if file_type != "":
            shutil.move(file_name, file_type)


main()
