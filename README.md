# Web Scraping Project: Extracting Product Reviews from E-commerce Websites
## Overview
This project focuses on extracting product reviews from various e-commerce websites using web scraping techniques. The primary goal is to gather detailed customer feedback, including reviewer names, comments, ratings, and dates in order to analyze customer sentiment by data analysts. The project utilizes Python libraries such as BeautifulSoup, Selenium, and Pandas to automate the scraping process and store the data in a structured format (CSV).

The project includes scripts for scraping reviews from multiple websites, each with its unique structure and logic. This repository contains the code, documentation, and sample outputs for the scraping process.

## Key Features
+ Web Scraping: Automated extraction of product reviews from e-commerce websites.

+ Dynamic Page Handling: Uses Selenium to handle dynamic content, such as "View More" buttons and pagination and BeautifulSoup to extract the necessary data.

+ Data Extraction: Extracts reviewer names, comments, dates, and ratings.

+ Data Storage: The scrapped data is saved into CSV files for further analysis.


## Tools Used
  - Python: Language for scripting.

  - BeautifulSoup: For parsing HTML and extracting data.

  - Selenium: For automating browser interactions and handling dynamic content.

  - Pandas: For data manipulation and storing scraped data in CSV format.

  - EdgeDriver: For controlling the Microsoft Edge browser via Selenium.

#### Repository Structure
```
web-scraping-project/
│
├── scripts/                         # Contains all scraping scripts
│   ├── jumia_scrapping.ipynb        # Script for scraping Jumia product reviews
│   ├── ebay_scrapping.ipynb         # Script for scraping reviews from another website
│   └── shopify_scrapping.ipynb      # Script for scraping reviews from a third website
│
├── Reviews/                         # Contains scraped data in CSV format
│   ├── Jumia/
│   │   └──Ace_Laptop_reviews.csv    # Sample output from [Jumia NG](https://jumia.com.ng/)
│   ├── Ebay
│   │   └──Laptop_Stand_reviews.csv  # Sample output from [ebay.com](https://ebay.com/)
│   └── Shopify
│       └──MercKeyboard_reviews.csv  # Sample output from [Shopify](https://shop.app/)
│
├── Driver/                          # Contains the EdgeDriver executable
│   └── msedgedriver.exe             # EdgeDriver for Selenium
│
└── README.md                        # Project documentation
```

>### Contact
For questions or feedback, please reach out to me at toluseonibiyo@gmail.com.

Happy Scraping! 🚀
