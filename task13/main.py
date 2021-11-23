from PyQt5 import uic, QtWidgets, QtCore, Qt
import random


Form, _ = uic.loadUiType("1.ui")


class Main(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sum_positive)
        self.random_list()

    def random_list(self):
        self.r_list = []
        for i in range(10):
            self.r_list.append(random.randint(-50, 50))

        self.label.setText(str(self.r_list))
    def sum_positive(self):
        summa = 0
        for i in self.r_list:
            if i > 0:
                summa +=i
        self.label_2.setText("Сумма:" + str(summa))


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
        context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))


if __name__ == "__main__":
    import sys

    QtCore.qInstallMessageHandler(qt_message_handler)
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())