import requests
from bs4 import BeautifulSoup


# from selenium import webdriver

# driver = webdriver.Chrome('C:\\Users\\kang6\\OneDrive\\동아리-Devsign\\프로젝트\\chromedriver.exe')

###############################################################
# robot.txt를 준수                                             #
#                                                             #
# Baekjoon Online Judge : https://www.acmicpc.net/robots.txt  #
# Solved ac : There isn't robots.txt                          #
###############################################################

class Crawl:  # 크롤링 클래스

    def __init__(self, prb_num: int = 10831):
        self.prb_num = prb_num
        self.contents: dict = {
            'num': self.prb_num,
            'tier': "",
            'title': "",
            'description': []
        }

        self.BOJ_URL = f'https://www.acmicpc.net/problem/{self.prb_num}'  # BOJ 주소
        self.SOL_URL = 'https://solved.ac/search'  # Solved.ac 주소

        self.BOJ_resp = requests.get(self.BOJ_URL, {})
        self.SOL_resp = requests.get(self.SOL_URL, {'query': self.prb_num})

        # 파싱된 html 문서를 담을 변수
        self.BOJ_soup = ""
        self.SOL_soup = ""

        self.get_data()     # 크롤링 시작

    def check_state_code(self) -> bool:  # request가 정상적으로 작동했는지 확인
        if self.BOJ_resp.status_code != 200 or self.SOL_resp.status_code != 200:
            raise Exception('ERROR: 404 Not Found')
        else:
            return True

    def parsing_html(self) -> bool:     # 응답 코드(request.stae_code()) 체크 후 parsing
        try:
            if self.check_state_code() is True:  # 정상적인 응답이면 parsing 후 저장
                self.BOJ_soup = BeautifulSoup(self.BOJ_resp.text, 'html.parser')
                self.SOL_soup = BeautifulSoup(self.SOL_resp.text, 'html.parser')
                return True
        except Exception as err:
            self.contents['num'] = '존재하지 않는 문제번호입니다.'
            self.contents['title'] = err.args[0]    # 예외 메시지를 문제 제목란에 저장
            print(err)
            return False

    def get_data(self):  # 크롤링 메소드
        if self.parsing_html():
            self.contents['title'] = self.BOJ_soup.select('#problem_title')[0].string  # 문제 제목 저장

            self.contents['description'] = []  # 문제 설명을 문단별로 저장
            for p in self.BOJ_soup.select('#problem_description > p'):
                self.contents['description'].append(p.text)

            self.contents['tier'] = \
                self.SOL_soup.select(f'a[href = "{self.BOJ_URL}"] > img')[0]['alt']  # 티어 저장

    def print_contents(self):   # 크롤링 정상 작동 확인용 메소드
        print('티어 :', self.contents['tier'], end='\n\n')
        print('문제 이름 : ', self.contents['title'], end='\n\n')
        print('문제 설명 : ')
        for discript in self.contents['description']:
            print(' ', discript, end='\n\n')


if __name__ == '__main__':  # 크롤링 정상 작동 확인용
    prb_num = int(input('문제 번호 : '))
    Crawl(prb_num).print_contents()
