import sys  #Demo3_18.py
from PySide6.QtWidgets import QApplication,QWidget,QProgressDialog
from PySide6.QtCore import QTimer

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.pd = QProgressDialog("Copying...","Cancel",0,100,self)
        self.pd.canceled.connect(self.cancel)
        self.t = QTimer(self)
        self.t.setInterval(200)
        self.t.timeout.connect(self.perform)
        self.t.start()
        self.steps=0
    def perform(self):
        self.pd.setValue(self.steps)
        self.steps = self.steps+ 1
        if self.steps > self.pd.maximum():
            self.t.stop()
    def cancel(self):
        self.t.stop()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
