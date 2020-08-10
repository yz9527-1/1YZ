#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('http://192.168.0.30:18069')

#print("nihao")
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/input').send_keys('admin@tynam.com')
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/input').send_keys('tynam123')
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/input').click()

time.sleep(2)
#driver.quit()