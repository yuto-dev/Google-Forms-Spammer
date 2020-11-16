from selenium import webdriver
import time

count = 0
message = "spam"

# Replace the variable value with google forms link.
link = 'https://docs.google.com/forms/d/e/1FAIpQLSf0D9PHZAw-MZn0H-Tf5vDrg6qWIpffpjZY43tHHCRFTuk41Q/viewform'

web = webdriver.Chrome()
web.get(link)

time.sleep(2)

while(count < 3):
    
    # Replace the variable value with the text field's xpath.
    textXpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input'
    spam = web.find_element_by_xpath(textXpath)
    spam.send_keys(message)

    # Replace the variable value with the submit button's xpath.
    buttonXpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
    submit = web.find_element_by_xpath(buttonXpath)
    submit.click()
    count = count + 1
    web.get(link)

# crispy