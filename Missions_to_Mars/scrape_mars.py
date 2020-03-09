{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import os\n",
    "from splinter import Browser \n",
    "from pprint import pprint\n",
    "import time\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Choose the executable path to driver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pprint(response)\n",
    "#pprint(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "time.sleep(2)\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "slide=soup.select_one('ul.item_list li.slide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Examine the results, then determine element that contains sought info\n",
    "#print(slide.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Find the title of the latest article\n",
    "news_title= slide.find('div', class_='content_title').get_text('a')\n",
    "print(f\"The title of the most recent article is: {news_title}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_paragraph = slide.find('div', class_='article_teaser_body').text\n",
    "print(news_paragraph)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "im_soup = BeautifulSoup(html, 'html.parser')\n",
    "front=\"https://www.jpl.nasa.gov\"\n",
    "try:\n",
    "    featured = im_soup.find('div', class_='img').img['src']\n",
    "    \n",
    "    if(featured):\n",
    "        print(front + featured)\n",
    "        \n",
    "except Exception as e:\n",
    "    print(e)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url=(front + featured)\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tw_soup = BeautifulSoup(html, 'html.parser')\n",
    "try:\n",
    "    mars_weather = tw_soup.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text   \n",
    "    if(featured):\n",
    "        print()\n",
    "        \n",
    "except Exception as e:\n",
    "    print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_df=tables[0]\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html_table = mars_df.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html_table.replace('\\n', '')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n",
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'text'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-d6bdde5e6e94>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mhtml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mhemi_soup\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBeautifulSoup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'html.parser'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m     \u001b[0mname1\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mhemi_soup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'div'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'description'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'a'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m     \u001b[0mimage\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mhemi_soup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'div'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'description'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'a'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'href'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'text'"
     ]
    }
   ],
   "source": [
    "image_first = 'https://astrogeology.usgs.gov'\n",
    "hemi_name=[]\n",
    "hemi_url=[]\n",
    "for x in range(4):\n",
    "    html = browser.html\n",
    "    hemi_soup = BeautifulSoup(html, 'html.parser')\n",
    "    name1=hemi_soup.find('div', class_='description').find('a').text\n",
    "    image=hemi_soup.find('div', class_='description').find('a')['href']\n",
    "    \n",
    "    print(name1)       \n",
    "    \n",
    "    image_get=image_first + image\n",
    "    \n",
    "    browser.visit(image_get)\n",
    "    html = browser.html\n",
    "    first_soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    final_1 = first_soup.find('div', class_='downloads').find('a')['href']\n",
    "    \n",
    "    print(final_1)\n",
    "    \n",
    "    name2=hemi_soup.find_all('div', class_='description')[1].find('a').text\n",
    "    image1=hemi_soup.find_all('div', class_='description')[1].find('a')['href']\n",
    "    \n",
    "    print(name2)\n",
    "    \n",
    "    image_get=image_first + image1    \n",
    "    \n",
    "    browser.visit(image_get)\n",
    "    html = browser.html\n",
    "    second_soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    final_2 = second_soup.find('div', class_='downloads').find('a')['href']\n",
    "    \n",
    "    print(final_2)\n",
    "    \n",
    "    name3=hemi_soup.find_all('div', class_='description')[2].find('a').text\n",
    "    image1=hemi_soup.find_all('div', class_='description')[2].find('a')['href']\n",
    "    \n",
    "    print(name3)\n",
    "    \n",
    "    image_get=image_first + image1    \n",
    "    \n",
    "    browser.visit(image_get)\n",
    "    html = browser.html\n",
    "    third_soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    final_3 = third_soup.find('div', class_='downloads').find('a')['href']\n",
    "    \n",
    "    print(final_3)\n",
    "    \n",
    "    name4=hemi_soup.find_all('div', class_='description')[3].find('a').text\n",
    "    image1=hemi_soup.find_all('div', class_='description')[3].find('a')['href']\n",
    "    \n",
    "    print(name4)\n",
    "    \n",
    "    image_get=image_first + image1    \n",
    "    \n",
    "    browser.visit(image_get)\n",
    "    html = browser.html\n",
    "    fourth_soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    final_4 = third_soup.find('div', class_='downloads').find('a')['href']\n",
    "    \n",
    "    print(final_4)\n",
    "    \n",
    "    try:\n",
    "        browser.back()\n",
    "        \n",
    "    except Exception as e:\n",
    "        print(e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': ['Cerberus Hemisphere Enhanced'],\n",
       "  'image url': ['http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg']},\n",
       " {'title': ['Schiaparelli Hemisphere Enhanced'],\n",
       "  'image url': ['http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg']},\n",
       " {'title': ['Syrtis Major Hemisphere Enhanced'],\n",
       "  'image url': ['http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg']},\n",
       " {'title': ['Valles Marineris Hemisphere Enhanced'],\n",
       "  'image url': ['http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg']}]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create dictionary and list\n",
    "hemisphere_image_urls=[]\n",
    "hemisphere_image_urls=[{\"title\":[name1], \"image url\":[final_1]},{\"title\":[name2], \"image url\":[final_2]},{\"title\":[name3], \"image url\":[final_3]},{\"title\":[name4], \"image url\":[final_4]}]\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
