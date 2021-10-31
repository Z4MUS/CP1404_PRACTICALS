"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


# def get_fixed_filename(filename):
#     """Return a 'fixed' version of filename."""
#     new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
#     return new_name


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    draft_name = ((filename.split('.'))[0]).replace("_", "")
    name_parts = "".join([(" " + i if i.isupper() else i) for i in draft_name]).strip().split()
    new_name_parts = []
    new_name = ""
    for name in name_parts:
        new_word = ""
        for character in name:
            if name.index(character) == 0 or name[name.index(character) - 1] in ["(", "_"]:
                new_word += character.title()
            else:
                new_word += character
        new_name_parts.append(new_word)
    for index, name in enumerate(new_name_parts):
        if index != 0 and str(new_name_parts[index - 1]) != "(":
            new_name += "_" + name
        elif str(new_name_parts[index - 1]) == "(":
            new_name += name
        else:
            new_name += name
    new_name += '.txt'
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            os.rename(f'.\{directory_name}\{filename}', f'.\{directory_name}\{new_name}')


def cleanup_files():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            os.rename(f'.\{directory_name}\{filename}', f'.\{directory_name}\{new_name}')

# main()
# demo_walk()
cleanup_files()
