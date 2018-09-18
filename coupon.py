from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import datetime
import getpass
import wget
import os
import re
import csv


class bdochrome:
    def coupon_list(self, date):
        coupon = []
        month = date[0:2]
        day = date[3:5]
        return coupon

    def coupon_list_date(self, date, directory):
        # Month-Day 파라미터에서 Month, Day 분리
        month = date[0:2]
        day = date[3:5]
        # 만약 9월 일경우 09로 나오기 때문에 0을 제거
        if month[0] == '0':
            month = month[1]
        if day[0] == '0':
            day = day[1]

        file = open(directory, 'r', encoding='utf-8')
        rdr = csv.reader(file)
        coupon_num = []

        # csv 날짜와 현재 날짜가 일치 할 경우 쿠폰 번호를 저장
        for line in rdr:
            date_regex = re.compile('\d')
            csv_month = date_regex.findall(line[0])[0]
            csv_day = date_regex.findall(line[0])[1]
            if csv_month == month and csv_day == day:
                coupon_num.append(line[1])

        file.close()
        return coupon_num;

    def confirm_state(self):
        directory = 'C:\\Users\\' + getpass.getuser() + '\\Downloads\\검은사막 쿠폰.csv'
        # 날짜 정보 확인
        now = datetime.datetime.now()
        month_day = now.strftime('%m-%d')

        # 서버 csv 다운로드
        url = 'https://docs.google.com/spreadsheets/d/1YUbIetRZtWu8N0rlMaVGNQ4z3T3LXL_rmeECb9GkAhM/export?format=csv&id=1YUbIetRZtWu8N0rlMaVGNQ4z3T3LXL_rmeECb9GkAhM&gid=0'
        if os.path.exists(directory):
            os.remove(directory)
            wget.download(url, directory)
        else:
            wget.download(url, directory)

        # Month-Day 파라미터에서 Month, Day 분리
        month = month_day[0:2]
        day = month_day[3:5]
        # 만약 9월 일경우 09로 나오기 때문에 0을 제거
        if month[0] == '0':
            month = month[1]
        if day[0] == '0':
            day = day[1]

        file = open(directory, 'r', encoding='utf-8')
        rdr = csv.reader(file)

        # csv 날짜와 현재 날짜가 일치 할 경우 쿠폰 번호를 저장
        coupon_ea = 0
        for line in rdr:
            date_regex = re.compile('\d')
            csv_month = date_regex.findall(line[0])[0]
            csv_day = date_regex.findall(line[0])[1]
            if csv_month == month and csv_day == day:
                coupon_ea = coupon_ea + 1
        if coupon_ea == 0:
            return False, 0
        else:
            return True, coupon_ea

    def launch_process(self, daumid, daumpw):
        bdo = bdochrome()

        driver = webdriver.Chrome('chromedriver.exe')
        download_directory = 'C:\\Users\\' + getpass.getuser() + '\\Downloads\\검은사막 쿠폰.csv'

        # 서버 csv 다운로드
        """url = 'https://docs.google.com/spreadsheets/d/1YUbIetRZtWu8N0rlMaVGNQ4z3T3LXL_rmeECb9GkAhM/export?format=csv&id=1YUbIetRZtWu8N0rlMaVGNQ4z3T3LXL_rmeECb9GkAhM&gid=0'
        if os.path.exists(download_directory):
            os.remove(download_directory)
            wget.download(url, download_directory)
        else:
            wget.download(url, download_directory)"""

        # csv 정보 로드
        now = datetime.datetime.now()
        month_day = now.strftime('%m-%d')
        coupon_num_list = bdo.coupon_list_date(month_day, download_directory)

        # 검은사막 로그인
        driver.get(
            "https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fblack.game.daum.net%2Fblack%2Findex.daum")
        driver.implicitly_wait(3)

        daum_id = driver.find_element_by_id('id')
        daum_id.send_keys(daumid)
        daum_pw = driver.find_element_by_id('inputPwd')
        daum_pw.send_keys(daumpw)
        sleep(0.3)
        daum_login = driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        sleep(1)

        # 쿠폰 입력 창 이동
        driver.get('http://game.daum.net/coupon/popup/register.daum?gamecode=black')
        driver.implicitly_wait(1)

        # 쿠폰 입력
        coupon_input = driver.find_element_by_id('numCoupon')

        for coupon_serial in coupon_num_list:
            coupon_input.send_keys(coupon_serial)
            coupon_input.find_element_by_xpath('//*[@id="couponRegister"]/fieldset/button').click()

        driver.find_element_by_xpath('//*[@id="couponUseLayer"]/div[2]/form/fieldset/div/a').click() #character_select
        driver.find_element_by_xpath('//*[@id="couponUseLayer"]/div[2]/form/fieldset/div/div[1]/div/ul/li[1]/a').click() #first_character_select
        driver.find_element_by_xpath('//*[@id="couponUseLayer"]/div[2]/form/fieldset/div/div[2]/div[3]/button[1]').click() #get_coupon_confirm
        alert = driver.switch_to.alert # 쿠폰 사용 확인 클릭
        alert.accept()
        sleep(0.5)
        alert = driver.switch_to.alert # 쿠폰 사용 확인 완료 클릭
        alert.accept()
        sleep(0.5)



if __name__ == "__main__":
    bdo = bdochrome()