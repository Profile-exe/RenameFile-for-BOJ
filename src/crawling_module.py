import requests
from bs4 import BeautifulSoup


def get_html(url):  # 해당 사이트의 html 파일을 text로 변환하여 불러온다.
	_html = ""
	resp = requests.get(url)
	if resp.status_code == 200:  # 정상적인 응답 [200] 이면 text로 변환
		_html = resp.text
	return _html


class Crawl:    # 크롤링 클래스

	def __init__(self):
		self.contents = self.crawling()

	@staticmethod
	def crawling():     # 크롤링 메소드
		prbNum = input('문제번호 : ')
		if prbNum == '':
			print('입력없음, 프로그램 종료')
			exit(0)

		BOJ_URL = "https://www.acmicpc.net/problem/{}".format(prbNum)
		BOJ_html = get_html(BOJ_URL)
		BOJ_soup = BeautifulSoup(BOJ_html, 'html.parser')

		problem_title = BOJ_soup.select('#problem_title')[0].string   # 문제 제목 저장
		problem_description = []
		for p in BOJ_soup.select('#problem_description > p'):
			problem_description.append(p.string)                  # 문제 설명을 문단별로 저장

		return {    # 딕셔너리 형태로 데이터 반환
			'title': problem_title,
			'description': problem_description
		}

	def print_contents(self):
		print()
		print('문제 이름 : ', self.contents['title'], end='\n\n')
		print('문제 내용 : ')
		for discript in self.contents['description']:
			print(' ', discript, end='\n\n')
