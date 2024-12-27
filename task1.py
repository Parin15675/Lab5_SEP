import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class SimpleDrawingWindow(QWidget):
    def __init__(self):
        super().__init__()  # Use super() for cleaner inheritance
        self.setWindowTitle("Simple GitHub Drawing")

        # Correct the path to avoid loading issues
        self.rabbit = QPixmap("images/rabbit.png")
        if self.rabbit.isNull():
            print("Image not found! Check the path.")

    def paintEvent(self, e):  # Fixed method name
        p = QPainter(self)  # Initialize directly

        # Green triangle
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(QPolygon([
            QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150)
        ]))

        # Orange pie
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        # Orange triangle
        p.drawPolygon(QPolygon([
            QPoint(50, 200), QPoint(150, 200), QPoint(100, 400)
        ]))

        # Rabbit image
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)

def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
