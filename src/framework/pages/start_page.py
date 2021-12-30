'''
Created on Dec 29, 2021
@author: a.volkodatov
'''


class StartPageLocators():  # pylint: disable=too-few-public-methods
    """Class that contains start page locators"""

    MAIN_PAGE_WRAPPER_XPATH = "//div[@class='appWrap']"

    HEADER_WRAPPER_XPATH = "//div[@class='headerWrap']"
    LOGIN_WRAPPER_XPATH = HEADER_WRAPPER_XPATH + "//div[@class='loginWrap']"
    RGSTR_BTN_XPATH = LOGIN_WRAPPER_XPATH + "//button[@class='mainBtn regBtn registrationBtn']"

    RGSTR_FORM_WRAPPER_XPATH = "//div[@class='formWrap authForm']"
    RGSTR_DATE_XPATH = RGSTR_FORM_WRAPPER_XPATH + "//input[@name='date']"
    RGSTR_EMAIL_XPATH = RGSTR_FORM_WRAPPER_XPATH + "//input[@name='email']"
    RGSTR_LOGIN_XPATH = RGSTR_FORM_WRAPPER_XPATH + "//input[@name='username']"
    RGSTR_PASSWORD_XPATH = RGSTR_FORM_WRAPPER_XPATH + \
        "//div[@class='fieldWrap passWrap'][1]/input[@type='password']"
    RGSTR_CONFIRM_PASSWORD_XPATH = RGSTR_FORM_WRAPPER_XPATH + \
        "//div[@class='fieldWrap passWrap'][2]/input[@type='password']"
    RGSTR_LICENSE_CHECKBOX_XPATH = RGSTR_FORM_WRAPPER_XPATH + "//input[@type='checkbox']"
    RGSTR_SUBMIT_XPATH = RGSTR_FORM_WRAPPER_XPATH + "//button[@class='mainBtn']"
    RGSTR_PASSWORD_LENGTH_ERROR_XPATH = RGSTR_FORM_WRAPPER_XPATH + \
        "//div[@class='error danger-color passValidation']"

    TOP_SLIDER_WRAPPER = "//div[@class='sliderWrap pageContainer']"
    LIVE_BTN_XPATH = TOP_SLIDER_WRAPPER + "//a[contains(@href,'/live')]"
    # //div[@class='sliderWrap pageContainer']//a[contains(@href,'/live')]
    USER_WRAP_LOGIN_XPATH = "//div[@class='userWrap curPointer logined']"
    LOGGED_USER_EMAIL_XPATH = USER_WRAP_LOGIN_XPATH + "//span[@class='userName ellipsis']"
    LIVE_SECTION_NAME = "//div[@class='pageWrap livePageWrap']/h1"

    COUNT_OUTER_WRAP_XPATH = "//div[@class='contOuterWrap']"
    SLIDER_WRAP_XPATH = COUNT_OUTER_WRAP_XPATH + "//div[@class='sliderWrap']"
    FURTHER_ARROW_XPATH = SLIDER_WRAP_XPATH + "//div[@class='custom-arrow slick-arrow slick-next']"
    SLIDER_ITEM_LIST_XPATH = SLIDER_WRAP_XPATH + "//div[@class='slick-track']/div"
    SPORT_COUNT_XPATH = ".//div[@class='sportCount']"
    SPORT_NAME_XPATH = ".//div[@class='sportName']"

    TABLE_WRAP_XPATH = "//div[@class='tableWrap']"
    TABLE_ITEM_XPATH = "//div[@class='eventItemWrap']"
    FAV_BLOCK_XPATH = "//div[@class='favBlock topFav']"
