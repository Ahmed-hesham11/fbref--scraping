
# Web Scraping Project



## Installation

### 1. Clone the Repository
Clone this project to your local machine:
```bash
git clone <repository-url>
cd <project-folder>
```



### 3. Install Required Libraries
Run the following command to install the required libraries:
```bash
pip install scrapy scrapy-selenium scrapy-proxy-pool fake-useragent
```

---

## How to Run the Project

### 1. Configure the Scrapy Project
- Edit the Scrapy settings file (`settings.py`) to include additional configurations for Selenium, proxies, and user agents.

### 2. Run the Scraper
Use the Scrapy command-line interface to run the project:
```bash
scrapy crawl <spider-name>
```

### 3. Save Output (Optional)
To save the scraped data to a file:
- JSON:
  ```bash
  scrapy crawl <spider-name> -o output.json
  ```
- CSV:
  ```bash
  scrapy crawl <spider-name> -o output.csv
  ```

---


```
