from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import json

browser = webdriver.Chrome("./chromedriver")
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')


username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")


passw = sys.argv[1]
username_input.send_keys("vi.va.an")
password_input.send_keys('vivaan098')

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(3)
getsearch = sys.argv[1]

browser.get("https://instagram.com/"+getsearch+"?__a=1")


x = browser.execute_script("return document.body.innerText;")
y = json.loads(x)

for i in y["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
    print(i["node"]["shortcode"])
    if i["node"]["shortcode"]==sys.argv[2]:
        browser.get(i["node"]["display_url"])


        

    



sleep(6)
#browser.close()


