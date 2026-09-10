# import asyncio
# from crawl4ai import AsyncWebCrawler

# async def main():
#     async with AsyncWebCrawler() as crawler:
#         # Replace with the URL you want to scrape
#         result = await crawler.arun(url="https://www.zomato.com/kolkata/peter-cat-park-street-area/reviews")

#         # Print clean markdown text
#         print(result.markdown)

# if __name__ == "__main__":
#     asyncio.run(main())

# import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context()
#         page = await context.new_page()
        
#         url = "https://tripadvisor.in"
#         await page.goto(url)
        
#         print("Waiting 20 seconds... If a DataDome verification screen pops up, solve it manually now!")
#         await page.wait_for_timeout(20000) 
        
#         review_elements = await page.locator("span").all_text_contents()
        
#         print("\n--- Scraped Content ---")
#         for text in review_elements:
#             if len(text.strip()) > 30: 
#                 print(f"- {text.strip()}\n")
                
#         await browser.close()

# if __name__ == "__main__":
#     asyncio.run(main())

#Data Scrapping for Air Conditioner from Amazon 

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        url = "https://www.amazon.in/s?k=air+conditioner&crid=3TA6FVV62DQES&sprefix=air+conditioner%2Caps%2C282&ref=nb_sb_noss_2" 
        await page.goto(url)
        
        print("Waiting 15 seconds... Check the window and complete any verification grids manually!")
        await page.wait_for_timeout(15000)# 1000 ms is = 1 seconds
        
        try:
            await page.wait_for_selector("[data-component-type='s-search-result']", timeout=10000)
            products = await page.locator("[data-component-type='s-search-result']").all()
            print(f"\n--- Found {len(products)} Products ---")
            
            for product in products:
                try:
                    title = await product.locator("h2, span.a-size-base-plus").first.text_content()
                    price = await product.locator("span.a-price-whole").first.text_content()
                    
                    print(f"Product: {title.strip()}")
                    print(f"Price: ₹{price.strip()}")
                    print("-" * 40)
                except Exception:
                    continue
                    
        except Exception as e:
            print("\n[Error] Timed out waiting for products. The page was likely stuck on a robot check screen.")
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())




    