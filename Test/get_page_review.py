from bs4 import BeautifulSoup

## Function to get the reviews on each page
def get_page_review(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = soup.find_all('article', class_='-pvs -hr _bet')

    # Extract review data
    review_data = []
    for review in reviews:
        
        # Reviewer Header Comment
        try:
            reviewer_header_comment = review.find('h3', class_ = '-m -fs16 -pvs').text.strip()
        except AttributeError:
            reviewer_header_comment = ''
        
        # Reviewer Detail Comment
        try:
            reviewer_detail_comment = review.find('p', class_ = '-pvs').text.strip()
        except AttributeError:
            reviewer_detail_comment = ''
        
        # Review Dates
        try:
            review_date = review.find('span', class_ = '-prs').text
        except AttributeError:
            review_date = ''
        
        # Reviewer Name
        try:
            div = review.find("div", class_="-df -j-bet -i-ctr -gy5")
            reviewer_name = div.find_all('span')[1].text.replace('by ', '')
        except AttributeError:
            reviewer_name = ''
                
        # product star
        try:
            product_star = review.find('div', class_ = 'stars _m _al -mvs').text
        except AttributeError:
            product_star = ''
        
        review_data.append({
            'reviewer_name': reviewer_name,
            'reviewer_header_comment': reviewer_header_comment,
            'reviewer_detail_comment': reviewer_detail_comment,
            'review_date': review_date,
            'product_star': product_star
        })
    
    return review_data