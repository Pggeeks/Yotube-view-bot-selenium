# code by pggeeks aka parth gujral
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Yt:
    #EXECUTABLE = 'C:/Users/LENOVO/Downloads/chromedriver_win32/chromedriver.exe' add executable path of your own
    driver = webdriver.Chrome(executable_path=EXECUTABLE)

    def __init__(self, link,views=50):
        self.link = link
        self.views = views


    def RunBot(self):
        self.driver.get(self.link)
        handel = self.driver.window_handles
        actions = ActionChains(self.driver)
        self.driver.execute_script(
            f'''window.open("{self.link}","secondtab");''') # Creates a new tab
        for i, _ in enumerate(range(self.views), start=1):
            try:
                if i % 2:
                    self.driver.switch_to.window("secondtab") # switch between the 2 tabs
            finally:
                actions.send_keys(Keys.SPACE).perform() # press space to play the video
                time.sleep(2)
                self.driver.refresh()
                for w in handel:
                    self.driver.switch_to.window(w) # switch back to the tab

V_LINK = # add the link here
if __name__ == '__main__':
    abc = Yt(V_LINK)
    abc.RunBot()

