import os
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from get_page_review import get_page_review
from get_details import get_product_details
from transform_df import transform_df

def jumia_scrap(product_url):
    # Configure Selenium EdgeDriver options
    options = Options()
    options.use_chromium = True
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")  # Headless mode
    options.add_argument("--disable-gpu")
    service = Service(executable_path=r'C:\Users\Joshu\OneDrive - MSFT\Documents\GitHub\eCommerce Web Scrapping\Scrap-Product-Reviews\Driver\msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=options)

    # Retry logic for loading the product page
    max_retries = 3
    for attempt in range(max_retries):
        try:
            driver.get(product_url)
            time.sleep(10)  # Wait for page to load
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed to load page: {e}")
            if attempt == max_retries - 1:
                print("Max retries reached. Exiting.")
                driver.quit()
                return

    # Get product details
    try:
        product_details = get_product_details(driver)
        product_name = re.split(r"['\"″]", product_details['product_name'])[0].replace(' ', '_')
    except Exception as e:
        print(f"Failed to get product details: {e}")
        driver.quit()
        return

    # Navigate to review page
    try:
        review_page_button = driver.find_element(By.XPATH, '//a[@class="btn _def _ti -mhs -fsh0"]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", review_page_button)
        time.sleep(2)
        review_page_button.click()
        time.sleep(10)  # Wait for review page to load
    except Exception as e:
        print("No review page button found or no reviews available:", e)

    # Scrape all reviews
    all_reviews = []
    while True:
        try:
            d_reviews = get_page_review(driver)
            all_reviews.extend(d_reviews)
            next_page_button = driver.find_element(By.XPATH, '//a[@aria-label="Next Page"]')
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_page_button)
            time.sleep(2)
            next_page_button.click()
            time.sleep(10)  # Wait for next page
        except Exception as e:
            print("No more review pages or error:", e)
            break

    driver.quit()

    # Combine product details with reviews
    for review in all_reviews:
        review.update(product_details)

    # Save to CSV
    if all_reviews:
        product_df = pd.DataFrame(all_reviews)
        real_data_df = transform_df(product_df)
        output_dir = r'Reviews\Jumia'
        file_name = f'{product_name}_reviews.csv'
        output_path = os.path.join(output_dir, file_name)
        os.makedirs(output_dir, exist_ok=True)
        real_data_df.to_csv(output_path, index=False)
        print(f'{len(product_df)} {product_name} reviews successfully written to {output_path}! Nice work!!!')
    else:
        print("No reviews collected.")