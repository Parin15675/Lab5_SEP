import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class SimpleDrawingWindow(QWidget):
    def __init__(self):
        super().__init__()  
        self.setWindowTitle("Simple GitHub Drawing")

        
        self.rabbit = QPixmap("images/rabbit.png")
        if self.rabbit.isNull():
            print("Image not found! Check the path.")

    def paintEvent(self, e):  
        p = QPainter(self)  

        
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(QPolygon([
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150)
        ]))

        
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        
        p.drawPolygon(QPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)
        ]))

        
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)

        p.setPen(QColor(0, 0, 0))  
        p.setBrush(QColor(255, 0, 0))  
        p.drawEllipse(100, 100, 200, 200)

        
        p.setPen(QColor(0, 127, 0))  
        p.setBrush(QColor(0, 127, 0))  
        p.drawEllipse(160, 50, 40, 60)

        
        p.setPen(QColor(139, 69, 19))  
        p.setBrush(QColor(139, 69, 19))  
        p.drawRect(190, 60, 20, 40)

        p.setPen(QColor(255, 0, 0))
        p.setBrush(QColor(255, 0, 0))
        p.drawEllipse(50, 250, 100, 140)  

        
        p.setPen(QColor(255, 255, 0))
        for x in range(60, 140, 20):  
            for y in range(270, 370, 20):  
                p.drawEllipse(x, y, 5, 5)

        
        p.setPen(QColor(0, 127, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(QPolygon([
            QPoint(100, 250), QPoint(80, 230), QPoint(120, 230)
        ]))
        p.drawPolygon(QPolygon([
            QPoint(100, 250), QPoint(70, 240), QPoint(130, 240)
        ]))

def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
