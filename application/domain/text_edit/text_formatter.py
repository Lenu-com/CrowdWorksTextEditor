from typing import Final

class TextFormatter:
    # full-width=1.0, half-width=0.5
    __CHAR_LIMIT: Final[float] = 15.0
    __CHAR_SIZE = {'full-width': 1.0, 'half-width': 0.5}
    __FULL_WIDTH_HEX = 0x3000
    
    def __init__(self):
        self.char_count: float = 0.0
    
    def __is_full_width(self, char: str) -> bool:
        if ord(char) <= self.__FULL_WIDTH_HEX:
            return False
        return True
    
    def __add_character_size(self, char: str) -> None:
        if self.__is_full_width(char):
            self.char_count += self.__CHAR_SIZE.get('full-width')
        else:
            self.char_count += self.__CHAR_SIZE.get('half-width')
    
    def __insert_newline(self,formatted_text: str) -> str:
        if self.char_count >= self.__CHAR_LIMIT:
            formatted_text += '\n'
            self.char_count = 0
        return formatted_text
    
    def format_text(self, text: str) -> str:
        formatted_text = ''
        
        for char in text:
            formatted_text += char
            self.__add_character_size(char)
            # TODO Consider making formatted_text a member variable
            formatted_text = self.__insert_newline(formatted_text)
            
        return formatted_text