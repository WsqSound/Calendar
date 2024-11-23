from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from datetime import datetime
import time
# Ввожу данные через инпут и разбиваю их на отдельные значения для последующей проверки допустимости значений
a,b,c=input("Введите дату в формате число.месяц.год (например, 01.01.2025): ").split(".")
# Формирую допустимые значения
days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31",]
month = ''
if b == '01':
    month = "Январь"
elif b == '02':
    month = "Февраль"
elif b == '03':
    month = "Март"
elif b == '04':
    month = "Апрель"
elif b == '05':
    month = "Май"
elif b == '06':
    month = "Июнь"
elif b == '07':
    month = "Июль"
elif b == '08':
    month = "Август"
elif b == '09':
    month = "Сентябрь"
elif b == '10':
    month = "Октябрь"
elif b == '11':
    month = "Ноябрь"
elif b == '12':
    month = "Декабрь"
else:
    print("You can input month value in 01 to 12")
    sys.exit() # Прекращаю программу при недопустимых значениях
if int(c) > 2025:
    print('Incorrect year')
    sys.exit()  # Прекращаю программу при недопустимых значениях
if a not in days:
    print("You can input day value in 01 to 31")
    sys.exit()  # Прекращаю программу при недопустимых значениях

date= [a,b,c]
date_input = '.'.join(date) # Джоиню список, чтобы потом передать в функцию в формате библиотеки datetime



url = f"https://www.consultant.ru/law/ref/calendar/proizvodstvennye/2025/"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)
weekend_dates ={}
# Получаем текст всех ячеек с выходными днями
weekend_days_jan = driver.find_elements(By.CSS_SELECTOR, "[value = 'Январь'] [class='weekend']")
weekend_days_jan.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Январь'] [class='holiday weekend']"))
weekend_days_feb = driver.find_elements(By.CSS_SELECTOR, "[value = 'Февраль'] [class='weekend']")
weekend_days_feb.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Февраль'] [class='holiday weekend']"))
weekend_days_mar = driver.find_elements(By.CSS_SELECTOR, "[value = 'Март'] [class='weekend']")
weekend_days_mar.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Март'] [class='holiday weekend']"))
weekend_days_apr = driver.find_elements(By.CSS_SELECTOR, "[value = 'Апрель'] [class='weekend']")
weekend_days_apr.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Апрель'] [class='holiday weekend']"))
weekend_days_may = driver.find_elements(By.CSS_SELECTOR, "[value = 'Ноябрь'] [class='weekend']")
weekend_days_may.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Ноябрь'] [class='holiday weekend']"))
weekend_days_jun = driver.find_elements(By.CSS_SELECTOR, "[value = 'Май'] [class='weekend']")
weekend_days_jun.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Май'] [class='holiday weekend']"))
weekend_days_jul = driver.find_elements(By.CSS_SELECTOR, "[value = 'Июнь'] [class='weekend']")
weekend_days_jul.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Июнь'] [class='holiday weekend']"))
weekend_days_aug = driver.find_elements(By.CSS_SELECTOR, "[value = 'Июль'] [class='weekend']")
weekend_days_aug.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Июль'] [class='holiday weekend']"))
weekend_days_sep = driver.find_elements(By.CSS_SELECTOR, "[value = 'Август'] [class='weekend']")
weekend_days_sep.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Август'] [class='holiday weekend']"))
weekend_days_oct = driver.find_elements(By.CSS_SELECTOR, "[value = 'Сентябрь'] [class='weekend']")
weekend_days_oct.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Сентябрь'] [class='holiday weekend']"))
weekend_days_nov = driver.find_elements(By.CSS_SELECTOR, "[value = 'Октябрь'] [class='weekend']")
weekend_days_nov.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Октябрь'] [class='holiday weekend']"))
weekend_days_dec = driver.find_elements(By.CSS_SELECTOR, "[value = 'Декабрь'] [class='weekend']")
weekend_days_dec.extend(driver.find_elements(By.CSS_SELECTOR, "[value = 'Декабрь'] [class='holiday weekend']"))
# Получаем даты выходных
for day in weekend_days_jan:
    weekend_dates[1] = {day}
for day in weekend_days_jan:
    weekend_dates[1] = {day}
for day in weekend_days_feb:
    weekend_dates[2] = {day}
for day in weekend_days_feb:
    weekend_dates[2] = {day}
for day in weekend_days_mar:
    weekend_dates[3] = {day}
for day in weekend_days_mar:
    weekend_dates[3] = {day}
for day in weekend_days_apr:
    weekend_dates[4] = {day}
for day in weekend_days_apr:
    weekend_dates[4] = {day}
for day in weekend_days_may:
    weekend_dates[5] = {day}
for day in weekend_days_may:
    weekend_dates[5] = {day}
for day in weekend_days_jun:
    weekend_dates[6] = {day}
for day in weekend_days_jun:
    weekend_dates[6] = {day}
for day in weekend_days_jul:
    weekend_dates[7] = {day}
for day in weekend_days_jul:
    weekend_dates[7] = {day}
for day in weekend_days_aug:
    weekend_dates[8] = {day}
for day in weekend_days_aug:
    weekend_dates[8] = {day}
for day in weekend_days_sep:
    weekend_dates[9] = {day}
for day in weekend_days_sep:
    weekend_dates[9] = {day}
for day in weekend_days_oct:
    weekend_dates[10] = {day}
for day in weekend_days_oct:
    weekend_dates[10] = {day}
for day in weekend_days_nov:
     weekend_dates[11] = {day}
for day in weekend_days_nov:
    weekend_dates[11] = {day}
for day in weekend_days_dec:
    weekend_dates[12] = {day}
for day in weekend_days_dec:
    weekend_dates[12] = {day}
# Закрываем браузер
driver.quit()
print(weekend_dates)
    # Проверяем, есть ли предоставленная дата в списке выходных

