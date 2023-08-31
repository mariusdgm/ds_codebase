import os

def generate_structure(startpath, ignore=[]):
    """Prints the file structure of a given path

    Example usage:
    start_directory = '.'  # Current directory. You can replace '.' with your root folder path.
folders_to_ignore = [".git", "__pycache__"]  # Replace with the names of the folders you want to ignore.
generate_structure(start_directory, folders_to_ignore)
    """
    for root, dirs, files in os.walk(startpath):
        # Remove dirs in the ignore list
        dirs[:] = [d for d in dirs if d not in ignore]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


