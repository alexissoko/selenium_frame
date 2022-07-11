from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# import conf

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


    