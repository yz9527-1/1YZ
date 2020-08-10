#coding=utf-8
from selenium import webdriver
import time,string,random

driver=webdriver.Chrome()
driver.get('http://192.168.0.223:8032/#')

driver.implicitly_wait(10)

driver.maximize_window()
#登录
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/div[1]/input").send_keys('zshjadmin01')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/input').send_keys('123456')
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/button').click()

driver.implicitly_wait(10)
time.sleep(2)

#点击用户管理
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div/ul/li[5]/a/span[2]').click()
time.sleep(2)
#点击ic卡管理
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div/ul/li[5]/div/div[3]/a/span').click()
for i in range(2600):
    print(i)
    user = ''.join(random.sample(string.digits, 8))
    print(user)

    a="测试%d"%(i)
    print(a)
    #time.sleep(1)
    #点击用户名输入框
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[1]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[1]').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[1]').send_keys(a)
    time.sleep(1)
    #点击姓名输入框
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[2]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[2]').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[2]').send_keys(a)
    #time.sleep(1)
    #点击卡号输入框
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[3]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[3]').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[1]/input[3]').send_keys(user)
    #time.sleep(1)
    #选择卡类型
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/select').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/select/option[2]').click()
    #time.sleep(1)
    #输入工号
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input[1]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input[1]').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input[1]').send_keys(user)
    #time.sleep(1)
    #输入标签
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input[2]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input[2]').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/input[2]').send_keys('测试添加')

    #time.sleep(1)

    #点击添加
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[1]').click()
    #time.sleep(1)
    continue
print("测试完成")
#driver.quit()