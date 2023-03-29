import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(1000,500)
      self.setWindowTitle("PyQt5")
      self.label = QLabel(self)
      self.label.setText("Hello World")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(16)
      self.label.setFont(font)
      self.label.move(50,20)

      self.textEdit = QTextEdit(self)
      self.textEdit.move(200,200)

      b1 = QPushButton(self)
      b1.setText("Button1")
      b1.move(100, 100)
      b1.clicked.connect(self.b1_clicked)

   def b1_clicked(self):
      f=open(self.textEdit.toPlainText(),"r")
      print(f.read())
      f.close()

def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()