# Twitter-Transfer
A python automation script that will help you transfer the following users from one account to the another.

### Getting Started
1. Clone this repo
```git
git clone https://github.com/falcon-head/Twitter-Transfer.git
```
2. Navigate to the following folder
```windows path
C:\>
C:\> cd C:\[path]\twitter_transfer\twitter_transfer>
```
3. Install all the depending libraries by running `setup.py` 
```windows path
C:\[path]\twitter_transfer\twitter_transfer>python setup.py
```
4. Download [ChromeDriver](https://chromedriver.chromium.org/downloads "Chrome Driver") extract the .exe file and place it inside `C:\[Python path]\Scripts`

### Usage
Generate the twitter accounts following list by running the following command
```windows path
C:\[path]\twitter_transfer\twitter_transfer>scrapy crawl get_follower_list -a email="twitter_email" -a password="twitter_pass" -o output.csv
```

Follow the users from the generated list using the following command
```windows path
C:\[path]\twitter_transfer\twitter_transfer>scrapy crawl get_follower_list -a email="twitter_email" -a password="twitter_pass" -a file='output.csv'
```
