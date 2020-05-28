import time

from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver')
    driver.get('https://github.com/login')
    time.sleep(2)
    username = driver.find_element_by_name('login')
    username.send_keys("kdeepak2912@gmail.com")
    password = driver.find_element_by_name('password')
    password.send_keys('dpkmr2912')
    submit = driver.find_element_by_name('commit')
    submit.click()
    time.sleep(15)



if __name__ == '__main__':
    main()