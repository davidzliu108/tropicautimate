from selenium import webdriver
import time
import datetime

web = webdriver.Chrome()

web.get('https://tsclistens.com/')

time.sleep(0.5)

# insert store number
storeNumber = "NC059"
storeNum = web.find_element_by_xpath('//*[@id="InputStoreNum"]')
storeNum.send_keys(storeNumber)

# insert date
calendar = web.find_element_by_xpath('//*[@id="Index_VisitDatecontainer"]/button/img')
calendar.click()
days = web.find_elements_by_xpath('//table[@class="ui-datepicker-calendar"]//a')
for day in days:
    datea=day.text
    today = str(datetime.datetime.now().day)
    if datea==today:
        day.click()
        break

# insert hour
hour = datetime.datetime.now().hour
if hour > 12: 
    standardHour = hour - 12
hourBox = web.find_element_by_xpath('//*[@id="InputHour"]')
if standardHour < 10:
    strStandard = "0" + str(standardHour)
    hourBox.send_keys(strStandard)
else:
    hourBox.send_keys(standardHour)
print(standardHour)

# insert minute
minute = datetime.datetime.now().minute
minuteBox = web.find_element_by_xpath('//*[@id="InputMinute"]')
if minute < 10:
    strMinute = "0" + str(minute)
    minuteBox.send_keys(strMinute)
else:
    minuteBox.send_keys(str(minute))
print(minute)

# insert AM/PM, AM=true, PM=false
ampm = web.find_element_by_xpath('//*[@id="InputMeridian"]')
if hour > 12:
    ampm.send_keys("PM")
else:
    ampm.send_keys("AM")
    
# insert transaction number
transBox = web.find_element_by_xpath('//*[@id="InputTransactionNum"]')
transBox.send_keys(6629)

# start
start = web.find_element_by_xpath('//*[@id="NextButton"]')
start.click()


# form
onep = web.find_element_by_xpath('//*[@id="FNSR000003"]/td[3]/span')
onep.click()
web.find_element_by_xpath('//*[@id="NextButton"]').click()

web.find_element_by_xpath('//*[@id="FNSR000006"]/div/div/div[1]/span/span').click()
web.find_element_by_xpath('//*[@id="NextButton"]').click()

web.find_element_by_xpath('//*[@id="FNSR000007"]/div/div/div[3]/span/span').click()
web.find_element_by_xpath('//*[@id="NextButton"]').click()

# dine type
types = web.find_elements_by_xpath('//div[@class="rbList"]//span')
for type in types:
    bruv = type.text
    if bruv=="Dine In":
        type.click()
        break



web.find_element_by_xpath('//*[@id="FNSR000009"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000028"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000010"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000016"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000018"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="NextButton"]').click()

web.find_element_by_xpath('//*[@id="FNSR000010"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000013"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000015"]/td[6]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000018"]/td[4]/span').click()
web.find_element_by_xpath('//*[@id="FNSR000011"]/td[2]/span').click()
web.find_element_by_xpath('//*[@id="NextButton"]').click()





