# -*- coding: utf-8 -*-
# @Author  : XerCis
# @Time    : 2020/4/27 17:37
# @Function: 转换ui.ui成ui.py，转换img.qrc成.py

UI_PATH = '../asset/tpl/ui.ui'
UIPY_PATH = '../src/ui.py'
CLASSUI_PATH = '../asset/tpl/classui.ui'
CLASSUIPY_PATH = '../src/classui.py'
QRC_PATH = '../asset/img/img.qrc'
QRCPY_PATH = '../src/img_rc.py'

import subprocess

print(subprocess.run(['pyuic5', UI_PATH, '-o', UIPY_PATH]))
print(subprocess.run(['pyuic5', CLASSUI_PATH, '-o', CLASSUIPY_PATH]))
print(subprocess.run(['pyrcc5', QRC_PATH, '-o', QRCPY_PATH]))
