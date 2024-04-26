import pages.PageElements as pe
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class AirLinePage(BasePage):

    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context
        self.departure_place = "인천"
        self.arrival_place = "오사카"

    def touch_roundtrip_tap(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_airline_roundtrip_tap)
        cl.allure_logs("네이버 항공권 페이지에서 왕복 탭 터치")

    def touch_departure_menu(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_airline_departure_menu)
        cl.allure_logs("출발 장소 선택 드롭다운 메뉴 터치")

    def input_departure_place(self):
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.naver_airline_departure_search_field, self.departure_place)
        cl.allure_logs(f"출발 장소 \"{self.departure_place}\" 입력")

    def touch_departure_place(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_airline_departure_place)
        cl.allure_logs(f"\"{self.departure_place}\" 검색 결과 터치")

    def touch_arrival_menu(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_airline_arrival_menu)
        cl.allure_logs("도착 장소 선택 드롭다운 메뉴 터치")

    def input_arrival_place(self):
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.naver_airline_arrival_search_field, self.arrival_place)
        cl.allure_logs(f"도착 장소 \"{self.arrival_place}\" 입력")

    def touch_arrival_place(self):
        BasePage.touch_element(self, AppiumBy.XPATH, pe.naver_airline_arrival_place)
        cl.allure_logs(f"\"{self.arrival_place}\" 검색 결과 터치")

    def check_airline_setup(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.naver_airline_setup)
        cl.allure_logs("출발 장소, 도착 장소 선택 확인")
