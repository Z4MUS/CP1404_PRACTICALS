import os
import shutil


def main():
    os.chdir('FilesToSort')
    file_types = []
    sorted_file_types = {}
    for name in os.listdir('.'):
        type = (os.path.splitext(name))[-1]
        if type not in file_types:
            file_types.append(type)
    for listed_file_type in file_types:
        directory = input(f"What category would you like to sort {listed_file_type} into?")
        sorted_file_types[listed_file_type] = directory
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass
    for file_name in os.listdir('.'):
        file_type = (os.path.splitext(file_name))[-1]
        if file_type != "":
            shutil.move(file_name, sorted_file_types[file_type])


main()
