# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

class SymbolTable:
    first_avaiable_address = 16
    new_variables: dict[str, int] = {}
    
    def __init__(self) -> None:
        self.predefined_symbols = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576
        }

    def add_entry(self, symbol, address: int = first_avaiable_address) -> None:
        self.new_variables[symbol] = address
        self.first_avaiable_address += 1

    def contains(self, symbol) -> bool:
        return symbol in self.predefined_symbols or symbol in self.new_variables
    
    def get_address(self, symbol) -> bool:
        if symbol in self.predefined_symbols:
            return self.predefined_symbols[symbol]
        return self.new_variables[symbol]
