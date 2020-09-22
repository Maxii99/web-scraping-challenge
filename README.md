# web-scraping-challenge


This is a web-scaping homework of building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The challenge involved using various programming tools such as BeautifulSoup, Pandas, MongoDB and Flask Application.
Filkes for this homework are contained in the folder called `web-scraping-challenge`.

Initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. The Jupyter Notebook file called `mission_to_mars.ipynb`was used to complete the scraping and analysis tasks. The following outlines scraped:

# 1. Nasa Mars News
I scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the following latest News Title and Paragraph Text to be referenced later:

```python:
news_title = "NASA's New Mars Rover Will Use X-Rays to Hunt Fossils"
--------------------------------------------------------------------
news_p = "PIXL, an instrument on the end of the Perseverance rover's arm, will search for chemical fingerprints left by ancient microbes."
```

# 2. JPL Mars Space Featured Images
I used splinter to navigate the JPL Featured Space Image site (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and found the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

```python:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA24096-640x350.jpg'
```

# 3. Mars Facts
I used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc from the Mars Facts webpage (https://space-facts.com/mars/) and use converted the data to a HTML table string.


# 4. Mars Hemisphere 
I visisted the USGS Astrogeology site(https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres. A Python dictionary to was used to store the data using the keys `img_url` and `title`, and the dictionary with the image url string and the hemisphere title was appended to a list. This list contains one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [{'title': 'Cerberus Hemisphere Enhanced',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
 {'title': 'Schiaparelli Hemisphere Enhanced',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
 {'title': 'Syrtis Major Hemisphere Enhanced',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
 {'title': 'Valles Marineris Hemisphere Enhanced',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]
]
```

# 5. MongoDB and Flask Application
I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
* The Jupyter notebook was converted into a Python script called `scrape_mars.py` with a function called `scrape` that executes all the scraping code from above and return one Python dictionary containing all of the scraped data.

* A route called `/scrape` was created that imports`scrape_mars.py` script, calls `scrape` function, and the returns value in Mongo as a Python dictionary.

* A root route `/` was created to query the Mongo database and pass the mars data into an HTML template to display the data.

* A template HTML file called `index.html` was created to take the mars data dictionary and display all of the data in the appropriate HTML elements. Screenshots of the final product are provided.
