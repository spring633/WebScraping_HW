from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd
def scrape():
    url = "https://mars.nasa.gov/news/8503/robotic-toolkit-added-to-nasas-mars-2020-rover/"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    
    news_title = soup.title.text
    ### NASA Mars News
    marsData={"title":news_title}
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    html = browser.html
    img_soup = bs(html, 'html.parser')
    img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    ### JPL Mars Space Images - Featured Image
    featured_image_url ="https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18884_hires.jpg"
    
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    response_twit = requests.get(mars_weather_url)
    twit_soup = bs(response_twit.text, 'html.parser')
    last_mars_weather = twit_soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    ### Mars Weather
    mars_weather = last_mars_weather[1].text

    table_url = "https://space-facts.com/mars/"
    table = pd.read_html(table_url)
    df = table[0]
    df = df.iloc[0:10,0:2]
    ### Mars Facts
    mars_html_table = df.to_html('table.html')

    Ast_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(Ast_url)
    browser.is_element_present_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('Cerberus Hemisphere Enhanced')
    more_info_elem.click()
    html = browser.html
    che_soup = bs(html, 'html.parser')
    cerberus_title = che_soup.find('h2', class_="title").text
    results = che_soup.find_all('img', class_="wide-image")
    che_src = results[0].get("src")
    che_src_url = 'https://astrogeology.usgs.gov'+ che_src
    Ast_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(Ast_url)
    browser.is_element_present_by_text('Schiaparelli Hemisphere Enhanced', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    more_info_elem.click()
    html = browser.html
    sch_soup = bs(html, 'html.parser')
    Schiaparelli_title = sch_soup.find('h2', class_="title").text
    sch_result = sch_soup.find_all('img', class_="wide-image")
    sch_img = sch_result[0].get("src")
    sch_img_url = 'https://astrogeology.usgs.gov'+ sch_img
    Ast_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(Ast_url)
    browser.is_element_present_by_text('Syrtis Major Hemisphere Enhanced', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    more_info_elem.click()
    html = browser.html
    syr_soup = bs(html, 'html.parser')
    syr_title = syr_soup.find('h2', class_="title").text
    syr_result = syr_soup.find_all('img', class_="wide-image")
    syr_img = syr_result[0].get("src")
    syr_img_url = 'https://astrogeology.usgs.gov'+ syr_img
    Ast_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(Ast_url)
    browser.is_element_present_by_text('Valles Marineris Hemisphere Enhanced', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    more_info_elem.click()
    html = browser.html
    vall_soup = bs(html, 'html.parser')
    vall_title = vall_soup.find('h2', class_="title").text
    vall_result = vall_soup.find_all('img', class_="wide-image")
    vall_img = vall_result[0].get("src")
    vall_img_url =  'https://astrogeology.usgs.gov' +vall_img
    ## Mars Hemispheres
    hemisphere_image_urls = [
   {"title": cerberus_title, "img_url": che_src_url},
   {"title": Schiaparelli_title, "img_url": sch_img_url},
   {"title": syr_title, "img_url": syr_img_url},
   {"title": vall_title, "img_url": vall_img_url},
    ]  
    
    

    return featured_image_url,marsData,mars_weather,mars_html_table,hemisphere_image_urls
    #return marsData 


