# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

""" Handles the parsing of a single .vm file, and encapsulates access to the input code. It reads VM
commands, parses them, and provides convenient access to their components. In addition, it removes all
white space and comments. """

from dataclasses import dataclass

@dataclass
class Parser:
    def __init__(self, input_file: list[str]) -> None:
        pass

    def has_more_commands(self) -> bool:
        pass

    def arg1(self) -> str:
        pass

    def arg2(self) -> int:
        pass

    def command_type(self) -> str:
        pass
