# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace

from dataclasses import dataclass

@dataclass
class Parser:
    file: list[str]
    current_command: str
    def __init__(self, file: list[str]) -> None:
        self.file = file
        if self.has_more_commands():
            self.advance()

    def has_more_commands(self) -> bool:
        return len(self.file) > 0
    
    def command_type(self) -> str:
        if '@' in self.current_command:
            return 'A_COMMAND'
        if '(' in self.current_command and ')' in self.current_command:
            return 'L_COMMAND'
        return 'C_COMMAND'
    
    def advance(self) -> None:
        self.current_command = self.file.pop(0)
        self.__clean()

    def symbol(self) -> str:
        if self.command_type() == 'A_COMMAND':
            return self.current_command.split('@', 1)[1]
        return self.current_command[self.current_command.find('(')+1:self.current_command.rfind(')')]
    
    def dest(self) -> str:
        possible_destinations = ('null', 'M', 'D', 'A', 'MD', 'AM', 'AD', 'AMD')
        result = 'null'
        if '=' in self.current_command:
            result = self.current_command.split('=',1)[0]
            assert result in possible_destinations, 'invalid qualcosa'
        return result
    
    def comp(self) -> str:
        possible_computations = ('0','1','-1','M','D','A','!M','!D','!A','-M','-D','-A','M+1','D+1','A+1', \
                               'M-1','D-1','A-1','D+A','D+M','D-A','D-M','A-D','M-D','D&A','D&M','D|A','D|M')
        result: str
        if '=' in self.current_command:
            result = self.current_command.split('=',1)[1]
        else:
            result = self.current_command.split(';',1)[0]
        assert result in possible_computations, 'invalid qualcosa'
        return result
    
    def jump(self) -> str:
        possible_jumps = ('null', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP')
        result = 'null'
        if ';' in self.current_command:
            result = self.current_command.split(';',1)[1]
            assert result in possible_jumps, 'invalid qualcosa'
        return result

    def __clean(self) -> None:
        self.current_command = self.current_command.replace(' ', '').replace('\n', '')
        if '//' in self.current_command:
            self.current_command = self.current_command.split('//', 1)[0]
        if len(self.current_command) < 1:
            self.advance()
            self.__clean()        
