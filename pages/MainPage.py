import pages.PageElements as pe
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time


class MainPage(BasePage):

    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context
        self.text = "네이버 항공권"

    def touch_naver_first_start_button(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_first_start_button)
        cl.allure_logs("첫 번째 네이버 시작하기 버튼 터치")

    def touch_later_login_button(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.later_login_button)
        cl.allure_logs("나중에 로그인 링크 텍스트 터치")

    def touch_naver_second_start_button(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_second_start_button)
        cl.allure_logs("두 번째 네이버 시작하기 버튼 터치")

    def touch_naver_tutorial_viewer(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_tutorial_viewer)
        cl.allure_logs("튜토리얼 가이드 딤드 페이지에서 화면 중앙 터치")

    def check_naver_main_page(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.naver_main_page_viewer)
        cl.allure_logs("네이버 메인 페이지 이동 확인")

    def touch_naver_search_field(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_main_search_field)
        cl.allure_logs("네이버 메인 페이지에서 검색 필드 터치")

    def input_naver_airline_text(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.naver_main_search_field_detail)
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.naver_main_search_field_detail, self.text)
        cl.allure_logs(f"검색 필드에 \"{self.text}\" 입력")

    def touch_search_icon(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_search_field_icon)
        cl.allure_logs("검색 아이콘 터치")

    def check_naver_airline_search_result(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.naver_search_result_airline)
        cl.allure_logs(f"\"{self.text}\" 검색 결과 표시 확인")

    def touch_naver_airline_link_text(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_search_result_airline)
        cl.allure_logs("\"{self.text}\" 링크 텍스트 터치")

    def check_naver_airline_page(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.naver_airline_page_top_bar)
        cl.allure_logs(f"{self.text} 페이지로 이동")