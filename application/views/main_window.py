from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QSize
from typing import Final

class MainWindow(QMainWindow):
    TITLE: Final[str] = 'CrowdWorksTextEditor'
    SIZE: Final[QSize] = QSize(400, 600)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.TITLE)
        self.resize(self.SIZE)