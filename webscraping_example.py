from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)

browser.get("ttps://stockx.com/adidas-yeezy-500-blush")

# Wait 20 seconds for page to load
timeout = 20

# try:
#     WebDriverWait(browser, timeout).until(
#         EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
# except TimeoutException:
#     print("Timed out waiting for page to load")
#     browser.quit()

# find_elements_by_class_name to get the historical sales.
class_element = browser.find_element_by_class_name("market-history-sales")

# get the a-ref to show 'all sales'
all_sales_link = class_elements.find_element_by_tag_name('a')
# click to get the table
all_sales_link.click()
# get the table
table_id = browser.find_element(By.ID, '480')
# get information inside tbody tag
t_body = table_id.find_elements(By.TAG_NAME, "tbody")

# get the date
data = t_body[0].text.split('\n')

for datum in data:
    sale = datum[0].split(' ')
    price = sale.pop()
    size = sale.pop()
    date = " ".join(sale)