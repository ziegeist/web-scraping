elements = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[13]/div/div/div/div[2]/div[2]/a')
elements.click()
table_id = browser.driver.find_element(By.ID, '480')
t_body = table_id.find_elements(By.TAG_NAME, "tbody")
t_body[0]
data = t_body[0].text.split('\n')
data[0].split(' ')
print(sale)
price = sale.pop()
size = sale.pop()
date = " ".join(sale)

class_elements = browser.find_element_by_class_name("market-history-sales")

all_sales_link = class_elements.find_element_by_tag_name('a')

all_sales_link.click()