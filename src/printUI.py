# -*- coding: utf-8 -*-

import sys
from crawling_module import Crawl

import PyQt5
from PyQt5.QtGui import *       # 폴더.파일의 모든 클래스, 함수, 변수 들을 불러온다.
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

RFB_UI = '../ui/RFB.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(RFB_UI, self)

        self.sourceName: str = ""        # 소스파일 이름 [절대경로]
        self.dirName: str = ""           # 저장폴더 이름 [절대경로]
        self.contents: Crawl             # 크롤링 정보 저장
        self.setFixedSize(570, 610)

        self.fileLocation_pushButton.clicked.connect(self.FileButtonClicked)
        self.dirLocation_pushButton.clicked.connect(self.DirButtonClicked)
        self.start_pushButton.clicked.connect(self.StartButtonClicked)

    def FileButtonClicked(self):
        fname: tuple = QFileDialog.getOpenFileName(self, "소스파일 선택", options=QFileDialog.DontResolveSymlinks)
        self.fileLocation_textBrowser.setText(fname[0])
        self.sourceName = fname[0]

    def DirButtonClicked(self):
        fname: str = QFileDialog.getExistingDirectory(self, "저장할 폴더 선택", options=QFileDialog.ShowDirsOnly)
        self.dirLocation_textBrowser.setText(fname)
        self.dirName = fname

    def StartButtonClicked(self):
        prb_num = int(input('문제 번호 입력 : '))
        self.crawl = Crawl(prb_num)
        self.prbNum_textBrowser.setText(str(prb_num))
        self.prbTier_textBrowser.setText(self.crawl.contents['tier'])
        self.prbName_textBrowser.setText(self.crawl.contents['title'])
        self.discription_textBrowser.setText(' ' + '\n\n '.join(self.crawl.contents['description']))

    """
    label.setText('<a href="http://stackoverflow.com/">Link</a>')
    label.setOpenExternalLinks(True)
    """

if __name__ == '__main__':
    app = QApplication(sys.argv)        # 프로그램을 실행시키는 역할
    main_dialog = MainDialog()
    main_dialog.show()
    # QApplication().exec_() : 프로그램을 이벤트 루프로 진입시키는 메서드
    app.exec_()
