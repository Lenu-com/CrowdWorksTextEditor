from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import QSize
from typing import Final

class TextEdit(QTextEdit):
    SIZE: Final[QSize] = QSize(400, 600)
    
    def __init__(self):
        super().__init__()
        self.resize(self.SIZE)