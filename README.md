# FileName-for-BOJ
Change the name of the file when you enter the problem number.

## ❗robots.txt❗
* 해당 프로젝트는 Baekjoon Online Judge의 https://www.acmicpc.net/robots.txt 에 서술된 **robots.txt**를 준수합니다.

## 동기
 문제를 해결한 뒤 소스코드를 저장할 때, 해당 문제의 난이도(solved ac기준)와 문제 제목을 매번 쳐주기 귀찮았다.\
그래서, 문제 번호를 입력하면 해당 문제에 대한 정보를 파일명에 기록할 수 있는 프로그램을 만들어보려한다.

## 필요 기능
* **크롤링**: 해당 문제의 웹페이지를 크롤링하여 필요한 데이터[티어, 번호, 이름]를 얻는다.
* **파일 I/O**: 얻은 데이터로 파일명을 바꾼다.
* **GUI**: GUI를 활용하여 편의성을 높인다.

## 방법
* 문제 번호 및 제목, 설명은 BOJ에서 크롤링
* 문제 난이도(티어)는 solved ac에서 크롤링

## TODO
* ~~입력한 문제 번호에 따라 크롤링~~
* ~~문제 티어, 제목, 설명 크롤링~~
* ~~특정 디렉토리에 있는 파일명 한꺼번에 바꾸기~~
* 파일을 특정 디렉토리로 복사 및 이름 바꾸기 
* 크롤링 최적화 [Multiprocessing] 
* 파일안에 해당 문제의 주소 및 알고리즘 주석으로 추가하기 
* PyQt5를 이용해 GUI 구현
