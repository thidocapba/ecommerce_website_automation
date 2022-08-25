import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#initialize webdriver
driver = webdriver.Chrome('D:/webdrivers/chromedriver.exe')

#Open URl and maximize window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()
time.sleep(2)

#phones button
phones = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
phones.click()
time.sleep(2)

#iphone
iphone = driver.find_element(By.XPATH, '//a[text()="iPhone"]')
iphone.click()
time.sleep(2)

#first picture
first_pic = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[1]/li[1]/a')
first_pic.click()
time.sleep(2)

#next picture
next_click = driver.find_element(By.XPATH, '/html/body/div[2]/div/button[2]')

for i in range(0, 5):
    next_click.click()
    time.sleep(2)

#save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')

#close
x_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/button')
x_button.click()
time.sleep(2)

#quantity
quantity = driver.find_element(By.ID, 'input-quantity')
quantity.click()
time.sleep(2)

quantity.clear()
time.sleep(2)
quantity.send_keys('2')
time.sleep(2)

#add to cart
add_to_button = driver.find_element(By.ID, 'button-cart')
add_to_button.click()
time.sleep(2)

laptops = driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/a')
action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2 = driver.find_element(By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/a')
laptops_2.click()
time.sleep(2)

#Click on HP laptop
HP = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div[1]/div/div[2]/div[1]/h4/a')
HP.click()

#scroll
add_to_button_2 = driver.find_element(By.XPATH, '//*[@id="button-cart"]')
add_to_button_2.location_once_scrolled_into_view
time.sleep(2)

#calendar
calendar = driver.find_element(By.XPATH, '//*[@id="product"]/div[1]/div/span/button/i')
calendar.click()
time.sleep(2)


next_click_calender = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/table/thead/tr[1]/th[3]')
month_year = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/table/thead/tr[1]/th[2]')

#year: 2022 and month: december
while month_year.text != 'December 2022':
    next_click_calender.click()
time.sleep(2)

#day 31
calender_date = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/table/tbody/tr[5]/td[6]')
calender_date.click()
time.sleep(2)

#add_to_button
add_to_button_2.click()
time.sleep(2)

#checkout
go_to_cart = driver.find_element(By.ID, 'cart-total')
go_to_cart.click()
time.sleep(2)

checkout = driver.find_element(By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[2]')
checkout.click()
time.sleep(2)

#click on guest account
guest = driver.find_element(By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
guest.click()
time.sleep(2)

#click continue 1
continue_1 = driver.find_element(By.ID, 'button-account')
continue_1.click()
time.sleep(2)

#scrolling
step_2 = driver.find_element(By.XPATH, '//*[@id="accordion"]/div[2]/div[1]/h4/a')
step_2.location_once_scrolled_into_view
time.sleep(2)

#first name
first_name = driver.find_element(By.ID, 'input-payment-firstname')
first_name.click()
time.sleep(2)
first_name.send_keys('test_first_name')
time.sleep(2)

#last name
last_name = driver.find_element(By.ID, 'input-payment-lastname')
last_name.click()
time.sleep(2)
last_name.send_keys('test_last_name')
time.sleep(2)

#email
email = driver.find_element(By.ID, 'input-payment-email')
email.click()
time.sleep(2)
email.send_keys('test@test.com')
time.sleep(2)

#telephone
telephone = driver.find_element(By.ID, 'input-payment-telephone')
telephone.click()
time.sleep(2)
telephone.send_keys('0123456789')
time.sleep(2)

#address
address = driver.find_element(By.ID, 'input-payment-address-1')
address.click()
time.sleep(2)
address.send_keys('Aeon Mall Ha Dong')
time.sleep(2)

#city
city = driver.find_element(By.ID, 'input-payment-city')
city.click()
time.sleep(2)
city.send_keys('Ha Noi')
time.sleep(2)

#post code
postcode = driver.find_element(By.ID, 'input-payment-postcode')
postcode.click()
time.sleep(2)
postcode.send_keys('112233')
time.sleep(2)

#country
country = driver.find_element(By.ID, 'input-payment-country')
dropdown_1 = Select(country)
time.sleep(2)
dropdown_1.select_by_index(-8)
time.sleep(2)

#region
region = driver.find_element(By.ID, 'input-payment-zone')
dropdown_2 = Select(region)
time.sleep(2)
dropdown_2.select_by_visible_text('Ha Noi')
time.sleep(2)

#click continue 2
continue_2 = driver.find_element(By.XPATH, '//*[@id="button-guest"]')
continue_2.click()
time.sleep(2)

#click continue 3
continue_3 = driver.find_element(By.XPATH, '//*[@id="button-shipping-method"]')
continue_3.click()
time.sleep(2)

#accept terms & conditions
t_e = driver.find_element(By.XPATH, '//*[@id="collapse-payment-method"]/div/div[2]/div/input[1]')
t_e.click()
time.sleep(2)

#click continue 4
continue_4 = driver.find_element(By.XPATH, '//*[@id="button-payment-method"]')
continue_4.click()
time.sleep(3)

#final price
final_price = driver.find_element(By.XPATH, '//*[@id="collapse-checkout-confirm"]/div/div[1]/table/tfoot/tr[3]/td[2]')

print("The final price of both products is " + final_price.text)
time.sleep(2)

#click on the confirmation button
confirmation_button = driver.find_element(By.XPATH, '//*[@id="button-confirm"]')
confirmation_button.click()
time.sleep(2)

#success text
success_text = driver.find_element(By.XPATH, '//*[@id="content"]/h1')
print(success_text.text)
time.sleep(2)

driver.close()