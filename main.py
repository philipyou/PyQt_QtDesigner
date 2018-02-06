import sys
from my_test import *
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QToolTip, QMessageBox,QDesktopWidget, QLabel,)
from PyQt5.QtGui import QIcon, QFont, QPixmap,QPainter,QImage

from PyQt5.QtCore import  QCoreApplication, QRect


def find(str):
    print("%s"%str)


if __name__ == '__main__':

    text = """US experience shaows that, unlike traditional patents,
    software patents do not encourage innovation and R&D, quite the
    contrary.In particular they hurt small and medium-sized enterprises
    and generally newcomers in the market.They will just weaken the market
    and increase spending on patents and litigation,at the expense of
    technological innovation and research.
    """

    app = QApplication(sys.argv)
    ui = myui(text)
    ui._signal.connect(find)
    ui.show()

    #ex = Example()

    sys.exit(app.exec_())
