#### Script for scraping Insight Crime
#### Developed by Alejandro Beltran and Laura Werthmann
# 3/17/2020

import scrapy
from insight.Insightitems import InsightItem
import re

class InsightCrime(scrapy.Spider):
    name = "Crime_spider"
    #URL for news repository
    start_urls = ["https://www.insightcrime.org/category/news/"]

    npages = 2
    #Let's make sure the spider is going through multiple pages of articles
    for i in range(2, npages +2):
        start_urls.append("https://www.insightcrime.org/category/news/page/"+str(i)+"")
    def parse(self, response):
        #this finds all the URL's on the /news/ webpage, about 12 per page
        for href in response.xpath("//h3[contains(@class, 'entry-title td-module-title')]/a//@href"):
            #For each url that it finds we need scrapy to open it so we can do things with it.
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = InsightItem()
        #get link
        item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()
        #get title
        item['title'] = response.xpath("//h1[contains(@class, 'entry-title')]/descendant::text()").extract()[0]
        #get authors
        item['author']  = response.xpath("//div[contains(@class, 'td-post-author-name-con-obv')]/descendant::text()").extract()
        # get tags
        item['tags'] = response.xpath("//div[contains(@class, 'tags-template-1')]/descendant::text()").extract()
        #article type
        item['type'] = response.xpath("//li[contains(@class, 'entry-category')]/descendant::text()").extract()
        #date of publication
        date = response.xpath("//time[contains(@class, 'entry-date updated td-module-date')]/@datetime").extract()
        date = "".join(date)
        item['date'] = date.split("T")[0]
        #content
        story_list = response.xpath("//div[contains(@class, 'td-post-content')]/descendant::text()").extract()
        story_list = [x.strip() for x in story_list if len(x.strip()) > 0 ]
        item['content'] = "\n".join(story_list)
        yield item
