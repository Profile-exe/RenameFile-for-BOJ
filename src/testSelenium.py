from selenium import webdriver

if __name__ == '__main__':
    prb_num = input('문제번호:')
    driver = webdriver.Chrome('C:\\Users\\kang6\\OneDrive\\동아리-Devsign\\프로젝트\\chromedriver.exe')
    # 웹드라이버 실행 경로 chromedriver는 폴더가 아니라 파일명입니다.
    driver.get(f'https://www.acmicpc.net/problem/{prb_num}')

    if driver.find_element_by_class_name('show-spoiler').text == '보기':
        driver.find_element_by_class_name('show-spoiler').click()

    print(driver.find_element_by_class_name('show-spoiler').text)
