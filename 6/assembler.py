# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

import os

from modules.parser import Parser
from modules.code import binary_comp, binary_dest, binary_jump
from modules.symbol_table import SymbolTable

def main():
    input_file_path = os.path.abspath('Prog.asm')
    output_file_path = os.path.abspath('Prog.hack')
    new_file: list[str] = []
    symbol_table = SymbolTable()

    with open(input_file_path, 'r', encoding='UTF-8') as f:
        i=0
        file = f.readlines()
        parser = Parser(file)
        z = 1

        while z >= 0:
            try:
                match parser.command_type():
                    case 'L_COMMAND':
                        symbol = parser.symbol()
                        if not symbol_table.contains(symbol):
                            symbol_table.add_entry(symbol, i)
                    case _:
                        i += 1 
            except ValueError as err:
                print(err)
                return
            if z > 0:      
                parser.advance()
            if not parser.has_more_commands():
                z -= 1

    with open(input_file_path, 'r', encoding='UTF-8') as f:
        file = f.readlines()
        parser = Parser(file)
        z = 1

        while z >= 0:
            match parser.command_type():
                case 'C_COMMAND':
                    try:
                        dest = binary_dest(parser.dest())
                        comp = binary_comp(parser.comp())
                        jump = binary_jump(parser.jump())
                    except (ValueError, AssertionError) as err:
                        print(err)
                        return
                    new_file.append('111'+comp+dest+jump)
                case 'A_COMMAND':
                    symbol = parser.symbol()
                    if symbol[0].isnumeric():
                        if symbol.isnumeric():
                            symbol = int(symbol)
                            binary_value = bin(symbol).replace('b','').zfill(16)
                            new_file.append(binary_value)
                        else:
                            raise ValueError(f'Invalid number: {symbol}')
                    else:
                        if not symbol_table.contains(symbol):
                            symbol_table.add_entry(symbol)                        
                        address = symbol_table.get_address(symbol)
                        binary_value = bin(address).replace('b','').zfill(16)
                        new_file.append(binary_value)

            if z > 0:      
                parser.advance()
            if not parser.has_more_commands():
                z -= 1
                
    with open(output_file_path, 'w', encoding='UTF-8') as f:
        f.write('\n'.join(new_file))

main()
