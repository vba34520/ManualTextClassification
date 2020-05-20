# -*- coding: utf-8 -*-
# @Author  : XerCis
# @Time    : 2020/4/28 10:00
# @Function: program entry

import sys
import tool
import traceback
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt, QCoreApplication
from ui import Ui_MainWindow
from classui import Ui_classForm


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.tr = QCoreApplication.translate
        """Class Variables"""
        self.file = None  # document in process
        self.classAction_list = []  # class action
        self.classForm_list = []  # class form
        self.classText = {}  # class text

        """Binding Signal"""
        self.testAction.triggered.connect(self.on_test)  # test new function
        self.open.triggered.connect(self.on_open)  # open document
        self.addClass.triggered.connect(self.on_addClass)  # add a class
        self.about.triggered.connect(self.on_about)  # about
        self.save.triggered.connect(self.on_save)  # save file
        self.quit.triggered.connect(self.on_quit)  # about

        """Shortcut"""
        QShortcut(QKeySequence(Qt.Key_Space), self, self.on_nextLine)  # space to next line
        QShortcut(QKeySequence(Qt.Key_Down), self, self.on_nextLine)  # down to next line

    def on_test(self):
        print(self.classText)

    def on_open(self):
        """open document"""
        print("on_open()")
        try:
            filePath, ok = QFileDialog.getOpenFileName(self, "open", "./", "All files (*);;Text Files (*.txt)")
            if ok:
                self.statusbar.showMessage(filePath)
                self.file = open(filePath, "r", encoding="utf-8")
                self.remainLabel.setText(
                    str(len(open(filePath, encoding="utf-8").readlines())))  # display the number of remaining rows
                self.showTextEdit.setPlainText(str(self.file.readline()))
        except Exception:
            traceback.print_exc()

    def on_nextLine(self):
        """next line"""
        print("on_nextLine()")
        try:
            remain = int(self.remainLabel.text())  # remaining rows
            line = self.file.readline() if self.file else None  # read the next line
            if line == "":
                self.file.close()  # close document after finishing reading
                self.file = None
                self.statusbar.showMessage("Finish reading!")
            if self.file and remain > 0:
                self.showTextEdit.setPlainText(line)
                self.remainLabel.setText(str(remain - 1))
            else:
                self.showTextEdit.setPlainText(None)
                self.remainLabel.setText(str(0))
                self.statusbar.showMessage("Finish reading!")
        except Exception:
            traceback.print_exc()

    def on_addClass(self):
        """add a class"""
        print("on_addClass()")
        try:
            index = len(self.classAction_list)  # new class index
            className = "class{}".format(index + 1)
            action = QAction(self)
            action.setObjectName(className)
            self.toolBar.addAction(action)
            action.setText(className)
            if index < 9:
                QShortcut(QKeySequence(str(index + 1)), self,
                          lambda: self.on_nextLineToClass(index))  # shortcut is the index
                self.statusbar.showMessage("{} added, shortcut {}".format(className, str(index + 1)))
                self.classAction_list.append(action)
            self.classText.setdefault(className, [])
            action.triggered.connect(lambda: self.on_showClass(index))  # show class message
        except Exception:
            traceback.print_exc()

    def on_showClass(self, index):
        """show class message"""
        print("on_showClass()")

        def mouseDoubleClickEvent(event):
            try:
                text, ok = QInputDialog().getText(QWidget(), "修改类名", "输入新类名:")
                if ok and text:
                    classAction = self.classAction_list[index]
                    className = classAction.text()
                    self.statusbar.showMessage("{} change to {}".format(className, text))
                    classAction.setText(text)
                    classAction.setObjectName(text)
                    classForm.classLabel.setText(text)
                    form.setWindowTitle(text)
                    self.classText.setdefault(text, None)
                    self.classText[text] = self.classText.pop(className)  # change old key to new key
            except Exception:
                traceback.print_exc()

        try:
            classAction = self.classAction_list[index]
            className = classAction.text()
            form = QDialog()
            classForm = Ui_classForm()
            classForm.setupUi(form)
            classForm.classLabel.setText(className)
            classForm.classLabel.mouseDoubleClickEvent = mouseDoubleClickEvent
            content = self.classText.get(className, None)  # all content of this class
            if content:
                classForm.classTextEdit.setText("".join(content))
                tool.scroll_bottom(classForm.classTextEdit)

            form.setWindowTitle(className)
            form.setWindowModality(Qt.ApplicationModal)  # stop interact with other window
            form.show()
            form.exec_()
        except Exception:
            traceback.print_exc()

    def on_nextLineToClass(self, index):
        """allot line to different class"""
        print("on_nextLineToClass()")
        try:
            line = self.showTextEdit.toPlainText()
            self.on_nextLine()
            if line:
                className = self.classAction_list[index].text()
                self.statusbar.showMessage("{} append: {}".format(className, line))
                self.classText[className].append(line)
        except Exception:
            traceback.print_exc()

    def on_about(self):
        """about"""
        link = "https://github.com/vba34520"
        message = "<a href=%s>https://github.com/vba34520</a>" % link
        QMessageBox.about(self, "about", message)

    def on_save(self):
        """save file"""
        print("on_save()")
        try:
            dir = QFileDialog.getExistingDirectory(self, "打开目录", "../test/",
                                                   QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
            ok = tool.save_file(self.classText, rootPath=dir)
            if ok:
                self.statusbar.showMessage("saved successfully to {}".format(dir))
            else:
                self.statusbar.showMessage("nothing to save")
        except Exception:
            traceback.print_exc()

    def on_quit(self):
        exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
