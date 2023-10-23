from typing import Final

# full-width=1.0, half-width=0.5
CHAR_LIMIT: Final[float] = 15.0
CHAR_SIZE = {'full-width': 1.0, 'half-width': 0.5}
FULL_WIDTH_HEX = 0x3000

class TextFormatter:
    def __init__(self):
        self.__char_count: float = 0.0
        self.__formatted_text = ''
    
    def __is_full_width(self, char: str) -> bool:
        if ord(char) <= FULL_WIDTH_HEX:
            return False
        return True
    
    def __add_character_size(self, char: str) -> str:
        if self.__is_full_width(char):
            self.__char_count += CHAR_SIZE['full-width']
        else:
            self.__char_count += CHAR_SIZE['half-width']
    
    def __insert_newline(self) -> None:
        if self.__char_count >= CHAR_LIMIT:
            self.__formatted_text += '\n'
            self.__char_count = 0
    
    def format_text(self, text: str) -> None:
        for char in text:
            self.__formatted_text += char
            self.__add_character_size(char)
            # TODO Consider making formatted_text a member variable
            self.__insert_newline()
        return self.__formatted_text