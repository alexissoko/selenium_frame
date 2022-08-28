from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta

# from unittest import TestCase

import conf

#class Test_Contract_creation():
class Contract_creation():
    def __init__(self):
        self.driver =  webdriver.Chrome("./chromedriver")
        self.driver.get(conf.url)
        # self.actions = ActionChains(self.driver)
    
    def explicit_waiting(self, type_tag, label):
        if type_tag == "XPATH":
            try:
                WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.XPATH, label)))
            except NoSuchElementException as nse:
                    print(nse)
                    print("-----")
                    print(str(nse))
                    print("-----")
                    print(nse.args)
                    print("=====")


    def login_deel(self):
        username = self.driver.find_element(By.XPATH, "//input[contains(@name, 'email')]")
        username.send_keys(conf.user)
        password = self.driver.find_element(By.XPATH, "//input[contains(@name, 'password')]")
        password.send_keys(conf.password)
            
        login = self.driver.find_element(By.XPATH, "//button[contains(@class, 'button w-100')]")
        login.click()
        input("Solve Captcha manually")


    def happy_deel_contract(self):
        """
        Method to test contract creation
        """
        self.login_deel()
        self.explicit_waiting("XPATH", '//*[@id="root"]/div[2]/div[4]/div/div[1]/div/div/div/div[1]/h1')
        
        # click contract button        
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div/a[2]/div').click()
        self.explicit_waiting("XPATH", '//*[@id="root"]/div[2]/div[2]/div/div[2]/h1')
        # click fixed rate type
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[3]/div[1]/a/div/div').click()
        self.explicit_waiting("XPATH", '//*[@id="root"]/div[2]/div[2]/div/form/div/div[1]/div/div/div[1]/div/div/div/input')
        # contract name fill in
        self.driver.find_element(By.CLASS_NAME, "deel-ui__input-component__input").send_keys(conf.contract_name)
        # country
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/form/div/div[1]/div/div/div[2]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-select-2-option-1-2"]').click()
        # State
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/form/div/div[1]/div/div/div[2]/div[2]/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-select-4-option-5"]').click()
        # dd = Select(country)# .send_keys("USA - COLORADO")
        # dd.select_by_value("Colorado")
        self.driver.find_element(By.XPATH, "//input[contains(@name, 'jobTitle')]").send_keys(conf.job_title)
        
        #Seniority
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/form/div/div[1]/div/div/div[4]/div/div/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-select-3-option-3"]').click()
        
        # Scope of work
        driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/form/div/div[1]/div/div/div[5]/div[1]/textarea').send_keys(conf.scope_of_work)
        
        # Date pick
        target_date = (datetime.today() - timedelta(days=1)).strftime('%m-%d-%Y')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/form/div/div[1]/div/div/div[7]').click()
        self.driver.find_element(By.XPATH,  "/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[4]/span[3]/button").click()

        self.driver.find_element(By.XPATH,  '//*[@id="root"]/div[2]/div[4]/div/form/div/div[2]/button').click()
        # Before ast form explicit waiting
        self.explicit_waiting("XPATH", '//*[@id="root"]/div[2]/div[4]/div/h2')
        # Currency
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[2]/form/div[1]/div[2]/div[1]/div/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-select-5-option-37"]').click()
        # Payment
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[2]/form/div[1]/div[2]/div[1]/span/div/div/input').send_keys(conf.payment)
        # Payment frequency
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-select-6-option-0"]').click()
        # Next
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[2]/form/div[2]/button[2]').click()
        # Last form screen wait
        self.explicit_waiting("XPATH", '//*[@id="root"]/div[2]/div[4]/div/div[2]/div/div[1]/h4')
        # Next's
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[2]/div/div[2]/form/div/div[4]/button[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[2]/div[5]/div/button[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[2]/div[2]/div/button[2]').click()

        self.explicit_waiting("XPATH", '//*[@id="root"]/div[2]/div[4]/div/div[1]/div[1]/div/h1')
        target =  driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[3]/div/div[1]/div[1]/div/div/button[1]')
        return target
    
    def simple_deel_test():
        driver =  webdriver.Chrome("./chromedriver")
        driver.get("https://dev.deel.wtf/")
        out = None
        WebDriverWait(driver, 75).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[1]/div/div/div/div[1]/h1')))
        try:
            # WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="www-wikipedia-org"]/div[1]/h1/span')))
            WebDriverWait(driver, 75).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[4]/div/div[1]/div/div/div/div[1]/h1')))
            out = True
        except NoSuchElementException as nse:
            print(nse)
            print("-----")
            print(str(nse))
            print("-----")
            print(nse.args)
            print("=====")
            out = False
        driver.quit()
        return out
    
def test_contract_auto():
    new_contract = Contract_creation()
    result =  new_contract.happy_deel()
    assert conf.contract_name == result.text


def test_happy_path_amazon():
    driver = webdriver.Chrome("./chromedriver")

    driver.get("https://www.amazon.com")

    driver.get(conf.user)

    time.sleep(2)

    search = driver.find_element_by_id("twotabsearchtextbox")
    search.sendkeys("laptop")
    driver.find_element_by_id("nav-search-submit-button").clieck()

    time.sleep(2)

    driver.find_element_by_id("results_array")[-1].click()
    driver.find_element_by_id("add_to_cart_link").click()
    driver.find_element_by_id("cart_icon").click()

    assert driver.find_element("")

def custom_xpath(url="https://www.google.com"):
    driver = webdriver.Chrome("./chromedriver")
    driver.get(url)
    test = driver.find_element(By.XPATH, "//a[contains(@class, 'gb_1 gb_2 gb_8d gb_8c')]")
    test.click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    except NoSuchElementException as nse:
            print(nse)
            print("-----")
            print(str(nse))
            print("-----")
            print(nse.args)
            print("=====")
    finally:
        driver.quit()
    
custom_xpath()


    
