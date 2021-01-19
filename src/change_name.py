import os
import re
from crawling_module import Crawl

file_path = r'C:\Users\kang6\Documents\test'         # IDE workspace 경로
workspace_path = r'C:\Users\kang6\Documents\test'    # IDE workspace 경로
save_path = r'C:\Users\kang6\Documents\test'         # 이름 변경 후 저장할 경로

# 초기화 과정에서 크롤링 함수를 호출하므로 객체를 생성하면 문제 번호 입력 후 정보가 저장된다.
if __name__ == '__main__':
	file_names = os.listdir(file_path)        # 해당 디렉토리에 있는 파일명을 리스트로 반환

	# 파일의 이름에서 문제 번호 추출
	for name in file_names:
		prb_num = re.findall('\d+', name)[0]  # 리스트로 반환되므로 안에 있는 str요소를 저장
		crawl = Crawl(prb_num).contents       # dictionary 형태인 Crawl클래스의 contents 저장
		extension = name.split('.')[1]        # 파일명의 확장자 유지

		src = os.path.join(file_path, name)
		dst = os.path.join(file_path, f"{crawl['tier'].split()[0]}_{prb_num}_{crawl['title']}.{extension}")
		os.rename(src, dst)  # 파일명 바꾸기
