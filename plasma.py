#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################################################
# Program Title: 
# Creation Date: 
# Description: 
#
##### Notes:

##### Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


import time
import pandas as pd
import matplotlib.pyplot as plt 
##### Functions
def openPlasma(driver):
    driver.get("https://rewards.cslplasma.com/login")

    return driver

def editOptions(driver):
    driver.maximize_window()
    time.sleep(0.3)

    size = driver.get_window_size()
    width, height = size.get('width'), size.get('height')

    driver.set_window_size(int(width/2), height)
    driver.set_window_position(0, 0)

    global wait 
    wait = WebDriverWait(driver, 10)
    return driver

def login(driver, info):
    time.sleep(2)
    email = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/form/div[2]/div[1]/input')
    password = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/form/div[2]/div[3]/div/input')

    email.send_keys(info[0])
    password.send_keys(info[1])
    time.sleep(2)
    button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/form/button')
    #ActionChains(driver).scroll_to_element(button).perform()

    # Get the total scrollable height of the page
    total_height = driver.execute_script("return document.body.scrollHeight")

    # Calculate the middle position
    middle_position = total_height / 4
    driver.execute_script(f"window.scrollTo(0, {middle_position});")

    button.click()
    print("Login successful")
    return driver

def accessHistory(driver):
    a = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[1]/div[1]/div/div[2]/div[4]/a')))
    #a = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[1]/div[1]/div/div[2]/div[4]/a')
    a.click()
    
    driver.execute_script("window.scrollTo(0, 0)")
    print("Donation history accessed")
    weight = []
    BP = []
    HR = []
    temp = []
    dates = []

    tiles = driver.find_elements(By.CLASS_NAME, 'mt-4')
    for t in tiles:
        t.find_element(By.TAG_NAME, 'svg').click()
        dates.append(t.find_elements(By.CLASS_NAME, 'ml-2')[1].text.split(',')[1::])

        health = t.find_elements(By.CLASS_NAME, 'healthSntitle')
        weight.append(health[0].text.split()[0])
        BP.append(health[1].text.split()[0])
        HR.append(health[2].text.split()[0])
        temp.append(health[3].text.split()[0])
    HISTORY = [dates, weight, BP, HR, temp]
    print("Vitals data acquired")
    return driver, HISTORY

def cleanData(history):
    dates = history[0]
    cleanDates = []
    monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i in dates:
        month = i[0].split()[0]
        day = i[0].split()[1]
        year = i[1][1:]
        month = monthNames.index(month) + 1
        cleanDates.append(f"{month}/{day}/{year}")
    sys = []
    dia = []
    for i in history[2]:
        sys.append(i.split('/')[0])
        dia.append(i.split('/')[1])
    
    cleanHistory = [list(map(float, history[1]))[::-1], list(map(float, sys))[::-1], list(map(float, dia))[::-1], list(map(float, history[3]))[::-1], list(map(float, history[4]))[::-1]]
      
    return cleanDates[::-1], cleanHistory

def saveData(date, vitals):
    data = {"Date": date, 
            "Weight": vitals[0],
            "Systolic": vitals[1],
            "Diastolic": vitals[2], 
            "Heart Rate": vitals[3], 
            "Temperature": vitals[4]}
    
    dfNew = pd.DataFrame(data)

    try:
        dfOld = pd.read_csv("plasmaVitals.csv")
        df = pd.concat([dfOld, dfNew])
    except:
        print("No old data to update")
        df = dfNew
    df.drop_duplicates(inplace=True)
    df.to_csv("plasmaVitals.csv", index=False)
    print("Data saved successfully")
    return

def update(email, password):
    loginInfo = [email, password]
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver = openPlasma(driver)
    driver = editOptions(driver)
    driver = login(driver, loginInfo)
    driver, history = accessHistory(driver)
    cleanDates, cleanHistory = cleanData(history)
    saveData(cleanDates, cleanHistory)
    return 

def analyze(file):

    df = pd.read_csv("plasmaVitals.csv")

    HR_average = df["Heart Rate"].mean()
    HR_min = df["Heart Rate"].min()
    weight_average = df["Weight"].mean()
    weight_min = df["Weight"].min()
    weight_max = df["Weight"].max()

    sys_average = int(df["Systolic"].mean())
    dia_average = int(df["Diastolic"].mean())

    temp_average = df["Temperature"].mean()

    fig, ax = plt.subplots(2, 3, figsize=(16, 14))

    fig.suptitle("Plasma Vitals", fontsize=30)
    ax[0, 0].plot(df['Date'], df['Weight'], marker='o', mfc='r')
    ax[0, 0].axhline(y=weight_average, color='r', linestyle='--')
    ax[0, 0].tick_params(axis='x', labelrotation=30, labelsize=6)
    ax[0, 0].set_ylabel("Weight (lbs)")
    ax[0, 1].plot(df['Date'], df['Temperature'], marker='o', mfc='r')
    ax[0, 1].axhline(y=temp_average, color='r', linestyle='--')
    ax[0, 1].tick_params(axis='x', labelrotation=30, labelsize=6)
    ax[0, 1].set_ylabel(f"Temperature ({'\u00b0'}F)")
    ax[0, 2].plot(df['Date'], df['Heart Rate'], marker='o', mfc='r')
    ax[0, 2].axhline(y=HR_average, color='r', linestyle='--')
    ax[0, 2].tick_params(axis='x', labelrotation=30, labelsize=6)
    ax[0, 2].set_ylabel("Heart Rate (bpm)")
    ax[1, 0].plot(df['Date'], df['Systolic'], marker='o', mfc='r')
    ax[1, 0].axhline(y=sys_average, color='r', linestyle='--')
    ax[1, 0].tick_params(axis='x', labelrotation=30, labelsize=6)
    ax[1, 0].set_ylabel("Systolic Pressure (mm Hg)")
    ax[1, 1].plot(df['Date'], df['Diastolic'], marker='o', mfc='r')
    ax[1, 1].axhline(y=dia_average, color='r', linestyle='--')
    ax[1, 1].tick_params(axis='x', labelrotation=30, labelsize=6)
    ax[1, 1].set_ylabel("Diastolic Pressure (mm Hg)")

    ax[1, 2].xaxis.set_visible(False)
    ax[1, 2].yaxis.set_visible(False)

    ax[1, 2].text(0.05, 0.95, "Averages:", fontsize=16, verticalalignment='top')
    ax[1, 2].text(0.05, 0.88, f"Heart Rate: {HR_average} bpm", fontsize=12, verticalalignment='top')
    ax[1, 2].text(0.05, 0.82, f"Blood Pressure: {sys_average}/{dia_average} mm Hg", fontsize=12, verticalalignment='top')
    ax[1, 2].text(0.05, 0.76, f"Weight: {weight_average} lbs", fontsize=12, verticalalignment='top')
    ax[1, 2].text(0.05, 0.70, f"Temperature: {temp_average:.1f} {'\u00b0'}F", fontsize=12, verticalalignment='top')

    ax[1, 2].text(0.05, 0.50, f"Records:", fontsize=16, verticalalignment='top')
    ax[1, 2].text(0.05, 0.43, f"Lowest Heart Rate: {HR_min} bpm", fontsize=12, verticalalignment='top')
    ax[1, 2].text(0.05, 0.37, f"Highest Weight: {weight_max} lbs", fontsize=12, verticalalignment='top')
    ax[1, 2].text(0.05, 0.31, f"Lowest Weight: {weight_min} min", fontsize=12, verticalalignment='top')

    plt.savefig("vitalsDashboard.png", format='png')
    plt.show()
    return
##### Parameters

#####
loginInfo = ["User_email_or_phone", "User_password"]
update(loginInfo[0], loginInfo[1])
analyze("plasmaVitals.csv")

#Last Updated: 