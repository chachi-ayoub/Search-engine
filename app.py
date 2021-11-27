
from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import pymongo
import json
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def search():
    if request.method == 'POST' :

        key = request.form['key']
        source = request.form['source']
        year = request.form['year']

        if (source == 'pubmed'):
            pubmed(key, year)

        if (source == 'scopus' and year == '2020'):
            scopus(key)
        if (source == 'scopus' and year == '2019'):
            scopus(key)
        if (source == 'scopus' and year == '2018'):
            scopus(key)
        if (source == 'scopus' and year == '2017'):
            scopus(key)

        if (source == 'ieee'):
            ieee(key,year)

        if (source == 'springer'):
            springer(key,year)
        
        return render_template("search.html")
        


@app.route('/database')
def database():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.pubmed
    articles = db.articles
    data = []
    for article in articles.find():
        data.append(article)
    
    return render_template("database.html" , data = data)





def scopus(term):
    driver = webdriver.Chrome(
        executable_path="C:/chromedriver.exe")
    driver.maximize_window()
    url = 'https://www.scopus.com'
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="signin_link_move"]/span').click()
    driver.find_element(
        By.XPATH, '//*[@id="bdd-email"]').send_keys("ayoub.chachi@etu.uae.ac.ma")
    driver.find_element(By.XPATH, '//*[@id="bdd-elsPrimaryBtn"]').click()
    driver.find_element(
        By.XPATH, '//*[@id="bdd-password"]').send_keys("0667227916w-W")
    driver.find_element(By.XPATH, '//*[@id="bdd-elsPrimaryBtn"]').click()
    driver.find_element(By.XPATH, '//*[@id="documents-tab-panel"]/div/form/div[1]/div/div[2]/els-input/div/label/input').send_keys(term)
    driver.find_element(
        By.XPATH, '//*[@id="documents-tab-panel"]/div/form/div[2]/div[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="li_2017"]/label').click()
    driver.find_element(
        By.XPATH, '//*[@id="RefineResults"]/div[1]/div[2]/ul/li[1]/input').click()
    driver.find_element(By.XPATH, '//*[@id="showAllPageBubble"]').click()
    driver.find_element(
        By.XPATH, '//*[@id="selectAllMenuItem"]/span[2]/span/ul/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="directExport"]/span').click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[3]/form/div[4]/div[2]/div/div/section[1]/div/div[1]/div[1]/div/div/span/div[6]/div/div/div[2]/div/div/ul/li[1]/label').click()
    driver.find_element(By.XPATH, '//*[@id="chunkExportTrigger"]').click()
    
    file1name = getDownLoadedFileName(10, driver)  # GET FILE NAME  //*[@id="chunkExportTrigger"]/span
    print("file 1 name: " + file1name)
    # driver.switch_to.window(driver.window_handles[0])
    # driver.back()
    # driver.find_element(By.XPATH, '//*[@id="li_2018"]/label').click()
    # driver.find_element(
    #     By.XPATH, '//*[@id="RefineResults"]/div[1]/div[2]/ul/li[1]/input').click()
    # driver.find_element(By.XPATH, '//*[@id="showAllPageBubble"]').click()
    # driver.find_element(
    #     By.XPATH, '//*[@id="selectAllMenuItem"]/span[2]/span/ul/li[1]/label').click()
    # driver.find_element(By.XPATH, '//*[@id="directExport"]/span').click()
    # time.sleep(1)
    # driver.find_element(
    #     By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[3]/form/div[4]/div[2]/div/div/section[1]/div/div[1]/div[1]/div/div/span/div[6]/div/div/div[2]/div/div/ul/li[1]/label').click()
    # driver.find_element(By.XPATH, '//*[@id="chunkExportTrigger"]').click()
    # file2name = getDownLoadedFileName(10, driver)  # GET FILE NAME
    # print("file 2 name: " + file2name)
    # driver.switch_to.window(driver.window_handles[0])
    # driver.back()
    # driver.find_element(
    #     By.XPATH, '//*[@id="seachwithinresults"]').send_keys("Thanks for watching.")

    # WebDriverWait(driver, 5)
    # driver.back()
    # driver.find_element(By.XPATH, '//*[@id="li_2019"]/label').click()
    # driver.find_element(
    #     By.XPATH, '//*[@id="RefineResults"]/div[1]/div[2]/ul/li[1]/input').click()
    # driver.find_element(By.XPATH, '//*[@id="showAllPageBubble"]').click()
    # driver.find_element(
    #     By.XPATH, '//*[@id="selectAllMenuItem"]/span[2]/span/ul/li[1]/label').click()
    # driver.find_element(By.XPATH, '//*[@id="directExport"]/span').click()
    # driver.find_element(By.XPATH, '//*[@id="exportTypeAndFormat"]').click()
    # driver.find_element(By.XPATH, '//*[@id="chunkExportTrigger"]').click()
    # WebDriverWait(driver, 5)
    # driver.back()
    # driver.find_element(By.XPATH, '//*[@id="li_2020"]/label').click()
    # driver.find_element(
    #     By.XPATH, '//*[@id="RefineResults"]/div[1]/div[2]/ul/li[1]/input').click()
    # driver.find_element(By.XPATH, '//*[@id="showAllPageBubble"]').click()
    # driver.find_element(
    #     By.XPATH, '//*[@id="selectAllMenuItem"]/span[2]/span/ul/li[1]/label').click()
    # driver.find_element(By.XPATH, '//*[@id="directExport"]/span').click()
    # driver.find_element(By.XPATH, '//*[@id="exportTypeAndFormat"]').click()
    # driver.find_element(By.XPATH, '//*[@id="chunkExportTrigger"]').click()
    # WebDriverWait(driver, 5)

    # df = pd.read_csv("covid-19.csv")
    # data = df.to_dict(orient = "records")
    # client = pymongo.MongoClient("mongodb://localhost:27017")
    # db = client["PubMedSraping"]
    # db.Articls.insert_many(data)
    driver.quit()
    # while(True):
    #     pass

def pubmed(term, year):
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://pubmed.ncbi.nlm.nih.gov/")
    search = driver.find_element(By.XPATH,"//input[@class='term-input tt-input']")
    search.send_keys(term)
    search.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, '/html/body/main/div[9]/div[1]/form/div/div[1]/div[4]/ul/li[4]/label').click()
    driver.find_element(By.XPATH, '//*[@id="datepicker"]/div[2]/input[1]').send_keys(year)
    driver.find_element(By.XPATH, '//*[@id="datepicker"]/div[4]/input[1]').send_keys(year)
    driver.find_element(By.XPATH, '//*[@id="datepicker"]/div[4]/input[2]').send_keys("12")
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
    df.to_csv('pubmed2018.csv', mode='a', header=True)

    df = pd.read_csv("pubmed2017.csv")
    data = df.to_dict(orient = "records")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["pubmed2017"]
    db.articles.insert_many(data)
    driver.quit()

def ieee (term,year):
    
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://ieeexplore.ieee.org/Xplore/home.jsp")

    driver.find_element_by_css_selector("input[type='text']").send_keys(term)
    driver.find_element_by_class_name("search-icon").click()
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="xplMainContent"]/div[2]/div[1]/xpl-facets/section/ul/li[1]/section/div[1]/xpl-nouislider-facet/span/span[1]/button[1]')))
    driver.find_element_by_class_name('//*[@id="xplMainContent"]/div[2]/div[1]/xpl-facets/section/ul/li[1]/section/div[1]/xpl-nouislider-facet/span/span[1]/button[1]').click()

    driver.find_element_by_class_name('//*[@id="xplMainContent"]/div[2]/div[1]/xpl-facets/section/ul/li[1]/section/div[1]/xpl-nouislider-facet/span/span[3]/span[2]/span/input').sen_keys(year)
    driver.find_element_by_class_name('//*[@id="Year-apply-btn"]').click()
    
    time.sleep(30)
    # # time.sleep(1)

    # driver.find_element_by_class_name("u-font-smaller ng-pristine ng-valid ng-touched").clear()
    # # time.sleep(1)

    # driver.find_element_by_class_name("u-font-smaller ng-pristine ng-valid ng-touched").send.keys(year)
    # # time.sleep(1)

    # driver.find_element_by_css_selector("#Year-apply-btn").click()
    # # time.sleep(1)
    
    # driver.find_element_by_css_selector("#xplMainContent > div.ng-Dashboard > div.col-12.action-bar.hide-mobile > ul > li.Menu-item.inline-flexed.export-filter.myproject-export > xpl-export-search-results > button > a").click
    # # time.sleep(1)

    # driver.find_element_by_css_selector("#ngb-nav-10-panel > div > div > div > button").click
    # time.sleep(20)


    # while True:
    #     pass  

def springer(term,year):
    
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://link.springer.com/")

    driver.find_element_by_css_selector("#query").send_keys(term)
    driver.find_element_by_css_selector("#search").click()
    time.sleep(1)

    driver.find_element_by_css_selector("#date-facet > button > div").click()
    time.sleep(1)

    driver.find_element_by_css_selector("#date-facet-mode").click()
    driver.find_element_by_css_selector("#date-facet-mode").send_keys("i")
    time.sleep(1)

    driver.find_element_by_css_selector("#date-facet-mode").click()
    time.sleep(1)

    driver.find_element_by_css_selector("#start-year").clear()
    time.sleep(1)

    driver.find_element_by_css_selector("#start-year").send_keys(year)
    time.sleep(1)

    driver.find_element_by_css_selector("#date-facet-submit").click()
    time.sleep(1)

    driver.find_element_by_css_selector("#tool-download > img").click()
    
    

    while True:
        pass

def getDownLoadedFileName(waitTime, driver):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[1])
        driver.get('chrome://downloads')

        endTime = time.time()+waitTime
        while True:
            try:
                # get downloaded percentage
                downloadPercentage = driver.execute_script(
                    "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
                time.sleep(3)
                if downloadPercentage == 100:
                    return driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
            except:
                pass
            time.sleep(1)
            if time.time() > endTime:
                break



if __name__ == '__main__':
    app.run(debug = True)