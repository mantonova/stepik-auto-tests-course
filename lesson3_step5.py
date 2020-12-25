from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element_by_xpath("//button[@type = 'submit']")
    option1.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    option2 = browser.find_element_by_xpath("//button[@type = 'submit']")
    option2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
