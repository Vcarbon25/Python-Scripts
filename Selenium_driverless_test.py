
# import the required libraries
from selenium_driverless import webdriver # this module don't require an external driver, and may be used as it is
import asyncio
"""
def scraper():

    with webdriver.Chrome() as browser:
    
        # open the target website
        browser.get("https://httpbin.io/")

        # implicitly wait for the page to load
        browser.sleep(1.0)

        # extract the page's full HTML
        print(browser.page_source)

        # quit the driver
        #browser.quit()
        
# run the function
scraper()
"""
async def scraper():

    async with webdriver.Chrome() as browser:

        # open the target website
        await browser.get("https://www.uol.com.br/")

        # implicitly wait for the page to load
        await browser.sleep(5.0)

        # extract the page's full HTML
        print(await browser.page_source)

        # quit the driver
        await browser.quit()

# run the function
asyncio.run(scraper())