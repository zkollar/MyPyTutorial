''' QLabel
-------------------------------------------------------------------------------
    Egyszerű egysoros szöveg.
-------------------------------------------------------------------------------
'''

import sys

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        # Label létrehozása és szövegének módosítása
        widget = QLabel("Label")    
        widget.setText("Helló")
        
        # Betűtípus módosítása és alkalmazása
        font = widget.font()        
        font.setPointSize(30)   
        widget.setFont(font)
        
        # Kép beillesztése QPixmap pixel tömb formájában
        widget.setPixmap(QPixmap("python_logo.jpg"))
        
        # Igazítás (#1)
        widget.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        # Méretezés az ablak méretéhez
        widget.setScaledContents(True) 
        
        self.setCentralWidget(widget)
    
if __name__ == '__main__':
    app = QApplication.instance() or QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    exit_code = app.exec()
    sys.exit(exit_code)

'''
     
------------------------------------------------------------------------------  
#1  Igazítás
-------------------------------------------------------------------------------    
    Qt.AlignRight       - jobbra    
    Qt.AlignLeft        - balra
    Qt.AlignHCenter     - vízszintesenközépre
    Qt.AlignJustify     - sorkizárt
    
    Qt.AlignTop         - felülre
    Qt.AlignBottom      - alulra
    Qt.AlignVCenter     - függőlegesen középre
    
    Qt.AlignCenter      - függőlegesen és vizszintesen középre
    
    Példa:
    align_top_left = Qt.AlignLeft | Qt.AlignTop
        
-------------------------------------------------------------------------------        
'''