from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建Chrome浏览器实例
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('blink-settings=imagesEnabled=false')
options.add_argument('--disable-software-rasterizer')

def get_keywords():
    
    return ['It Takes Two','A Few Good Men','Avatar: The Way of Water']

def search(driver,keyword):
    # 在搜索框中输入关键词并提交搜索
    search_box = driver.find_element(By.CLASS_NAME,"imdb-header-search__input")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果页面加载完成
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ipc-metadata-list-summary-item")))

    # 获取搜索结果中第一个电影的链接
    first_result = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")
    print(first_result)
    print(len(first_result))
    if(len(first_result)>0):
        links=first_result[0].find_elements(By.TAG_NAME,'a')
        if(len(links)>0):
            link=links[0]
            movie_url = link.get_attribute("href")
            print("movie:",keyword, movie_url)

#driver = webdriver.Chrome(options=options,executable_path='/tools/chromedriver')
driver = webdriver.Chrome(options=options)
# 打开IMDB网站
driver.get("https://www.imdb.com/")

for keyword in get_keywords():
    search(driver=driver,keyword=keyword)
# 关闭浏览器
driver.quit()