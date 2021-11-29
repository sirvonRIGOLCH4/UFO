import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Управление НЛО')
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('Ufo.jpg'))
        self.image.move(150, 150)
        self.image.resize(self.image.sizeHint())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.image.move(self.image.x(), self.image.y() - 10)
        if event.key() == Qt.Key_Down:
            self.image.move(self.image.x(), self.image.y() + 10)
        if event.key() == Qt.Key_Left:
            self.image.move(self.image.x() - 10, self.image.y())
        if event.key() == Qt.Key_Right:
            self.image.move(self.image.x() + 10, self.image.y())
        if -self.image.width() + 10 > self.image.x():
            self.image.move(self.width() - 10, self.image.y())
        elif self.image.x() > self.width():
            self.image.move(-self.image.width() + 10, self.image.y())
        if -self.image.height() + 10 > self.image.y():
            self.image.move(self.image.x(), self.height() - 10)
        elif self.image.y() > self.height():
            self.image.move(self.image.x(), -self.image.height() + 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
