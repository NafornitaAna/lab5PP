import sys
import sysv_ipc
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
      titlu=f.readline().strip()
      continut=""
      for line in f.readlines()[1:]:
         continut+=line
      print("titlu ",titlu,"\n continut",continut)
      g=open("/home/ana/Desktop/htmlll","w")
      g.write(f"<Html> <Head> <title> {titlu} </title> </Head> <Body>{continut} </Body> </Html>")
      try:
         # put the key (integer) as parameter (in this case: -1)
         message_queue = sysv_ipc.MessageQueue(-1)
         send_message(message_queue, f"<Html> <Head> <title> {titlu} </title> </Head> <Body>{continut} </Body> </Html>")
      except sysv_ipc.ExistentialError:
         print("Message queue not initialized. Please run the C program first")
      f.close()


def send_message(message_queue, message):
   message_queue.send(message)

def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()
