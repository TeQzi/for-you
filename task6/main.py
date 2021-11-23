from PyQt5 import uic, QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QColorDialog, QFontDialog, QFileDialog


Form, _ = uic.loadUiType("1.ui")


class Main(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.actionInputDialog.triggered.connect(self.show_input)
        self.actionQColorDialog.triggered.connect(self.show_color)
        self.actionQFontDialog.triggered.connect(self.show_font)
        self.actionQFileDialog.triggered.connect(self.show_file)
        self.actionQMessageBox.triggered.connect(self.show_msgbox)


    def show_input(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        if ok:
            pass

    def show_color(self):
        col = QColorDialog.getColor()

    def show_font(self):

        font, ok = QFontDialog.getFont()
        if ok:
            pass

    def show_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

    def show_msgbox(self):
        self.messageBox = QMessageBox()
        QMessageBox.about(self.messageBox, "ok", "ladno")

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
