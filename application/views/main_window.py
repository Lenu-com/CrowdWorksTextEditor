from views.widgets.text_edit import TextEdit
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize
from typing import Final

class MainWindow(QMainWindow):
    TITLE: Final[str] = 'CrowdWorksTextEditor'
    SIZE: Final[QSize] = QSize(400, 600)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.TITLE)
        self.resize(self.SIZE)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(TextEdit())
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)