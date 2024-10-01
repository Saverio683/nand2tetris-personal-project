# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

""" Translates VM commands into Hack assembly code. """

from dataclasses import dataclass

@dataclass
class CodeWriter:
    def __init__(self, output_file: list[str]) -> None:
        pass

    def set_file_name(self, name: str) -> None:
        pass

    def write_arithmetic(self, command: str) -> None:
        pass

    def write_push_pop(self, command: str, segment: str, index: int) -> int:
        pass

    def close(self) -> None:
        pass
