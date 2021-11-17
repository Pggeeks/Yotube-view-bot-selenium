from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Yt:
    EXECUTABLE = 'C:/Users/LENOVO/Downloads/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=EXECUTABLE)

    def __init__(self, link,views=50):
        self.link = link
        self.views = views


    def RunBot(self):
        self.driver.get(self.link)
        handel = self.driver.window_handles
        actions = ActionChains(self.driver)
        self.driver.execute_script(
            f'''window.open("{self.link}","secondtab");''')
        for i, _ in enumerate(range(self.views), start=1):
            try:
                if i % 2:
                    self.driver.switch_to.window("secondtab")
            finally:
                actions.send_keys(Keys.SPACE).perform()
                time.sleep(2)
                self.driver.refresh()
                for w in handel:
                    self.driver.switch_to.window(w)

V_LINK = 'https://youtu.be/AZ0X7hG8aIo'
if __name__ == '__main__':
    abc = Yt(V_LINK)
    abc.RunBot()

