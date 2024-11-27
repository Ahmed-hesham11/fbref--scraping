import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import os
from scrapy.selector import Selector



class ItemSpider(scrapy.Spider):
    name = "item"
   
    
    def start_requests(self):
        
        user_agent = UserAgent().random

        yield SeleniumRequest(
            url="https://fbref.com/en/comps/12/passing/La-Liga-Stats",
            wait_time=2,
            callback=self.parse,
            headers={'User-Agent': user_agent},
        )
    def parse(self, response):
        driver = response.meta['driver']
        time.sleep(5)
        
        html = driver.page_source
        
        response_obj = Selector(text=html)
        
        screenshot_path = os.path.join(os.getcwd(), "search_results_screenshot.png")
        driver.save_screenshot(screenshot_path)
        self.log(f"Search results screenshot saved at: {screenshot_path}")

        rows=response_obj.xpath('//div[@class="table_container is_setup"]//tbody/tr')
        for row in rows:
            yield{ 
                  #############frist sectiom #######################
                "RK":row.xpath('.//th[@class="right "]/text()').get(),
                "Player":row.xpath('.//td[@class="left "][1]//text()').get(),
                "Nation":row.xpath(".//td[@class='left poptip' and @data-stat='nationality']/a/span/text()").get(),
                "pos":row.xpath('.//td[@class="center "][1]/text()').get(),
                "Squad":row.xpath('.//td[@class="left "][2]//text()').get(),
                "Age":row.xpath('.//td[@class="center "][2]/text()').get(),
                "Born":row.xpath('.//td[@class="center "][3]/text()').get(),
                "90s":row.xpath('.//td[@class="right "][1]/text()').get(),
                ##############    section 2     ####################################################################################3
                "cmp":row.xpath('.//td[@class="right group_start"]/text()').get(),
                "Att":row.xpath('.//td[@class="right "and@data-stat="passes"]/text()').get(),
                "Cmp%":row.xpath('.//td[@data-stat="passes_pct"]/text()').get(),
                "TotDis":row.xpath('.//td[@class="right "and @data-stat="passes_total_distance"]/text()').get(),
                "PrgDist":row.xpath('.//td[@class="right "and@data-stat="passes_progressive_distance"]/text()').get(),
                
               ################### section 3 ######################################################### 
                
                "cmp2":row.xpath('.//td[@class="right group_start"][2]/text()').get(),
                "Att2":row.xpath('.//td[@class="right "and@data-stat="passes_short"]/text()').get(),
                "Cmp2%":row.xpath('.//td[@data-stat="passes_pct_short"]/text()').get(),
                
                #################################################################
                
        
                "cmp3":row.xpath('.//td[@class="right group_start"][3]/text()').get(),
                "Att3":row.xpath('.//td[@class="right "and@data-stat="passes_medium"]/text()').get(),
                "Cmp3%":row.xpath('.//td[@data-stat="passes_pct_medium"]/text()').get(),

                ######################################################################
                "cmp4":row.xpath('.//td[@class="right group_start"][4]/text()').get(),
                "Att4":row.xpath('.//td[@class="right "and@data-stat="passes_long"]/text()').get(),
                "Cmp4%":row.xpath('.//td[@data-stat="passes_pct_long"]/text()').get(),
                ########################################################################################
                "Ast":row.xpath('.//td[@data-stat="assists"]/text()').get(),
                "xAG":row.xpath('.//td[@data-stat="xg_assist"]/text()').get(),
                "xA":row.xpath('.//td[@data-stat="pass_xa"]/text()').get(),
                "A-xAG":row.xpath('.//td[@data-stat="xg_assist_net"]/text()').get(),
                "Kp":row.xpath('.//td[@data-stat="assisted_shots"]/text()').get(),
                "1/3":row.xpath('.//td[@data-stat="passes_into_final_third"]/text()').get(),
                "PPA":row.xpath('.//td[@data-stat="passes_into_penalty_area"]/text()').get(),
                "CrsPA":row.xpath('.//td[@data-stat="crosses_into_penalty_area"]/text()').get(),
                "Prgp":row.xpath('.//td[@data-stat="progressive_passes"]/text()').get(),
                
            }