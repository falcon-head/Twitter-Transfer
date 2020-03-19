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
Run `get_follower_list.py` to get the following users username.
```windows path
C:\[path]\twitter_transfer\twitter_transfer>scrapy crawl get_follower_list -a email="twitter_email" -a password="twitter_pass" -o output.csv
```
After getting the ouput in `csv` file run `follow.py` to follow the users in the users list
```windows path
C:\[path]\twitter_transfer\twitter_transfer>scrapy crawl follow -a email="twitter_email" -a password="twitter_pass" -a csv="output.csv"
```
