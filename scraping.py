from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import pymongo
import json
import time


def pubmed(term):
    
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.get("https://pubmed.ncbi.nlm.nih.gov/")
    search = driver.find_element(By.XPATH,"//input[@class='term-input tt-input']")
    search.send_keys(term)
    search.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, '/html/body/main/div[9]/div[1]/form/div/div[1]/div[4]/ul/li[4]/label').click()
    driver.find_element(By.XPATH, '//*[@id="datepicker"]/div[2]/input[1]').send_keys("2017")
    driver.find_element(By.XPATH, '//*[@id="datepicker"]/div[4]/input[1]').send_keys("2018")
    driver.find_element(By.XPATH, '//*[@id="datepicker"]/div[5]/button[2]').click()
    driver.find_element(By.XPATH, "//*[@id='search-results']/section[1]/div[2]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='search-results']/section[1]/div[2]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='search-results']/section[1]/div[2]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='search-results']/section[1]/div[2]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='search-results']/section[1]/div[2]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='search-results']/section[1]/div[2]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='search-results']/section[1]/div[2]/button/span").click()
    pmid = driver.find_elements(By.XPATH,"//span[@class='docsum-pmid']")
    title = driver.find_elements(By.XPATH,"//a[@class='docsum-title']")
    author = driver.find_elements(By.XPATH,"//span[@class='docsum-authors full-authors']")
    jornal = driver.find_elements(By.XPATH,"//span[@class='docsum-journal-citation full-journal-citation']")
    snippet = driver.find_elements(By.XPATH,"//div[@class='full-view-snippet']")

    pmids = []
    titles = []
    authors = []
    jornals = []
    snippets = []

    for i in range(len(pmid)):
        pmids.append(pmid[i].text)
        titles.append(title[i].text)
        authors.append(author[i].text)
        jornals.append(jornal[i].text)
        snippets.append(snippet[i].text)
    df = pd.DataFrame({'PMIDS':pmids, 'Title':titles, 'Authors':authors, 'Jornals':jornals, 'Snippets':snippets})
    df.to_csv('pubmed2017.csv', mode='a', header=True)

    df = pd.read_csv("pubmed2017.csv")
    data = df.to_dict(orient = "records")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["pubmed2017"]
    db.articles.insert_many(data)


pubmed("business")

