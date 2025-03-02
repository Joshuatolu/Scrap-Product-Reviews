from bs4 import BeautifulSoup
import re

## Function to get product details
def get_product_details(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    brand_section = None
    for div in soup.find_all('div', class_='-phs'):
        if div.find('div', class_='-pvxs') and "Brand:" in div.text:
            brand_section = div
            break

    # Extract product details
    product_details = {
        'product_name': soup.find('h1', class_='-fs20 -pts -pbxs').text.strip(),
        'brand': brand_section.find('div', class_='-pvxs').find('a').text.strip(),
        'price': re.sub(r'[^\d]', '', soup.find('span', class_='-b -ubpt -tal -fs24 -prxs').text.strip()),
        # 'description': soup.find('div', class_='markup -mhm -pvl -oxa -sc').text.strip(),
        'features': soup.find('div', class_ = 'markup -pam').text.strip(),
        'specification': soup.find('ul', class_ = '-pvs -mvxs -phm -lsn').text.strip()
    }

    return product_details