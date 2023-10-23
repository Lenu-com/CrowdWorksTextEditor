from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QTextCursor
from domain.text_edit.text_formatter import TextFormatter
from typing import Final

SIZE: Final[QSize] = QSize(400, 600)

class TextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self.resize(SIZE)
        self.textChanged.connect(self.__apply_formatting)
        
    def __apply_formatting(self):
        original_text = self.toPlainText()
        formatted_text = TextFormatter().format_text(original_text)
        
        if formatted_text != original_text:
            self.textChanged.disconnect(self.__apply_formatting)
            self.setPlainText(formatted_text)
            self.moveCursor(QTextCursor.MoveOperation.End)
            self.textChanged.connect(self.__apply_formatting)
