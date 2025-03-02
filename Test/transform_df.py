import pandas as pd

## Function to Transform the datafram before saving
def transform_df(df):
    s_df = df.copy()
    new_df = pd.DataFrame()
    
    new_df['Brand'] = s_df['brand']
    new_df['Product Name'] = s_df['product_name']
    new_df['Price'] = s_df['price']
    new_df['Features'] = s_df['features']
    new_df['Specification'] = s_df['specification']
    new_df['Reviewer Name'] = s_df['reviewer_name']
    new_df['Review Date'] = s_df['review_date']
    new_df['Rating'] = s_df['product_star']
    new_df['Reviewer Comment'] = s_df['reviewer_header_comment'] + ' ' + s_df['reviewer_detail_comment']
    new_df.insert(0, 'Store', 'Jumia Nigeria')
    new_df.insert(1, 'Product Type', 'Phones')

    return new_df