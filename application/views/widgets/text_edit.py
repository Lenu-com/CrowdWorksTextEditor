from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QTextCursor
from domain.text_edit.text_formatter import TextFormatter
from typing import Final

class TextEdit(QTextEdit):
    __SIZE: Final[QSize] = QSize(400, 600)
    
    def __init__(self):
        super().__init__()
        self.resize(self.__SIZE)
        self.textChanged.connect(self.__apply_formatting)
        
    def __apply_formatting(self):
        original_text = self.toPlainText()
        formatted_text = TextFormatter().format_text(original_text)
        
        if formatted_text != original_text:
            # textChanged シグナルの一時的な切断
            self.textChanged.disconnect(self.__apply_formatting)
            
            # テキストの更新
            self.setPlainText(formatted_text)
            
            # カーソルの位置を末尾に移動（これを行わないと、テキスト変更後にカーソルが先頭に移動してしまいます）
            self.moveCursor(QTextCursor.MoveOperation.End)
            
            # textChanged シグナルの再接続
            self.textChanged.connect(self.__apply_formatting)
