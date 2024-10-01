# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

"""
The main program should construct a Parser to parse the VM input file and a CodeWriter
to generate code into the corresponding output file. It should then march through the VM commands in the
input file and generate assembly code for each one of them.
If the program’s argument is a directory name rather than a file name, the main program should process
all the .vm files in this directory. In doing so, it should use a separate Parser for handling each input file
and a single CodeWriter for handling the output.
"""

import os

from modules.parser import Parser
from modules.code_writer import CodeWriter

def main():
    input_file_path = os.path.abspath('samples/SimpleAdd.vm')
    
    with open(input_file_path, 'r', encoding='UTF-8') as f:
        file = f.readlines()
        parser = Parser(file)

main()
