from views.widgets.text_edit import TextEdit
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize
from typing import Final

TITLE: Final[str] = 'CrowdWorksTextEditor'
SIZE: Final[QSize] = QSize(400, 600)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE)
        self.resize(SIZE)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(TextEdit())
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)