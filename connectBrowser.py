from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import pyautogui as pya

def hangoutsMeet(url):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 2
        })

    chromedriver = '<path/of/file.extension>'   #location of your chromedriver.exe
    # for windows 2 backlash(\) e.g. C:\\Users\\ABC\\Python\\autoclass\\JoinNow.png

    browser = webdriver.Chrome(options=opt,executable_path=chromedriver)
    browser.maximize_window()

    browser.get("http:\\google.com")

    time.sleep(3)


    browser.find_element_by_css_selector('#gb_70').click()
    time.sleep(5)

    browser.find_element_by_css_selector('#identifierId').send_keys('<your email id>')  # insert your mail id

    browser.find_element_by_css_selector('#identifierNext > div > button > div.VfPpkd-RLmnJb').click()
    time.sleep(10)

    browser.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys('<password>')     # insert password

    browser.find_element_by_css_selector('#passwordNext > div > button > div.VfPpkd-RLmnJb').click()
    time.sleep(5)


    action = ActionChains(browser)
    find = browser.find_element_by_link_text('About')
    action.key_down(Keys.CONTROL).click(find).key_up(Keys.CONTROL).perform()
    browser.switch_to.window(browser.window_handles[-1])

    browser.get(url=url)


    time.sleep(7)

    #Block Video
    
    browser.find_element_by_css_selector('#yDmH0d > c-wiz > div > div > div:nth-child(4) > div.crqnQb > div > div.vgJExf > div > div > div.oORaUb.NONs6c > div.mFzCLe > div.EhAUAc > div.GOH7Zb > div > div > span > span > div > div > svg').click()
    time.sleep(1)

    #Block Audio
    
    browser.find_element_by_css_selector('#yDmH0d > c-wiz > div > div > div:nth-child(4) > div.crqnQb > div > div.vgJExf > div > div > div.oORaUb.NONs6c > div.mFzCLe > div.EhAUAc > div.ZB88ed > div > div > div > span > span').click()
    time.sleep(3)

    #Join class

    x,y=pya.locateCenterOnScreen("path/of/file.extension")  #enter location of JoinNow.png file
    pya.moveTo(x,y,1)
    pya.click()


    time.sleep(30)  # change this 30 to the running time of class
    #to end the class
    pya.moveRel(200,0,1)
    browser.find_element_by_css_selector('#ow3 > div.T4LgNb > div > div:nth-child(4) > div.crqnQb > div.rG0ybd.LCXT6 > div.q2u11 > div.s1GInc.zCbbgf > div').click()