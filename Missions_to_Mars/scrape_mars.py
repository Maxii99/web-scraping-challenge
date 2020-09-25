# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    # Mars News URL to scrape
    news_url = 'https://mars.nasa.gov/news/'

    browser.visit(news_url)

    html = browser.html 

    news_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest news title and paragraph
    try:

        slide_elem=news_soup.find('li', class_='slide')
        news_title = slide_elem.find('div', class_='content_title').a.text
        news_p = slide_elem.find('div', class_='article_teaser_body').text
    except AttributeError:
        news_title=None
        news_p=None
    # Mars image to scrape

    jpl_nasa_url = 'https://www.jpl.nasa.gov'
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(images_url)

    html = browser.html

    images_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve featured image link
    relative_image_path = images_soup.find_all('img')[3]["src"]
    featured_image_url = jpl_nasa_url + relative_image_path
    
    # Scrape Mars facts
    facts_url = 'https://space-facts.com/mars/'
    facts_table = pd.read_html(facts_url)
    
    # Convert table to dataframe
    mars_facts_df = facts_table[2]
    mars_facts_df.columns = ["Description", "Value"]
    
    # Convert table to html
    mars_html_table = mars_facts_df.to_html()
    
    # Clean table by replacing '\n' and print
    mars_html_table.replace('\n', '')

    # Scrape USGS website for Mars hemispheres high resolution images
    usgs_url = 'https://astrogeology.usgs.gov'
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hemispheres_url)

    hemispheres_html = browser.html

    hemispheres_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    # Mars hemispheres products data
    all_mars_hemispheres = hemispheres_soup.find('div', class_='collapsible results')
    mars_hemispheres = all_mars_hemispheres.find_all('div', class_='item')

    # Create hemisphere image urls list to append hemisphere data to
    hemisphere_image_urls = []

    # Iterate through each hemisphere data
    for i in mars_hemispheres:
        # Collect Title
        hemisphere = i.find('div', class_="description")
        title = hemisphere.h3.text
        
        # Collect image link by browsing to hemisphere page
        hemisphere_link = hemisphere.a["href"]    
        browser.visit(usgs_url + hemisphere_link)
        
        image_html = browser.html
        image_soup = BeautifulSoup(image_html, 'html.parser')
        
        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']

        # Create Dictionary to store title and url info
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_url
        
        hemisphere_image_urls.append(image_dict)



    # Mars dictionary
    mars_dict = {
            "news_title": news_title,
            "news_p": news_p,
            "featured_image_url": featured_image_url,
            "fact_table": str(mars_html_table),
            "hemisphere_images": hemisphere_image_urls
    }
    browser.quit()

    return mars_dict

if __name__ == "__main__":
    mars = scrape()
    print(mars)