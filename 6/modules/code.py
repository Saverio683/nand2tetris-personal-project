# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

def _parse_mnemonic(mnemonic: str, data_map: dict[str, str]) -> str:
    if mnemonic in data_map:
        return data_map.get(mnemonic, '')
    raise ValueError(f'Invalid mnemonic: {mnemonic}')

def binary_comp(mnemonic: str) -> str:   
    comp_map = {
        '0': '0101010',
        '1': '011111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
        'M': '1110000',
        '!M': '1110001',
        '!D': '0001101',
        '!A': '0110001',
        '-M': '1110011',
        '-D': '0001111',
        '-A': '0110011',
        'M+1': '1110111',
        'D+1': '0011111',
        'A+1': '0110111',
        'M-1': '1110010',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D+M': '1000010',
        'D-A': '0010011',
        'D-M': '1010011',
        'A-D': '0000111',
        'M-D': '1000111',
        'D&A': '0000000',
        'D&M': '1000000',
        'D|A': '0010101',
        'D|M': '1010101'
    }     
    return _parse_mnemonic(mnemonic, comp_map)

def binary_dest(mnemonic: str) -> str:
    dest_map = {
        'null': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }
    return _parse_mnemonic(mnemonic, dest_map)

def binary_jump(mnemonic: str) -> str:
    jump_map = {
        'null': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }
    return _parse_mnemonic(mnemonic, jump_map)
