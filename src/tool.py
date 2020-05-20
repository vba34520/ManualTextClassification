# -*- coding: utf-8 -*-
# @Author  : XerCis
# @Time    : 2020/4/29 11:00
# @Function: useful tools

import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor


def scroll_bottom(textEdit):
    """scroll the cursor of textEdit to bottom"""
    cursor = textEdit.textCursor()
    cursor.movePosition(QTextCursor.End)
    textEdit.setTextCursor(cursor)


def save_file(d, rootPath="./"):
    """save different txt accroding to dict"s key and value"""
    has_written = False
    if isinstance(d, dict):
        for key, value in d.items():
            if value:
                has_written = True
                filePath = os.path.join(rootPath, "{}.txt".format(key))
                with open(filePath, "w", encoding="utf-8") as f:
                    for i in value:
                        f.write(i)
    if has_written:
        return True
    return False


if __name__ == "__main__":
    d = {"class0": ["不知天上宫阙，今夕是何年。\n"], "class1": ["我欲乘风归去，又恐琼楼玉宇，高处不胜寒。\n", "不应有恨，何事长向别时圆？\n"],
         "class2": ["转朱阁，低绮户，照无眠。\n", "人有悲欢离合，月有阴晴圆缺，此事古难全。\n"], "class3": ["起舞弄清影，何似在人间。\n", "但愿人长久，千里共婵娟。"]}
    save_file(d)
