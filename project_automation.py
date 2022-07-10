from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
maps=["gas station","groceries","restaurant","hotel"]
page=input("enter the page name: ").lower()
if(page!="maps"):
    if(page=="google"):
        google_search=input("enter the the name u want to search: ").lower()
        if(google_search=="youtube"):
            YT_search=input("enter your favorite channel: ").lower()
            driver=webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chrome driver\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/")
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys(google_search + Keys.ENTER)
            click=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')))
            click.click()
            driver.find_element_by_name("search_query").send_keys(YT_search)
            driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()
            play=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')))
            play.click()
        elif(google_search=="facebook"):
            driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chrome driver\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/")
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys(google_search + Keys.ENTER)
            FB_click=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/a')))
            FB_click.click()
            driver.find_element_by_name("email").send_keys("9110649656")
            driver.find_element_by_name("pass").send_keys("Rahul@#$123")
            driver.find_element_by_name("login").submit()
        elif(google_search=="amazon"):
            AMZ_search=input("what u wanna search in amazon: ")
            driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chrome driver\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/")
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys(google_search + Keys.ENTER)
            AMA_click = WebDriverWait(driver, 20).until(EC.presence_of_element_located(('xpath', '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')))
            AMA_click.click()
            driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys(AMZ_search)
            driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").submit()
        else:
            driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chrome driver\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/")
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys(google_search +Keys.ENTER)
else:
    print("1.petrol station\n2.groceries\n3.restaurant\n4.hotel")
    select=int(input("select one option to show: "))-1
    if(select==0):
        driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chrome driver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys("maps" + Keys.ENTER)
        maps_click=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3')))
        maps_click.click()
        driver.find_element_by_name("q").send_keys("gas station" + Keys.ENTER)
        gas=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[2]/button')))
        gas.click()
    elif(select==1):
        driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\Downloads\\chrome driver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys("maps" + Keys.ENTER)
        Groceries_maps=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3')))
        Groceries_maps.click()
        driver.find_element_by_name("q").send_keys("groceries" + Keys.ENTER)
        store_click=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')))
        store_click.click()
        dire_click=WebDriverWait(driver,20).until(EC.presence_of_element_located(('xpath','//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/button')))
        dire_click.click()







