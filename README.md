# Insight Crime Crawl
Script for scraping news from Insight Crime and saving in CSV format
Developed by Alejandro Beltran and Laura Werthmann
3/17/2020

## Steps for running the Scrapy Spider

1. Create an anaconda environment with Scrapy and Python=3.6
```python
  conda create --name insight python=3.6 Scrapy
  conda activate insight
  ```
2. Activate the environment
3. Download the insight folder from github and cd into the folder, you should be at the same level as scrapy.cfg.
4. Navigate to inisght/spiders/ and open Crime_spider.py. This is the script that does the crawling. You can see the xpaths we are navigating to in order to extract the contents. In this test version the number of pages to scrape is reduced to the first three, but you can change this by changing "npages" to your desired #.
5. Open file inisght/settings.py and change the USER_AGENT to your own identifiable information. In this file I have added a 2 second delay between pages, to avoid overwhelming the website, as well as the AUTOTHROTTLE feature which slows down the spider if its putting too much strain on the website. I have also enabled the LOG_LEVEL = 'INFO' feature which captures the print out of the script to avoid overwhelming your computer.
6. After making your edits, we are ready to run the spider, in your anaconda terminal run the below command:
```python
  scrapy crawl Crime_spider -o file_name.csv
```
- a. the scrapy command tells python we are using scrapy,
- b. the crawl command tells scrapy we are going to use a spider,
- c. the Crime_spider is the script we are using, aka the spider,
- d. -o is the output and the file_name.csv is the desired filename in csv format.

7. Once it has concluded, check the insight/ folder for the csv and check out the output. Remember that excel struggles with utf-8 encoding, so don't be alarmed if the content column has funny characters.
Happy scraping!

P.S. I built this spider using the following tutorials, check them out if you want more detailed info of the steps and process.

https://docs.scrapy.org/en/latest/intro/tutorial.html

https://towardsdatascience.com/using-scrapy-to-build-your-own-dataset-64ea2d7d4673

https://github.com/mGalarnyk/Python_Tutorials/tree/master/Scrapy


Notes:

3/17/20: For each article, the crawler is extracting the content, in the process I remove white space and try to preserve paragraph structures. Insight crime splits the text for links within paragraphs
into its own html and this is breaking the paragraph structure. So it will have a paragraph saying 20 people died and if there is a link

it breaks

like this until it either finds another link

or gets to the end of the paragraph. I would suggest we combine all text into a single string to avoid this problem but I know Eventus ID cares about paragraph strcuture so I left it this way.
