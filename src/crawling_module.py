import requests
from bs4 import BeautifulSoup


def get_html(url, query):  # 해당 사이트의 html 파일을 text로 변환하여 불러온다.
	_html = ""
	resp = requests.get(url, query)
	print(resp.url)
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

		# todo Solved ac URL에 dic매개변수를 줘서 티어 확인 "problem_tier"에 저장
		# 키값은 query 매개변수는 문제 번호인 prbNum 이용 ex) params
		# 티어 셀렉터 : #__next > div.contents > div:nth-child(3) > div:nth-child(2) > div > div.StickyTable__Wrapper-akg1ak-3.cWzfCw.sticky-table > div > div:nth-child(2) > div:nth-child(1) > span > a > img

		# solved ac
		SOL_URL = "https://solved.ac/search"
		SOL_html = get_html(SOL_URL, query={'query': prbNum})
		SOL_soup = BeautifulSoup(SOL_html, 'html.parser')


		# 백준 알고리즘
		BOJ_URL = "https://www.acmicpc.net/problem/{}".format(prbNum)
		BOJ_html = get_html(BOJ_URL, {})    # 백준은 dic값 필요 없음
		BOJ_soup = BeautifulSoup(BOJ_html, 'html.parser')

		problem_title = BOJ_soup.select('#problem_title')[0].string   # 문제 제목 저장
		problem_description = []
		for p in BOJ_soup.select('#problem_description > p'):
			problem_description.append(p.string)                  # 문제 설명을 문단별로 저장

		problem_tier = SOL_soup.select('#__next > div.contents > div:nth-child(3) > div:nth-child(2) > div > div.sticky-table > div.sticky-table-table > div.sticky-table-row > div.sticky-table-cell > span > a[href = "{0}"] > img'.format(BOJ_URL))[0]['alt']
		print(problem_tier)
		return {    # 딕셔너리 형태로 데이터 반환
			'tier': problem_tier,
			'title': problem_title,
			'description': problem_description
		}

	def print_contents(self):
		print()
		print('티어 :', self.contents['tier'], end='\n\n')
		print('문제 이름 : ', self.contents['title'], end='\n\n')
		print('문제 내용 : ')
		for discript in self.contents['description']:
			print(' ', discript, end='\n\n')
