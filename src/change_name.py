import os
from crawling_module import Crawl

file_path = r'C:\Users\kang6\Documents\test'     # IDE workspace 경로
workspace_path = r'C:\Users\kang6\Documents\test'     # IDE workspace 경로
save_path = r'C:\Users\kang6\Documents\test'          # 이름 변경 후 저장할 경로

crawl = Crawl().contents

file_names = os.listdir(file_path)
i = 1
for name in file_names:
	extension = '.' + name.split('.')[1]     # 파일명의 확장자 유지
	src = os.path.join(file_path, name)
	# todo 크롤링한 데이터로 파일 명 바꿔보기
	dst = crawl['tier'].split()[0] + crawl['title'] + crawl['description'] + extension
	dst = os.path.join(file_path, dst)
	os.rename(src, dst)
	i += 1
