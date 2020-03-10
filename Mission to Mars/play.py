#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser 
from pprint import pprint
import time
import pandas as pd


# In[6]:


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
    


# # NASA Mars News

# In[ ]:

def scrape():
# URL of page to be scraped
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


# In[ ]:


    html = browser.html


# In[ ]:


#pprint(response)
#pprint(response.text)


# In[ ]:


# Create BeautifulSoup object; parse with 'html.parser'
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


    slide=soup.select_one('ul.item_list li.slide')


# In[ ]:


# Examine the results, then determine element that contains sought info
#print(slide.prettify())


# In[ ]:


#Find the title of the latest article
    news_title= slide.find('div', class_='content_title').get_text('a')
    print(f"The title of the most recent article is: {news_title}")


# In[ ]:


    news_paragraph = slide.find('div', class_='article_teaser_body').text
    print(news_paragraph)


# # JPL Mars Space Images - Featured Image

# In[ ]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


# In[ ]:


    html = browser.html


# In[ ]:


    im_soup = BeautifulSoup(html, 'html.parser')
    front="https://www.jpl.nasa.gov"
    try:
        featured = im_soup.find('div', class_='img').img['src']
        
        if(featured):
            print(front + featured)
        
    except Exception as e:
        print(e)
        


# In[ ]:


    featured_image_url=(front + featured)
    featured_image_url


# # Mars Weather

# In[ ]:


    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)


# In[ ]:


    html = browser.html


# In[ ]:


    tw_soup = BeautifulSoup(html, 'html.parser')
    try:
        mars_weather = tw_soup.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text   
        if(featured):
            print()
        
    except Exception as e:
        print(e)


# In[ ]:


    print(mars_weather)


# # Mars Facts

# In[ ]:


    url = 'https://space-facts.com/mars/'


# In[ ]:


    tables = pd.read_html(url)
    tables


# In[ ]:


    mars_df=tables[0]
    mars_df


# In[ ]:


    html_table = mars_df.to_html()
    html_table


# In[ ]:


    html_table.replace('\n', '')


# # Mars Hemispheres

# In[7]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


# In[8]:


    image_first = 'https://astrogeology.usgs.gov'
    hemi_name=[]
    hemi_url=[]
    for x in range(4):
        html = browser.html
        hemi_soup = BeautifulSoup(html, 'html.parser')
        name1=hemi_soup.find('div', class_='description').find('a').text
        image=hemi_soup.find('div', class_='description').find('a')['href']
        
        print(name1)       
    
        image_get=image_first + image
        
        browser.visit(image_get)
        html = browser.html
        first_soup = BeautifulSoup(html, 'html.parser')
    
        final_1 = first_soup.find('div', class_='downloads').find('a')['href']
        
        print(final_1)
    
        name2=hemi_soup.find_all('div', class_='description')[1].find('a').text
        image1=hemi_soup.find_all('div', class_='description')[1].find('a')['href']
        
        print(name2)
        
        image_get=image_first + image1    
        
        browser.visit(image_get)
        html = browser.html
        second_soup = BeautifulSoup(html, 'html.parser')
        
        final_2 = second_soup.find('div', class_='downloads').find('a')['href']
        
        print(final_2)
        
        name3=hemi_soup.find_all('div', class_='description')[2].find('a').text
        image1=hemi_soup.find_all('div', class_='description')[2].find('a')['href']
        
        print(name3)
        
        image_get=image_first + image1    
        
        browser.visit(image_get)
        html = browser.html
        third_soup = BeautifulSoup(html, 'html.parser')
        
        final_3 = third_soup.find('div', class_='downloads').find('a')['href']
        
        print(final_3)
    
        name4=hemi_soup.find_all('div', class_='description')[3].find('a').text
        image1=hemi_soup.find_all('div', class_='description')[3].find('a')['href']
        
        print(name4)
        
        image_get=image_first + image1    
        
        browser.visit(image_get)
        html = browser.html
        fourth_soup = BeautifulSoup(html, 'html.parser')
        
        final_4 = third_soup.find('div', class_='downloads').find('a')['href']
        
        print(final_4)
        
        try:
            browser.back()
        
        except Exception as e:
            print(e)


# In[27]:


#Create dictionary and list
    hemisphere_image_urls=[]
    hemisphere_image_urls=[{"title":[name1], "image url":[final_1]},{"title":[name2], "image url":[final_2]},{"title":[name3], "image url":[final_3]},{"title":[name4], "image url":[final_4]}]
    hemisphere_image_urls


# In[ ]:

    data={"title":news_title, "paragraph": news_paragraph, "featured image": featured_image_url, "Mars weather": mars_weather, "Hemispere": hemisphere_image_urls}

    return data
