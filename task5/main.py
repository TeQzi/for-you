from PyQt5 import uic, QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QMessageBox

Form, _ = uic.loadUiType("1.ui")


class Main(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.rating = 0
        self.pushButton.clicked.connect(self.check)
        self.messageBox = QMessageBox()

    def check(self):

        if self.buttonGroup.buttons()[1].isChecked():
            self.rating += 1
        if self.buttonGroup_2.buttons()[0].isChecked():
            self.rating += 1
        if self.buttonGroup_3.buttons()[0].isChecked():
            self.rating += 1

        grade = 3 if self.rating == 1 else 4

        if not self.rating:
            grade = 2
        if self.rating == 3:
            grade = 5

        QMessageBox.about(self.messageBox, "Успешно", f"Ваша оценка: {grade} ({self.rating}/3)")
        self.rating = 0

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
