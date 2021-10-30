from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import os
import io
import time
from PIL import Image

import requests
driver = webdriver.Chrome('chromedriver.exe')  
driver.maximize_window()
driver.get('https://www.google.com/')
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")  
driver.find_element_by_xpath('//input[@id="identifierId"]').send_keys(Email)# your email to login
driver.find_element_by_xpath(' //span[contains(text(),"التالي")]').click()
time.sleep(3)
driver.find_element_by_name('password').send_keys(password)# your password to login
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(),'التالي')]").click()
time.sleep(5)
driver.get('https://www.google.com/')
driver.find_element_by_name('q').send_keys(Any search) # your search
driver.find_element_by_xpath('//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[3]/center[1]/input[1]').click()
time.sleep(3)
driver.find_element_by_xpath("//body/div[@id='main']/div[@id='cnt']/div[@id='top_nav']/div[@id='hdtb']/div[@id='pTwnEc']/div[@id='hdtb-msb']/div[1]/div[1]/div[2]/a[1]").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
imgResults = driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")
totalResults=len(imgResults)
print(totalResults)
img_urls = set()
for i in range(0,imgResults):
    img = imgResults[i]
    try:
        img.click()
        time.sleep(2)
        actual_images = driver.find_elements_by_css_selector('img.n3VNCb')
        for actual_image in actual_images:
            if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
                img_urls.add(actual_image.get_attribute('src'))
    except:
        print("Error")           
os.chdir(Path)#Your Path to download images
baseDir=os.getcwd()
for i, url in enumerate(img_urls):
    file_name = f"{i:150}.jpg"    
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - COULD NOT DOWNLOAD {url} - {e}")
    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
            
        file_path = os.path.join(baseDir, file_name)
            
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
            print(f"SAVED - {url} - AT: {file_path}")
    except Exception as e:
            print(f"ERROR - COULD NOT SAVE {url} - {e}")
driver.close()

  
