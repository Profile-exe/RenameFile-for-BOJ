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
		if prbNum == '\n':
			exit(0)

		URL = "https://www.acmicpc.net/problem/{}".format(prbNum)
		html = get_html(URL)
		soup = BeautifulSoup(html, 'html.parser')

		problem_title = soup.select('#problem_title')[0].string
		problem_description = []
		for p in soup.select('#problem_description > p'):
			problem_description.append(p.string)

		return {
			'title': problem_title,
			'description': problem_description
		}

	def print_contents(self):
		print()
		print('문제 이름 : ', self.contents['title'], end='\n\n')
		print('문제 내용 : ')
		for discript in self.contents['description']:
			print(' ', discript, end='\n\n')
