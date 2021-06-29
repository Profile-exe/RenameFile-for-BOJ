# -*- coding: utf-8 -*-
import os
import sys
import re
import shutil
from crawling_module import Crawl

import PyQt5
from PyQt5.QtGui import *       # 폴더.파일의 모든 클래스, 함수, 변수 들을 불러온다.
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

RFB_UI = 'RFB.ui'
ui_path = resource_path(RFB_UI)
form_class = uic.loadUiType(ui_path)[0]

ICON = '..\\img\\icon.ico'
icon_path = resource_path(ICON)

class MainDialog(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.prb_num = 0
        self.contents: dict = {}

        self.sourceName: str = ""        # 소스파일 이름 [절대경로]
        self.dirName: str = ""           # 저장폴더 이름 [절대경로]
        self.setFixedSize(570, 630)      # 위젯 크기 고정

        self.fileLocation_pushButton.clicked.connect(self.FileButtonClicked)
        self.dirLocation_pushButton.clicked.connect(self.DirButtonClicked)
        self.start_pushButton.clicked.connect(self.StartButtonClicked)
        self.changeAll_pushButton.clicked.connect(self.ChangeAllButtonClicked)

    def FileButtonClicked(self):    # 파일 선택 버튼 슬롯
        fname: tuple = QFileDialog.getOpenFileName(self, "소스파일 선택", options=QFileDialog.DontResolveSymlinks)
        self.fileLocation_textBrowser.setText(fname[0])
        self.sourceName = fname[0].replace('/', '\\')

    def DirButtonClicked(self):     # 폴더 선택 버튼 슬롯
        fname: str = QFileDialog.getExistingDirectory(self, "저장할 폴더 선택", options=QFileDialog.ShowDirsOnly)
        self.dirLocation_textBrowser.setText(fname)
        self.dirName = fname.replace('/', '\\')

    def StartButtonClicked(self):   # 시작 버튼 슬롯
        # 문제 번호를 소스파일의 맨 첫번째 목록에서 읽어온다.
        if self.dirName == '' or self.sourceName == '':   # 파일 위치 또는 저장위치가 선택되지 않은 경우
            self.prbNum_textBrowser.setText('파일위치 또는 저장위치 미선택')
            return

        self.changeFile()   # 파일 이름 변경 후 선택된 폴더에 저장
        self.showData()     # 정보 출력

    def ChangeAllButtonClicked(self):
        file_names = os.listdir(self.dirName)  # 해당 디렉토리에 있는 파일명을 리스트로 반환
        for f in file_names:
            self.sourceName = os.path.join(self.dirName, f)
            self.changeFile()

    def changeFile(self):           # 파일 이름 변경 메소드
        try:
            with open(self.sourceName, 'r', encoding='UTF-8') as f:
                self.prb_num = re.findall('\d+', f.readline())[0]       # 소스파일 맨 첫 번째 줄에서 문제번호 읽고 저장
                self.contents: dict = Crawl(self.prb_num).contents      # 해당 번호로 크롤링
                extension = self.sourceName.split('.')[-1]    # 파일명의 확장자 유지
                new_name = f"{self.dirName}\\{self.contents['tier'].split()[0]}_{self.prb_num}_{self.contents['title']}.{extension}"
        except Exception as err:
            print(err)
            return

        if self.dirName != os.path.dirname(self.sourceName):
            cur_name = shutil.copy(self.sourceName, self.dirName)
            os.rename(cur_name, new_name)
        else:
            cur_name = self.sourceName
            os.rename(cur_name, new_name)

    def showData(self):             # GUI로 정보 출력 함수
        self.prbNum_textBrowser.setText(str(self.contents['num']))
        self.prbTier_textBrowser.setText(self.contents['tier'])
        self.prbName_textBrowser.setText(self.contents['title'])
        self.discription_textBrowser.setText(' ' + '\n\n '.join(self.contents['description']))

    """
    label.setText('<a href="http://stackoverflow.com/">Link</a>')
    label.setOpenExternalLinks(True)
    """

if __name__ == '__main__':
    app = QApplication(sys.argv)        # 프로그램을 실행시키는 역할
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()  # QApplication().exec_() : 프로그램을 이벤트 루프로 진입시키는 메서드
