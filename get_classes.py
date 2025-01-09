from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from bs4 import BeautifulSoup

def get_timetable_html(url, username, password):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    # Find the username and password input fields
    username_input = driver.find_element(By.CSS_SELECTOR, '.username')
    password_input = driver.find_element(By.CSS_SELECTOR, '.password')
    # Enter your username and password
    username_input.send_keys(username)
    password_input.send_keys(password)
    # Find and click the login button
    login_button = driver.find_element(By.CLASS_NAME, 'uiButton')
    login_button.click()
    # Wait for the page to load after login
    time.sleep(5)  # You may need to adjust the sleep time depending on the page load speed
    # Now you are logged in and can proceed with scraping or other actions
    html = driver.page_source
    # Close the browser window when done
    driver.delete_all_cookies()
    driver.quit()
    return html 


def getClasses(url, username, password):
    html = get_timetable_html(url, username, password)
    soup = BeautifulSoup(html, 'html.parser')
    days = soup.find_all(class_='entriesWrapper')
    #daysclasses = {}
    weekclasses = []
    for day in days:
        classes = day.find_all(class_='entry class')
        date = day['data-date']
        #classesSummaries = []
        for class_ in classes:
            classSummary = {}
            name_tag = class_.find(class_='title')
            name = name_tag.text if name_tag else None
            times_tag = class_.find(class_='times')
            times = times_tag.text if times_tag else None
            teacher_tag = class_.find(class_='teacher')
            teacher = teacher_tag.text if teacher_tag else None
            roomtag = class_.find(class_='room')
            room = roomtag.text if roomtag else None
            classSummary['name'] = name
            classSummary['times'] = times
            classSummary['teacher'] = teacher
            classSummary['room'] = room
            classSummary['date'] = date
            #classesSummaries.append(classSummary)
            weekclasses.append(classSummary)
        #daysclasses[date] = classesSummaries
    return weekclasses


        
    