import os
import re
from crawling_module import Crawl

file_path = r'C:\Users\kang6\Documents\test'  # IDE workspace 경로
workspace_path = r'C:\Users\kang6\Documents\test'  # IDE workspace 경로
save_path = r'C:\Users\kang6\Documents\test'  # 이름 변경 후 저장할 경로

# 초기화 과정에서 크롤링 함수를 호출하므로 객체를 생성하면 문제 번호 입력 후 정보가 저장된다.

file_names = os.listdir(file_path)  # 해당 디렉토리에 있는 파일명을 리스트로 반환

# 파일의 이름에서 문제 번호 추출
numbers = []
for name in file_names:
	numbers.append(re.findall('\d+', name))

print(numbers)

for prb_num in numbers:                # 파일에 있는 문제 번호들을 하나씩 탐색
	prb_num = prb_num[0]               # 리스트로 반환되므로 안에 있는 str요소를 저장
	crawl = Crawl(prb_num).contents    # dictionary 형태인 Crawl클래스의 contents 저장
	# todo 파일의 개수만큼 수행하므로 번호별로 내용 출력해보기 -> test폴더 파일 이름들을 존재하는 문제 번호로 변환
	print(crawl)

#
# i = 1
# for name in file_names:
# 	extension = '.' + name.split('.')[1]     # 파일명의 확장자 유지
# 	src = os.path.join(file_path, name)
# 	# todo 크롤링한 데이터로 파일 명 바꿔보기
# 	dst = f"{crawl['tier'].split()[0]}_{crawl['title']}_{crawl['description']} + {extension}"
# 	dst = os.path.join(file_path, dst)
# 	os.rename(src, dst)
# 	i += 1
