#!/usr/bin/python3

"""
function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    opening the file
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        modified_lines = []
        """
        iterate through the lines.
        """
        for line in lines:
            modified_lines.append(line)
            """
            check if the search_string is found in the line.
            """
            if search_string in line:
                if not line.endswith('\n'):
                    modified_lines.append(new_string + '\n')
                else:
                    modified_lines.append(new_string)
                
        """
        rewind the file to the beginning
        """
        file.seek(0)
        file.truncate()
        file.writelines(modified_lines)
