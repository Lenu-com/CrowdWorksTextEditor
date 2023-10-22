from typing import Final

class TextFormatter:
    # full-width=1.0, half-width=0.5
    __CHAR_LIMIT: Final[float] = 15.0
    __CHAR_SIZE = {'full-width': 1.0, 'half-width': 0.5}
    __FULL_WIDTH_HEX = 0x3000
    
    def __is_full_width(self, char: str) -> bool:
        if ord(char) <= self.__FULL_WIDTH_HEX:
            return False
        return True
    
    def format_text(self, text: str) -> str:
        formatted_text = ''
        char_count = 0
        
        for char in text:
            formatted_text += char
            if self.__is_full_width(char):
                char_count += self.__CHAR_SIZE.get('full-width')
            else:
                char_count += self.__CHAR_SIZE.get('half-width')
            if char_count >= self.__CHAR_LIMIT:
                formatted_text += '\n'
                char_count = 0
        return formatted_text